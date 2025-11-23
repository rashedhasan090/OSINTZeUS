#!/usr/bin/env python3
"""
OSINTZeUS - Open Source Intelligence Gathering Tool
Backend API Server
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import json
import uuid
from datetime import datetime
from werkzeug.utils import secure_filename
import traceback

from osint_modules.social_media import SocialMediaSearch
from osint_modules.image_search import ImageSearch
from osint_modules.phone_lookup import PhoneLookup
from osint_modules.email_lookup import EmailLookup
from osint_modules.address_lookup import AddressLookup
from osint_modules.wifi_scanner import WiFiScanner
from utils.report_generator import ReportGenerator

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Create uploads directory
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('reports', exist_ok=True)

# Initialize OSINT modules
social_media = SocialMediaSearch()
image_search = ImageSearch()
phone_lookup = PhoneLookup()
email_lookup = EmailLookup()
address_lookup = AddressLookup()
wifi_scanner = WiFiScanner()
report_generator = ReportGenerator()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/api/search/name', methods=['POST'])
def search_by_name():
    """Search by name or username"""
    try:
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({'error': 'Name is required'}), 400
        
        name = data['name']
        options = data.get('options', {})
        
        results = {
            'query': name,
            'timestamp': datetime.now().isoformat(),
            'search_id': str(uuid.uuid4()),
            'results': {}
        }
        
        # Social media search
        if options.get('social_media', True):
            results['results']['social_media'] = social_media.search(name)
        
        # Email search
        if options.get('email', True):
            results['results']['emails'] = email_lookup.search_by_name(name)
        
        # Phone search
        if options.get('phone', True):
            results['results']['phones'] = phone_lookup.search_by_name(name)
        
        # Address search
        if options.get('address', True):
            results['results']['addresses'] = address_lookup.search_by_name(name)
        
        return jsonify(results), 200
    
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()}), 500

@app.route('/api/search/image', methods=['POST'])
def search_by_image():
    """Reverse image search"""
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type'}), 400
        
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        results = {
            'query': filename,
            'timestamp': datetime.now().isoformat(),
            'search_id': str(uuid.uuid4()),
            'results': image_search.reverse_search(filepath)
        }
        
        # Clean up uploaded file
        os.remove(filepath)
        
        return jsonify(results), 200
    
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()}), 500

@app.route('/api/search/phone/<phone_number>', methods=['GET'])
def search_by_phone(phone_number):
    """Search by phone number"""
    try:
        results = {
            'query': phone_number,
            'timestamp': datetime.now().isoformat(),
            'search_id': str(uuid.uuid4()),
            'results': phone_lookup.lookup(phone_number)
        }
        return jsonify(results), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/search/email/<email>', methods=['GET'])
def search_by_email(email):
    """Search by email address"""
    try:
        results = {
            'query': email,
            'timestamp': datetime.now().isoformat(),
            'search_id': str(uuid.uuid4()),
            'results': email_lookup.lookup(email)
        }
        return jsonify(results), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/search/wifi', methods=['POST'])
def search_wifi():
    """Scan for WiFi networks (requires authorization)"""
    try:
        data = request.get_json()
        location = data.get('location') if data else None
        
        results = {
            'timestamp': datetime.now().isoformat(),
            'search_id': str(uuid.uuid4()),
            'results': wifi_scanner.scan(location)
        }
        return jsonify(results), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/report/<report_id>', methods=['GET'])
def get_report(report_id):
    """Get generated OSINT report"""
    try:
        report_path = os.path.join('reports', f'{report_id}.json')
        if os.path.exists(report_path):
            with open(report_path, 'r') as f:
                report = json.load(f)
            return jsonify(report), 200
        else:
            return jsonify({'error': 'Report not found'}), 404
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/report/generate', methods=['POST'])
def generate_report():
    """Generate comprehensive OSINT report"""
    try:
        data = request.get_json()
        search_results = data.get('search_results', {})
        
        report_id = str(uuid.uuid4())
        report = report_generator.generate(search_results, report_id)
        
        # Save report
        report_path = os.path.join('reports', f'{report_id}.json')
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        return jsonify({
            'report_id': report_id,
            'report': report
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify({'error': 'File too large'}), 413

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)


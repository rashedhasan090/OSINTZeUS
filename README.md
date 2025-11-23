# OSINTZeUS 🔍

**Open Source Intelligence Gathering Tool**

A powerful, web-based OSINT (Open Source Intelligence) tool that can gather information from names, images, and other identifiers. OSINTZeUS helps security researchers, investigators, and authorized personnel collect publicly available information efficiently.

![OSINTZeUS](https://img.shields.io/badge/OSINTZeUS-v1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Node.js](https://img.shields.io/badge/Node.js-16+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ⚠️ Disclaimer

**This tool is for educational and authorized security research purposes only.** 

- Only use this tool on systems and data you own or have explicit written permission to test
- Unauthorized use of OSINT tools may violate privacy laws and terms of service
- Users are solely responsible for ensuring compliance with applicable laws and regulations
- The authors assume no liability for misuse of this software

## 🚀 Features

### Core Capabilities
- **Name-based Search**: Find information using full names, usernames, or aliases
- **Image Reverse Search**: Upload images to find matches across multiple platforms
- **Social Media Discovery**: Find profiles on major platforms
- **Contact Information**: Extract phone numbers, email addresses
- **Address & Location**: Find physical addresses and map locations
- **WiFi Network Discovery**: Identify nearby networks (with proper authorization)
- **Comprehensive Reports**: Generate detailed OSINT reports

### Supported Platforms
- Social Media: Twitter/X, Facebook, Instagram, LinkedIn, GitHub, Reddit
- Image Search: Google Images, TinEye, Yandex
- People Search: Various public databases
- Maps: Google Maps, OpenStreetMap integration

## 📋 Requirements

- Python 3.8+
- Node.js 16+
- npm or yarn
- Internet connection

## 🛠️ Installation

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
```

## 🎯 Usage

### Development Mode

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate
python app.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

### Production Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

## 📖 API Documentation

### Endpoints

#### POST `/api/search/name`
Search by name/username

**Request:**
```json
{
  "name": "John Doe",
  "options": {
    "social_media": true,
    "email": true,
    "phone": true
  }
}
```

#### POST `/api/search/image`
Reverse image search

**Request:**
- Multipart form data with `image` file

#### GET `/api/search/phone/{phone_number}`
Search by phone number

#### GET `/api/search/email/{email}`
Search by email address

#### GET `/api/report/{report_id}`
Get generated OSINT report

## 🏗️ Project Structure

```
OSINTZeUS/
├── backend/
│   ├── app.py                 # Flask application
│   ├── osint_modules/         # OSINT gathering modules
│   │   ├── social_media.py
│   │   ├── image_search.py
│   │   ├── phone_lookup.py
│   │   ├── email_lookup.py
│   │   └── address_lookup.py
│   ├── utils/                 # Utility functions
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/       # React components
│   │   ├── services/          # API services
│   │   └── App.js
│   ├── package.json
│   └── public/
├── docs/                      # Documentation
└── README.md
```

## 🔧 Configuration

Create a `.env` file in the backend directory:

```env
FLASK_ENV=development
FLASK_DEBUG=True
API_KEY_GOOGLE=your_google_api_key
API_KEY_TINEYE=your_tineye_api_key
```

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Flask and React
- Uses various open-source OSINT tools and APIs
- Inspired by the security research community

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Remember: Use responsibly and ethically. Always obtain proper authorization before conducting OSINT research.**


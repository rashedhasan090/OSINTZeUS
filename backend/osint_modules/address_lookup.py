"""
Address and Location Lookup Module
"""

import requests
from typing import Dict, List
import googlemaps
import os

class AddressLookup:
    """Address and location lookup"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        # Initialize Google Maps client if API key is available
        self.gmaps = None
        api_key = os.environ.get('GOOGLE_MAPS_API_KEY')
        if api_key:
            try:
                self.gmaps = googlemaps.Client(key=api_key)
            except Exception as e:
                print(f"Google Maps initialization error: {e}")
    
    def search_by_name(self, name: str) -> List[Dict]:
        """Search addresses by name"""
        results = []
        try:
            if self.gmaps:
                # Use Google Maps Geocoding API
                geocode_result = self.gmaps.geocode(name)
                for result in geocode_result[:5]:
                    results.append({
                        'formatted_address': result.get('formatted_address'),
                        'location': result.get('geometry', {}).get('location'),
                        'place_id': result.get('place_id'),
                        'types': result.get('types')
                    })
            else:
                results.append({
                    'note': 'Google Maps API key required for address lookup',
                    'name': name
                })
        except Exception as e:
            print(f"Address lookup error: {e}")
        return results
    
    def geocode(self, address: str) -> Dict:
        """Geocode an address to coordinates"""
        result = {
            'address': address,
            'coordinates': None,
            'formatted_address': None
        }
        
        try:
            if self.gmaps:
                geocode_result = self.gmaps.geocode(address)
                if geocode_result:
                    location = geocode_result[0].get('geometry', {}).get('location')
                    result['coordinates'] = {
                        'lat': location.get('lat'),
                        'lng': location.get('lng')
                    }
                    result['formatted_address'] = geocode_result[0].get('formatted_address')
        except Exception as e:
            result['error'] = str(e)
        
        return result
    
    def reverse_geocode(self, lat: float, lng: float) -> Dict:
        """Reverse geocode coordinates to address"""
        result = {
            'coordinates': {'lat': lat, 'lng': lng},
            'address': None
        }
        
        try:
            if self.gmaps:
                reverse_result = self.gmaps.reverse_geocode((lat, lng))
                if reverse_result:
                    result['address'] = reverse_result[0].get('formatted_address')
        except Exception as e:
            result['error'] = str(e)
        
        return result


"""
Social Media OSINT Module
Searches for profiles across multiple social media platforms
"""

import requests
from bs4 import BeautifulSoup
import re
import json
from typing import Dict, List

class SocialMediaSearch:
    """Search for social media profiles"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def search(self, name: str) -> Dict[str, List[Dict]]:
        """Search for social media profiles by name"""
        results = {
            'github': self.search_github(name),
            'twitter': self.search_twitter(name),
            'linkedin': self.search_linkedin(name),
            'instagram': self.search_instagram(name),
            'facebook': self.search_facebook(name),
            'reddit': self.search_reddit(name),
        }
        return results
    
    def search_github(self, username: str) -> List[Dict]:
        """Search GitHub profiles"""
        results = []
        try:
            url = f"https://api.github.com/search/users?q={username}"
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                for user in data.get('items', [])[:5]:
                    results.append({
                        'username': user.get('login'),
                        'profile_url': user.get('html_url'),
                        'avatar': user.get('avatar_url'),
                        'type': user.get('type')
                    })
        except Exception as e:
            print(f"GitHub search error: {e}")
        return results
    
    def search_twitter(self, username: str) -> List[Dict]:
        """Search Twitter/X profiles"""
        results = []
        try:
            # Using web search as API requires authentication
            url = f"https://twitter.com/{username}"
            response = requests.get(url, headers=self.headers, timeout=10, allow_redirects=False)
            if response.status_code == 200:
                results.append({
                    'username': username,
                    'profile_url': url,
                    'platform': 'Twitter/X'
                })
        except Exception as e:
            print(f"Twitter search error: {e}")
        return results
    
    def search_linkedin(self, name: str) -> List[Dict]:
        """Search LinkedIn profiles"""
        results = []
        try:
            # LinkedIn requires authentication, using public search
            search_url = f"https://www.linkedin.com/pub/dir/?first={name.split()[0]}&last={name.split()[-1] if len(name.split()) > 1 else ''}"
            results.append({
                'name': name,
                'search_url': search_url,
                'platform': 'LinkedIn',
                'note': 'LinkedIn requires login for full access'
            })
        except Exception as e:
            print(f"LinkedIn search error: {e}")
        return results
    
    def search_instagram(self, username: str) -> List[Dict]:
        """Search Instagram profiles"""
        results = []
        try:
            url = f"https://www.instagram.com/{username}/"
            response = requests.get(url, headers=self.headers, timeout=10, allow_redirects=False)
            if response.status_code == 200:
                results.append({
                    'username': username,
                    'profile_url': url,
                    'platform': 'Instagram'
                })
        except Exception as e:
            print(f"Instagram search error: {e}")
        return results
    
    def search_facebook(self, name: str) -> List[Dict]:
        """Search Facebook profiles"""
        results = []
        try:
            # Facebook search URL
            search_url = f"https://www.facebook.com/search/people/?q={name}"
            results.append({
                'name': name,
                'search_url': search_url,
                'platform': 'Facebook',
                'note': 'Facebook requires login for full access'
            })
        except Exception as e:
            print(f"Facebook search error: {e}")
        return results
    
    def search_reddit(self, username: str) -> List[Dict]:
        """Search Reddit profiles"""
        results = []
        try:
            url = f"https://www.reddit.com/user/{username}/"
            response = requests.get(url, headers=self.headers, timeout=10, allow_redirects=False)
            if response.status_code == 200:
                results.append({
                    'username': username,
                    'profile_url': url,
                    'platform': 'Reddit'
                })
        except Exception as e:
            print(f"Reddit search error: {e}")
        return results


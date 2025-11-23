"""
WiFi Network Scanner Module
Note: Requires proper authorization and may be platform-specific
"""

import subprocess
import platform
import re
from typing import Dict, List

class WiFiScanner:
    """WiFi network scanning (requires authorization)"""
    
    def __init__(self):
        self.system = platform.system()
    
    def scan(self, location: str = None) -> Dict:
        """Scan for WiFi networks"""
        results = {
            'networks': [],
            'location': location,
            'platform': self.system,
            'note': 'WiFi scanning requires proper authorization and may be restricted'
        }
        
        try:
            if self.system == 'Linux':
                networks = self.scan_linux()
            elif self.system == 'Darwin':  # macOS
                networks = self.scan_macos()
            elif self.system == 'Windows':
                networks = self.scan_windows()
            else:
                networks = []
            
            results['networks'] = networks
        except Exception as e:
            results['error'] = str(e)
            results['note'] = 'WiFi scanning may require elevated permissions'
        
        return results
    
    def scan_linux(self) -> List[Dict]:
        """Scan WiFi on Linux using nmcli or iwlist"""
        networks = []
        try:
            # Try nmcli first (NetworkManager)
            result = subprocess.run(['nmcli', '-t', '-f', 'SSID,SIGNAL,SECURITY', 'device', 'wifi', 'list'],
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                for line in result.stdout.strip().split('\n'):
                    if line:
                        parts = line.split(':')
                        if len(parts) >= 3:
                            networks.append({
                                'ssid': parts[0],
                                'signal': parts[1],
                                'security': parts[2]
                            })
        except Exception as e:
            print(f"Linux WiFi scan error: {e}")
        
        return networks[:10]  # Limit to 10 networks
    
    def scan_macos(self) -> List[Dict]:
        """Scan WiFi on macOS using airport command"""
        networks = []
        try:
            # macOS airport utility
            airport_path = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport'
            result = subprocess.run([airport_path, '-s'],
                                   capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')[1:]  # Skip header
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 6:
                        networks.append({
                            'ssid': parts[0],
                            'bssid': parts[1],
                            'rssi': parts[2],
                            'channel': parts[3],
                            'security': ' '.join(parts[4:])
                        })
        except Exception as e:
            print(f"macOS WiFi scan error: {e}")
        
        return networks[:10]
    
    def scan_windows(self) -> List[Dict]:
        """Scan WiFi on Windows using netsh"""
        networks = []
        try:
            result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'],
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if 'All User Profile' in line or 'User Profile' in line:
                        ssid_match = re.search(r':\s*(.+)', line)
                        if ssid_match:
                            networks.append({
                                'ssid': ssid_match.group(1).strip(),
                                'note': 'Saved profile'
                            })
        except Exception as e:
            print(f"Windows WiFi scan error: {e}")
        
        return networks[:10]


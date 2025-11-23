"""
Report Generator Module
Generates comprehensive OSINT reports
"""

from datetime import datetime
from typing import Dict, List

class ReportGenerator:
    """Generate OSINT reports"""
    
    def generate(self, search_results: Dict, report_id: str) -> Dict:
        """Generate comprehensive OSINT report"""
        report = {
            'report_id': report_id,
            'generated_at': datetime.now().isoformat(),
            'summary': self._generate_summary(search_results),
            'findings': self._extract_findings(search_results),
            'recommendations': self._generate_recommendations(search_results),
            'raw_data': search_results
        }
        return report
    
    def _generate_summary(self, results: Dict) -> Dict:
        """Generate report summary"""
        summary = {
            'total_findings': 0,
            'social_media_profiles': 0,
            'email_addresses': 0,
            'phone_numbers': 0,
            'addresses': 0,
            'images_found': 0
        }
        
        if 'results' in results:
            results_data = results['results']
            
            # Count social media profiles
            if 'social_media' in results_data:
                for platform, profiles in results_data['social_media'].items():
                    summary['social_media_profiles'] += len(profiles)
            
            # Count emails
            if 'emails' in results_data:
                summary['email_addresses'] = len(results_data['emails'])
            
            # Count phones
            if 'phones' in results_data:
                summary['phone_numbers'] = len(results_data['phones'])
            
            # Count addresses
            if 'addresses' in results_data:
                summary['addresses'] = len(results_data['addresses'])
            
            # Count images
            if 'image' in results_data:
                summary['images_found'] = len(results_data.get('image', {}).get('results', []))
        
        summary['total_findings'] = (
            summary['social_media_profiles'] +
            summary['email_addresses'] +
            summary['phone_numbers'] +
            summary['addresses'] +
            summary['images_found']
        )
        
        return summary
    
    def _extract_findings(self, results: Dict) -> List[Dict]:
        """Extract key findings"""
        findings = []
        
        if 'results' in results:
            results_data = results['results']
            
            # Social media findings
            if 'social_media' in results_data:
                for platform, profiles in results_data['social_media'].items():
                    if profiles:
                        findings.append({
                            'type': 'social_media',
                            'platform': platform,
                            'count': len(profiles),
                            'severity': 'medium'
                        })
            
            # Email findings
            if 'emails' in results_data and results_data['emails']:
                findings.append({
                    'type': 'email',
                    'count': len(results_data['emails']),
                    'severity': 'high'
                })
            
            # Phone findings
            if 'phones' in results_data and results_data['phones']:
                findings.append({
                    'type': 'phone',
                    'count': len(results_data['phones']),
                    'severity': 'high'
                })
        
        return findings
    
    def _generate_recommendations(self, results: Dict) -> List[str]:
        """Generate recommendations based on findings"""
        recommendations = []
        
        if 'results' in results:
            results_data = results['results']
            
            if 'social_media' in results_data:
                recommendations.append("Review social media privacy settings")
            
            if 'emails' in results_data and results_data['emails']:
                recommendations.append("Consider using email aliases for public registrations")
            
            if 'phones' in results_data and results_data['phones']:
                recommendations.append("Be cautious sharing phone numbers publicly")
        
        if not recommendations:
            recommendations.append("No specific recommendations at this time")
        
        return recommendations


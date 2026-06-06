"""
SimilarWeb爬虫模块
用于抓取流量数据
"""

import requests
from bs4 import BeautifulSoup
import logging
from typing import Dict, Any
from datetime import datetime

logger = logging.getLogger(__name__)

class SimilarWebScraper:
    """SimilarWeb免费版爬虫"""
    
    def __init__(self):
        self.base_url = "https://www.similarweb.com/website"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def get_traffic_summary(self, website: str) -> Dict[str, Any]:
        """获取流量摘要
        
        Args:
            website: 网站域名（如 example.com）
            
        Returns:
            Dict: 包含流量数据的字典
        """
        # 清理域名
        domain = website.replace('https://', '').replace('http://', '').split('/')[0]
        url = f"{self.base_url}/{domain}"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # 提取流量数据
                traffic_data = {
                    'domain': domain,
                    'total_visits': self._extract_visits(soup),
                    'bounce_rate': self._extract_bounce_rate(soup),
                    'pages_per_visit': self._extract_pages_per_visit(soup),
                    'avg_visit_duration': self._extract_visit_duration(soup),
                    'traffic_sources': self._extract_traffic_sources(soup),
                    'top_countries': self._extract_top_countries(soup),
                    'source_url': url,
                    'confidence': '中',
                    'scraped_at': datetime.now().isoformat()
                }
                
                logger.info(f"成功获取 {domain} 的流量数据")
                return traffic_data
            else:
                logger.warning(f"SimilarWeb返回状态码: {response.status_code}")
                return self._fallback_data(domain, url, f'状态码: {response.status_code}')
                
        except Exception as e:
            logger.error(f"SimilarWeb抓取失败: {e}")
            return self._fallback_data(domain, url, str(e))
    
    def _extract_visits(self, soup) -> str:
        """提取访问量"""
        try:
            visits_elem = soup.find('span', {'class': 'engagementInfo-value'})
            return visits_elem.text.strip() if visits_elem else 'N/A'
        except:
            return 'N/A'
    
    def _extract_bounce_rate(self, soup) -> str:
        """提取跳出率"""
        try:
            bounce_elem = soup.find('div', {'data-test': 'bounce-rate'})
            return bounce_elem.text.strip() if bounce_elem else 'N/A'
        except:
            return 'N/A'
    
    def _extract_pages_per_visit(self, soup) -> str:
        """提取每次访问页数"""
        try:
            pages_elem = soup.find('div', {'data-test': 'pages-per-visit'})
            return pages_elem.text.strip() if pages_elem else 'N/A'
        except:
            return 'N/A'
    
    def _extract_visit_duration(self, soup) -> str:
        """提取平均访问时长"""
        try:
            duration_elem = soup.find('div', {'data-test': 'avg-visit-duration'})
            return duration_elem.text.strip() if duration_elem else 'N/A'
        except:
            return 'N/A'
    
    def _extract_traffic_sources(self, soup) -> Dict[str, str]:
        """提取流量来源"""
        sources = {}
        try:
            source_items = soup.find_all('div', {'class': 'trafficSources-chartItem'})
            
            for item in source_items:
                label = item.find('span', {'class': 'trafficSources-chartLabel'})
                value = item.find('span', {'class': 'trafficSources-chartValue'})
                
                if label and value:
                    sources[label.text.strip()] = value.text.strip()
        except:
            pass
        
        return sources
    
    def _extract_top_countries(self, soup) -> list:
        """提取主要国家"""
        countries = []
        try:
            country_items = soup.find_all('div', {'class': 'country-item'})
            
            for item in country_items[:5]:  # 前5个国家
                name = item.find('span', {'class': 'country-name'})
                share = item.find('span', {'class': 'country-share'})
                
                if name and share:
                    countries.append({
                        'country': name.text.strip(),
                        'share': share.text.strip()
                    })
        except:
            pass
        
        return countries
    
    def _fallback_data(self, domain: str, url: str, error: str) -> Dict[str, Any]:
        """返回备用数据"""
        return {
            'domain': domain,
            'total_visits': '需要手动查询',
            'bounce_rate': '需要手动查询',
            'pages_per_visit': '需要手动查询',
            'avg_visit_duration': '需要手动查询',
            'traffic_sources': {},
            'top_countries': [],
            'source_url': url,
            'confidence': '低',
            'error': error,
            'note': 'SimilarWeb爬虫需要维护，建议手动访问上述链接获取数据',
            'scraped_at': datetime.now().isoformat()
        }

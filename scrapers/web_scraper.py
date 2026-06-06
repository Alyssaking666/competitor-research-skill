"""
通用网页爬虫模块
用于抓取竞品官网信息
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)

class WebScraper:
    """通用网页爬虫"""
    
    def __init__(self, timeout: int = 10, delay: int = 2):
        self.timeout = timeout
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def extract_products(self, website: str) -> Dict[str, Any]:
        """提取产品信息"""
        try:
            response = self.session.get(website, timeout=self.timeout)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            products = []
            
            # 常见的产品选择器
            product_selectors = [
                '.product', '.product-item', '.product-card',
                '[class*="product"]', '[class*="item"]'
            ]
            
            for selector in product_selectors:
                items = soup.select(selector)
                for item in items[:10]:  # 限制数量
                    product = self._extract_product_info(item)
                    if product:
                        products.append(product)
            
            return {
                'products': products,
                'total_found': len(products),
                'source_url': website,
                'confidence': '中' if products else '低',
                'scraped_at': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"提取产品信息失败: {e}")
            return {
                'error': str(e),
                'source_url': website,
                'confidence': '低',
                'scraped_at': datetime.now().isoformat()
            }
    
    def _extract_product_info(self, element) -> Optional[Dict[str, str]]:
        """提取单个产品信息"""
        product = {}
        
        # 产品名称
        name_elem = element.find(['h1', 'h2', 'h3', 'h4', '.title', '.name'])
        if name_elem:
            product['name'] = name_elem.get_text(strip=True)
        
        # 产品价格
        price_elem = element.find(['.price', '[class*="price"]', '[class*="cost"]'])
        if price_elem:
            product['price'] = price_elem.get_text(strip=True)
        
        # 产品描述
        desc_elem = element.find(['.description', '.desc', 'p'])
        if desc_elem:
            product['description'] = desc_elem.get_text(strip=True)[:200]
        
        # 产品链接
        link_elem = element.find('a')
        if link_elem and link_elem.get('href'):
            product['url'] = link_elem['href']
        
        return product if product else None
    
    def extract_pricing(self, website: str) -> Dict[str, Any]:
        """提取定价信息"""
        pricing_url = f"{website.rstrip('/')}/pricing"
        
        try:
            response = self.session.get(pricing_url, timeout=self.timeout)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            pricing_tiers = []
            
            # 常见的定价选择器
            pricing_selectors = [
                '.pricing-tier', '.plan', '.pricing-card',
                '[class*="pricing"]', '[class*="plan"]'
            ]
            
            for selector in pricing_selectors:
                items = soup.select(selector)
                for item in items:
                    tier = self._extract_pricing_tier(item)
                    if tier:
                        pricing_tiers.append(tier)
            
            return {
                'pricing_tiers': pricing_tiers,
                'source_url': pricing_url,
                'confidence': '中' if pricing_tiers else '低',
                'scraped_at': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"提取定价信息失败: {e}")
            return {
                'error': str(e),
                'source_url': pricing_url,
                'confidence': '低',
                'scraped_at': datetime.now().isoformat()
            }
    
    def _extract_pricing_tier(self, element) -> Optional[Dict[str, str]]:
        """提取单个定价层级"""
        tier = {}
        
        # 层级名称
        name_elem = element.find(['h1', 'h2', 'h3', 'h4', '.title', '.name'])
        if name_elem:
            tier['name'] = name_elem.get_text(strip=True)
        
        # 价格
        price_elem = element.find(['.price', '[class*="price"]'])
        if price_elem:
            tier['price'] = price_elem.get_text(strip=True)
        
        # 功能列表
        features = []
        feature_elems = element.find_all(['li', '.feature'])
        for feat in feature_elems:
            features.append(feat.get_text(strip=True))
        
        if features:
            tier['features'] = features
        
        return tier if tier else None

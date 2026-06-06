"""
数据验证模块
用于验证爬虫数据的完整性和准确性
"""

import logging
from typing import Dict, Any, List
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class DataValidator:
    """数据验证器"""
    
    def __init__(self):
        self.validation_rules = {
            'G1': self._validate_traffic_data,
            'G2': self._validate_product_data,
            'G3': self._validate_social_data,
            'G7': self._validate_ad_data,
        }
    
    def validate(self, dimension: str, data: Dict[str, Any]) -> bool:
        """验证数据
        
        Args:
            dimension: 维度代码
            data: 数据字典
            
        Returns:
            bool: 验证是否通过
        """
        # 基础验证
        if not data or not isinstance(data, dict):
            logger.warning(f"{dimension}: 数据为空或格式错误")
            return False
        
        # 检查是否包含错误
        if 'error' in data:
            logger.warning(f"{dimension}: 数据包含错误: {data['error']}")
            return False
        
        # 维度特定验证
        validator = self.validation_rules.get(dimension)
        if validator:
            return validator(data)
        
        return True
    
    def cross_validate(self, dimension: str, data: Dict[str, Any], 
                      website: str = None) -> Dict[str, Any]:
        """交叉验证
        
        Args:
            dimension: 维度代码
            data: 数据字典
            website: 网站域名
            
        Returns:
            Dict: 验证结果
        """
        result = {
            'passed': True,
            'warnings': [],
            'checks': []
        }
        
        # 检查数据时效性
        scraped_at = data.get('scraped_at', '')
        if scraped_at:
            try:
                scrape_time = datetime.fromisoformat(scraped_at.replace('Z', '+00:00'))
                age = datetime.now() - scrape_time
                if age > timedelta(days=7):
                    result['warnings'].append(f'数据超过7天，可能已过期')
                    result['checks'].append({'check': '时效性', 'status': '警告'})
                else:
                    result['checks'].append({'check': '时效性', 'status': '通过'})
            except:
                result['checks'].append({'check': '时效性', 'status': '未知'})
        
        # 检查置信度
        confidence = data.get('confidence', '中')
        if confidence == '低':
            result['warnings'].append('数据置信度低，建议二次验证')
            result['checks'].append({'check': '置信度', 'status': '警告'})
        else:
            result['checks'].append({'check': '置信度', 'status': '通过'})
        
        # 检查关键字段
        if 'source_url' not in data:
            result['warnings'].append('缺少数据来源URL')
            result['checks'].append({'check': '数据来源', 'status': '警告'})
        else:
            result['checks'].append({'check': '数据来源', 'status': '通过'})
        
        if result['warnings']:
            result['passed'] = False
        
        return result
    
    def _validate_traffic_data(self, data: Dict[str, Any]) -> bool:
        """验证流量数据"""
        required_fields = ['total_visits', 'traffic_sources']
        for field in required_fields:
            if field not in data:
                logger.warning(f"G1: 缺少必要字段 {field}")
                return False
        return True
    
    def _validate_product_data(self, data: Dict[str, Any]) -> bool:
        """验证产品数据"""
        if 'products' not in data:
            logger.warning("G2: 缺少产品列表")
            return False
        return True
    
    def _validate_social_data(self, data: Dict[str, Any]) -> bool:
        """验证社媒数据"""
        if 'social_data' not in data:
            logger.warning("G3: 缺少社媒数据")
            return False
        return True
    
    def _validate_ad_data(self, data: Dict[str, Any]) -> bool:
        """验证广告数据"""
        if 'ads' not in data:
            logger.warning("G7: 缺少广告列表")
            return False
        return True

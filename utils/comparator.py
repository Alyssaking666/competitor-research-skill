"""
数据对比模块
用于对比不同时间点的数据，识别变化
"""

import json
import hashlib
import logging
from typing import Dict, Any, List, Tuple
from datetime import datetime

logger = logging.getLogger(__name__)

class DataComparator:
    """数据对比器"""
    
    def __init__(self):
        pass
    
    def compare_data(self, old_data: Dict[str, Any], 
                    new_data: Dict[str, Any]) -> Dict[str, Any]:
        """对比两份数据，识别变化
        
        Args:
            old_data: 旧数据
            new_data: 新数据
            
        Returns:
            Dict: 变化结果
        """
        changes = {
            'added': [],
            'removed': [],
            'modified': [],
            'unchanged': [],
            'summary': ''
        }
        
        # 对比所有键
        all_keys = set(old_data.keys()) | set(new_data.keys())
        
        for key in all_keys:
            if key not in old_data:
                changes['added'].append({
                    'field': key,
                    'new_value': new_data[key]
                })
            elif key not in new_data:
                changes['removed'].append({
                    'field': key,
                    'old_value': old_data[key]
                })
            elif old_data[key] != new_data[key]:
                changes['modified'].append({
                    'field': key,
                    'old_value': old_data[key],
                    'new_value': new_data[key]
                })
            else:
                changes['unchanged'].append(key)
        
        # 生成摘要
        total_changes = len(changes['added']) + len(changes['removed']) + len(changes['modified'])
        if total_changes == 0:
            changes['summary'] = '无变化'
        else:
            changes['summary'] = f"共 {total_changes} 处变化: "
            if changes['added']:
                changes['summary'] += f"新增 {len(changes['added'])} 项, "
            if changes['removed']:
                changes['summary'] += f"删除 {len(changes['removed'])} 项, "
            if changes['modified']:
                changes['summary'] += f"修改 {len(changes['modified'])} 项"
        
        return changes
    
    def compute_hash(self, data: Dict[str, Any]) -> str:
        """计算数据指纹
        
        Args:
            data: 数据字典
            
        Returns:
            str: MD5哈希值
        """
        data_str = json.dumps(data, sort_keys=True, ensure_ascii=False)
        return hashlib.md5(data_str.encode('utf-8')).hexdigest()
    
    def has_changed(self, old_hash: str, new_data: Dict[str, Any]) -> bool:
        """检查数据是否变化
        
        Args:
            old_hash: 旧数据哈希
            new_data: 新数据
            
        Returns:
            bool: 是否变化
        """
        new_hash = self.compute_hash(new_data)
        return old_hash != new_hash

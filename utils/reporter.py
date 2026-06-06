"""
报告生成模块
用于生成Markdown格式的调研报告
"""

import json
import logging
from typing import Dict, Any, List
from datetime import datetime

logger = logging.getLogger(__name__)

class ReportGenerator:
    """报告生成器"""
    
    def __init__(self):
        self.dimension_names = {
            'G1': '流量起量分析', 'G2': '品牌新品动向', 'G3': '社媒数据分析',
            'G4': '红人合作分析', 'G5': 'UGC舆情分析', 'G6': 'PR稿件分析',
            'G7': '广告投放分析', 'S1': '功能对比分析', 'S2': '技术维度分析',
            'S3': '用户体验分析', 'S4': '商业模式分析', 'S5': '生态集成分析',
            'S6': '发展历程分析', 'B1': '产品矩阵分析', 'B2': '渠道布局分析',
            'B3': '品牌定位分析', 'B4': '供应链分析'
        }
    
    def generate(self, data: Dict[str, Any], competitor_name: str,
                dimensions: List[str], level: str) -> str:
        """生成报告
        
        Args:
            data: 调研数据
            competitor_name: 竞品名称
            dimensions: 维度列表
            level: 调研级别
            
        Returns:
            str: Markdown格式报告
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        report = f"""# {competitor_name} 竞品调研报告

> **生成时间**: {timestamp}
> **调研级别**: {level}
> **分析维度**: {', '.join(dimensions)}
> **数据来源**: Python爬虫抓取
> **成本**: $0

---

## 执行摘要

### 调研概况
- **目标竞品**: {competitor_name}
- **调研维度数**: {len(dimensions)}
- **数据完整度**: {self._compute_completeness(data, dimensions)}

### 核心发现
（此处需要根据实际数据人工填写）

---

## 详细分析

"""
        
        # 按维度输出详细分析
        for dimension in dimensions:
            report += self._generate_dimension_section(dimension, data.get(dimension))
        
        report += """## 数据来源与验证

### 数据来源
- 全部数据通过Python爬虫从公开渠道获取
- 主要来源: 官网、社媒平台、广告库、论坛等

### 验证方式
- 多源交叉验证
- 数据时效性检查
- 置信度评级

### 数据局限
- 爬虫可能受反爬机制影响
- 部分数据需要手动补充
- 实时性不如付费API

---

## 附录

### 原始数据 (JSON)

```json
"""
        
        # 添加原始JSON数据
        raw_data = {dim: info['data'] if info else {} for dim, info in data.items()}
        report += json.dumps(raw_data, ensure_ascii=False, indent=2)
        
        report += """
```

---

*本报告由竞品调研工具自动生成，建议结合人工分析使用*
"""
        
        return report
    
    def _generate_dimension_section(self, dimension: str, 
                                   data: Dict[str, Any]) -> str:
        """生成单个维度的分析章节"""
        dim_name = self.dimension_names.get(dimension, dimension)
        section = f"### {dimension} {dim_name}\n\n"
        
        if not data:
            section += "❌ 未获取到数据\n\n"
            return section
        
        dim_data = data.get('data', {})
        section += f"**数据时间**: {data.get('created_at', '未知')}\n\n"
        section += f"**置信度**: {dim_data.get('confidence', '中')}\n\n"
        
        if 'error' in dim_data:
            section += f"⚠️ **数据获取失败**: {dim_data['error']}\n\n"
        else:
            section += "**关键数据**:\n\n"
            for key, value in dim_data.items():
                if key not in ['confidence', 'source_url', 'scraped_at', 'cleaned_at', 'dimension']:
                    section += f"- {key}: {value}\n"
        
        if 'source_url' in dim_data:
            section += f"\n**数据来源**: {dim_data['source_url']}\n"
        
        section += "\n---\n\n"
        return section
    
    def _compute_completeness(self, data: Dict[str, Any], 
                             dimensions: List[str]) -> str:
        """计算数据完整度"""
        if not dimensions:
            return "0/0"
        
        valid_count = 0
        for dim in dimensions:
            if dim in data and data[dim] and 'error' not in data[dim].get('data', {}):
                valid_count += 1
        
        return f"{valid_count}/{len(dimensions)}"

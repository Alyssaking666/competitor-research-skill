"""
Reddit爬虫模块
用于抓取UGC舆情数据
"""

import requests
import json
import logging
from typing import Dict, List, Any
from datetime import datetime

logger = logging.getLogger(__name__)

class RedditScraper:
    """Reddit爬虫 - 自用版"""
    
    def __init__(self):
        self.base_url = "https://www.reddit.com"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def search_brand_mentions(self, brand_name: str, limit: int = 25) -> Dict[str, Any]:
        """搜索品牌提及
        
        Args:
            brand_name: 品牌名称
            limit: 返回结果数量
            
        Returns:
            Dict: 包含提及列表的字典
        """
        try:
            # 使用Reddit搜索API
            search_url = f"{self.base_url}/search.json"
            params = {
                'q': brand_name,
                'limit': limit,
                'sort': 'new',
                't': 'year'  # 最近一年
            }
            
            response = requests.get(
                search_url, 
                params=params, 
                headers=self.headers,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                mentions = self._parse_reddit_posts(data, brand_name)
                
                return {
                    'mentions': mentions,
                    'total_count': len(mentions),
                    'brand_name': brand_name,
                    'source_url': f'{self.base_url}/search/?q={brand_name}',
                    'confidence': '中',
                    'scraped_at': datetime.now().isoformat()
                }
            else:
                logger.warning(f"Reddit API返回状态码: {response.status_code}")
                return {
                    'mentions': [],
                    'error': f'API返回状态码: {response.status_code}',
                    'source_url': f'{self.base_url}/search/?q={brand_name}',
                    'confidence': '低',
                    'scraped_at': datetime.now().isoformat()
                }
                
        except Exception as e:
            logger.error(f"Reddit搜索失败: {e}")
            return {
                'mentions': [],
                'error': str(e),
                'source_url': f'{self.base_url}/search/?q={brand_name}',
                'confidence': '低',
                'scraped_at': datetime.now().isoformat()
            }
    
    def _parse_reddit_posts(self, data: Dict, brand_name: str) -> List[Dict[str, Any]]:
        """解析Reddit帖子"""
        mentions = []
        
        posts = data.get('data', {}).get('children', [])
        
        for post in posts:
            post_data = post.get('data', {})
            
            mention = {
                'title': post_data.get('title', ''),
                'subreddit': post_data.get('subreddit', ''),
                'author': post_data.get('author', ''),
                'score': post_data.get('score', 0),
                'num_comments': post_data.get('num_comments', 0),
                'created_utc': post_data.get('created_utc', 0),
                'url': f"https://www.reddit.com{post_data.get('permalink', '')}",
                'selftext': post_data.get('selftext', '')[:500]  # 限制长度
            }
            
            mentions.append(mention)
        
        return mentions
    
    def analyze_sentiment(self, mentions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """简单情感分析（基于关键词）"""
        positive_words = ['good', 'great', 'excellent', 'amazing', 'love', 'best', 'recommend']
        negative_words = ['bad', 'terrible', 'awful', 'hate', 'worst', 'problem', 'issue']
        
        sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
        
        for mention in mentions:
            text = (mention.get('title', '') + ' ' + mention.get('selftext', '')).lower()
            
            pos_count = sum(1 for word in positive_words if word in text)
            neg_count = sum(1 for word in negative_words if word in text)
            
            if pos_count > neg_count:
                sentiment_counts['positive'] += 1
            elif neg_count > pos_count:
                sentiment_counts['negative'] += 1
            else:
                sentiment_counts['neutral'] += 1
        
        total = len(mentions)
        if total > 0:
            sentiment_counts['positive_ratio'] = round(sentiment_counts['positive'] / total, 2)
            sentiment_counts['negative_ratio'] = round(sentiment_counts['negative'] / total, 2)
            sentiment_counts['neutral_ratio'] = round(sentiment_counts['neutral'] / total, 2)
        
        return sentiment_counts

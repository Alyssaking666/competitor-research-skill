---
name: "竞品调研洞察"
description: "深度竞品/品类调研与洞察分析。融合横纵分析法、流量起量追踪与全维度月度监测，输出结构化报告与JSON数据。支持自用版（低预算爬虫驱动）和平台版（API服务化）两种模式。Invoke when user needs competitive analysis, market research, competitor tracking, or strategic insights on products/brands/companies."
---

# 竞品调研洞察 SKILL（双模式完整版 v5 - 最终优化版）

## 核心定位

本SKILL不是让AI直接输出报告——那种东西全是公开信息的摘要拼凑，没洞察。而是**让AI按照横纵分析法+流量起量追踪+全维度监测的框架，分步骤搜集、整理原始素材，你来做最后的判断**。

**本版本支持两种服务模式**：
- **自用版**：服务个人/单公司，预算极低，重爬虫，适合定期调研
- **平台版**：服务多公司/多客户，API驱动，标准化输出，适合商业化

---

## 快速导航

| 章节 | 内容 | 适用读者 |
|------|------|----------|
| [执行流程图](#执行流程图) | 一张图看懂整个调研流程 | 所有人 |
| [工具选型决策树](#工具选型决策树) | 根据场景自动推荐工具组合 | 所有人 |
| [模式选择指南](#模式选择指南) | 自用版 vs 平台版详细对比 | 所有人 |
| [调研级别定义](#调研级别定义优化版) | 4个级别的详细说明 | 所有人 |
| [维度执行手册](#第三阶段维度执行手册双模式) | 17个维度的完整执行方案 | 执行者 |
| [爬虫代码库](#核心爬虫代码自用版优化) | 可直接运行的Python代码 | 开发者 |
| [报告模板](#第六阶段输出模板) | 轻度/深度报告模板 | 分析师 |
| [FAQ与故障排除](#第十阶段faq与故障排除) | 常见问题解决方案 | 所有人 |

---

## 执行流程图

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           竞品调研执行流程图                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  开始                                                                       │
│    │                                                                        │
│    ▼                                                                        │
│  ┌─────────────────────┐                                                   │
│  │ Step 1: 选择模式     │                                                   │
│  │ • 自用版 (个人/单公司)│                                                   │
│  │ • 平台版 (多客户/商业化)│                                                  │
│  └─────────────────────┘                                                   │
│    │                                                                        │
│    ▼                                                                        │
│  ┌─────────────────────┐                                                   │
│  │ Step 2: 确定调研类型 │                                                   │
│  │ • 跨境电商/消费品    │                                                   │
│  │ • SaaS/软件产品     │                                                   │
│  │ • 两者都需要        │                                                   │
│  └─────────────────────┘                                                   │
│    │                                                                        │
│    ▼                                                                        │
│  ┌─────────────────────┐                                                   │
│  │ Step 3: 选择调研级别 │                                                   │
│  │ • 增量更新 (30min)  │                                                   │
│  │ • 轻度调研 (1-2h)   │                                                   │
│  │ • 深度调研 (4-8h)   │                                                   │
│  │ • 全面审计 (16-24h) │                                                   │
│  └─────────────────────┘                                                   │
│    │                                                                        │
│    ▼                                                                        │
│  ┌─────────────────────┐                                                   │
│  │ Step 4: 选择分析维度 │                                                   │
│  │ • 通用维度 (G1-G7)  │                                                   │
│  │ • SaaS维度 (S1-S6)  │                                                   │
│  │ • 品牌维度 (B1-B4)  │                                                   │
│  └─────────────────────┘                                                   │
│    │                                                                        │
│    ▼                                                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Step 5: 执行调研 (根据模式选择工具)                                   │   │
│  │                                                                     │   │
│  │  自用版                    平台版                                    │   │
│  │  ┌─────────────┐          ┌─────────────┐                          │   │
│  │  │ 爬虫抓取     │          │ API调用      │                          │   │
│  │  │ (Python)    │          │ (SEMrush等)  │                          │   │
│  │  └──────┬──────┘          └──────┬──────┘                          │   │
│  │         │                        │                                 │   │
│  │         ▼                        ▼                                 │   │
│  │  ┌─────────────┐          ┌─────────────┐                          │   │
│  │  │ 数据存储     │          │ 数据存储     │                          │   │
│  │  │ (SQLite)    │          │ (PostgreSQL)│                          │   │
│  │  └──────┬──────┘          └──────┬──────┘                          │   │
│  │         │                        │                                 │   │
│  │         ▼                        ▼                                 │   │
│  │  ┌─────────────┐          ┌─────────────┐                          │   │
│  │  │ 数据验证     │          │ 数据验证     │                          │   │
│  │  │ (交叉验证)   │          │ (多重验证)   │                          │   │
│  │  └──────┬──────┘          └──────┬──────┘                          │   │
│  └─────────┼────────────────────────┼───────────────────────────────────┘   │
│            │                        │                                       │
│            ▼                        ▼                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Step 6: 生成报告                                                     │   │
│  │ • Markdown格式                                                      │   │
│  │ • JSON原始数据                                                      │   │
│  │ • 可选: PDF (平台版)                                                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│            │                                                                │
│            ▼                                                                │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Step 7: 人工审核与洞察提炼                                           │   │
│  │ • 验证关键数据点                                                     │   │
│  │ • 提炼核心洞察                                                       │   │
│  │ • 形成战略建议                                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│            │                                                                │
│            ▼                                                                │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Step 8: 输出最终报告                                                 │   │
│  │ • 执行摘要                                                          │   │
│  │ • 详细分析                                                          │   │
│  │ • 数据附录                                                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│            │                                                                │
│            ▼                                                                │
│           结束                                                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 工具选型决策树

```
开始选择工具
    │
    ├── 你的预算是？
    │       │
    │       ├── $0-20/月 → 自用版
    │       │       │
    │       │       ├── 需要流量数据？
    │       │       │       ├── 是 → SimilarWeb免费版 + Google Trends
    │       │       │       └── 否 → 跳过
    │       │       │
    │       │       ├── 需要广告数据？
    │       │       │       ├── 是 → Meta Ad Library爬虫
    │       │       │       └── 否 → 跳过
    │       │       │
    │       │       ├── 需要社媒数据？
    │       │       │       ├── 是 → 社媒平台公开数据 + Social Blade
    │       │       │       └── 否 → 跳过
    │       │       │
    │       │       ├── 需要UGC/舆情？
    │       │       │       ├── 是 → Reddit API + Google Search
    │       │       │       └── 否 → 跳过
    │       │       │
    │       │       └── 需要产品功能对比？
    │       │               ├── 是 → 官网爬虫 + 手动体验
    │       │               └── 否 → 跳过
    │       │
    │       └── $100-500/月 → 平台版
    │               │
    │               ├── 需要精准流量数据？
    │               │       ├── 是 → SEMrush API / Ahrefs API
    │               │       └── 否 → SimilarWeb API
    │               │
    │               ├── 需要广告数据？
    │               │       ├── 是 → Meta Ad Library API
    │               │       └── 否 → 跳过
    │               │
    │               ├── 需要社媒数据？
    │               │       ├── 是 → 社媒API + 爬虫补充
    │               │       └── 否 → 跳过
    │               │
    │               ├── 需要批量处理？
    │               │       ├── 是 → Celery + Redis队列
    │               │       └── 否 → 同步处理
    │               │
    │               └── 需要多租户？
    │                       ├── 是 → PostgreSQL + 租户隔离
    │                       └── 否 → 单数据库
    │
    └── 你的技术能力是？
            │
            ├── 基础Python → 自用版（有完整代码示例）
            ├── 后端开发 → 平台版（FastAPI/Node.js）
            └── 无技术背景 → 建议先用平台版或外包开发
```

---

## 模式选择指南

### 模式A：自用版（推荐个人/单公司使用）

**适用场景**：
- 你是产品经理/运营/市场，需要定期调研竞品
- 公司计划切入新品类，需要快速评估
- 预算有限，希望用技术能力替代付费工具

**核心特点**：
- **预算极低**：$0-20/月（主要是API超额费用）
- **重爬虫**：80%数据通过Python爬虫获取
- **可定期执行**：配置一次，每月自动跑一遍
- **增量更新**：只更新变化的部分，节省时间和成本

**技术要求**：
- 基础Python能力
- 能配置定时任务（crontab/Windows任务计划）
- 能管理简单的数据库（SQLite即可）

---

### 模式B：平台版（推荐服务化/商业化使用）

**适用场景**：
- 你是咨询顾问/服务商，为多个客户提供调研服务
- 公司内部有多个团队需要调研支持
- 希望标准化、规模化输出报告

**核心特点**：
- **API驱动**：接入SEMrush、Ahrefs、SimilarWeb等API
- **多租户隔离**：不同客户数据独立存储
- **批量处理**：一次可处理多个竞品/多个维度
- **标准化输出**：统一报告模板，品牌可定制

**技术要求**：
- 后端开发能力（Node.js/Python）
- 数据库设计（PostgreSQL/MongoDB）
- API集成和权限管理

---

## 两种模式对比

| 对比项 | 自用版 | 平台版 |
|--------|--------|--------|
| **月预算** | $0-20 | $100-500 |
| **核心工具** | Python爬虫 | API + 爬虫 |
| **数据获取** | 80%爬虫 + 20%手动 | 80%API + 20%爬虫 |
| **执行方式** | 本地脚本/定时任务 | 服务端部署/队列处理 |
| **存储方式** | SQLite/本地文件 | PostgreSQL/MongoDB |
| **输出格式** | Markdown + JSON | Markdown + JSON + PDF |
| **可扩展性** | 单用户 | 多租户 |
| **维护成本** | 低（个人维护） | 中（需运维） |
| **适用人群** | 产品经理、运营、创业者 | 咨询顾问、服务商、中大型企业 |

---

## 调研级别定义（优化版）

### 级别1：增量更新（新增）

**适用场景**：已做过完整调研，只需更新变化部分
**时间成本**：30分钟-1小时
**工具成本**：$0
**输出规模**：1000-2000字（变更摘要）
**推荐维度**：G2,G3,G7（变化最快的维度）

**执行策略**：
- 对比上次调研结果，只抓取变化部分
- 使用爬虫快速扫描官网/社媒/广告库
- 输出变更摘要，标注"新增/变化/消失"

---

### 级别2：轻度调研（优化）

**适用场景**：快速了解竞品现状，日常监测
**时间成本**：1-2小时
**工具成本**：$0
**输出规模**：3000-5000字
**推荐维度**：3-4个核心维度

**自用版执行策略**：
- 全部使用爬虫获取数据
- 手动验证关键数据点
- 输出简化版报告

**平台版执行策略**：
- 使用免费API获取基础数据
- 爬虫补充免费API覆盖不到的部分
- 自动化生成报告

---

### 级别3：深度调研（优化）

**适用场景**：战略决策、季度评审、融资准备
**时间成本**：4-8小时
**工具成本**：自用版$0-20，平台版$100-300
**输出规模**：10000-15000字
**推荐维度**：6-10个维度

**自用版执行策略**：
- 爬虫获取80%数据
- 手动补充关键验证（如亲自体验产品）
- 人工分析+AI辅助生成洞察

**平台版执行策略**：
- API获取精准数据（流量、关键词、广告）
- 爬虫补充UGC、PR等定性数据
- 自动化分析+人工审核

---

### 级别4：全面审计（平台版专属）

**适用场景**：重要客户、IPO准备、并购尽调
**时间成本**：16-24小时
**工具成本**：$300-500
**输出规模**：20000-30000字
**推荐维度**：全部17个维度

**执行策略**：
- 全API+全爬虫覆盖
- 多数据源交叉验证
- 专家人工审核
- 定制化报告+演示PPT

---

## 预算对照表（双模式）

### 自用版预算

| 调研级别 | 月预算 | 时间成本 | 主要支出 | 适用频率 |
|---------|--------|---------|---------|---------|
| 增量更新 | $0 | 30min-1h | 无 | 每周/每月 |
| 轻度调研 | $0 | 1-2h | 无 | 每月 |
| 深度调研 | $0-20 | 4-8h | API超额费用 | 每季度 |

**省钱技巧（自用版）**：
1. **爬虫替代API**：用Selenium/Playwright模拟浏览器抓取SimilarWeb免费版数据
2. **缓存机制**：抓取的数据本地缓存，下次只更新变化部分
3. **定时任务**：用crontab设置每月1号自动执行增量更新
4. **免费额度最大化**：Google Custom Search 100次/天，Reddit API 60次/分钟

---

### 平台版预算

| 调研级别 | 月预算 | 时间成本 | 主要支出 | 适用频率 |
|---------|--------|---------|---------|---------|
| 轻度调研 | $0-50 | 30min（人工审核） | Google API + 服务器 | 按需 |
| 深度调研 | $100-300 | 1-2h（人工审核） | SEMrush + 服务器 | 按需 |
| 全面审计 | $300-500 | 4-8h（专家审核） | 全工具订阅 + 人工 | 按项目 |

**收费建议（平台版）**：
- 轻度调研：$200-500/份
- 深度调研：$1000-3000/份
- 全面审计：$5000-10000/份
- 月度监测服务：$500-2000/月（含4次增量更新+1次轻度调研）

---

## 第一阶段：研究启动

### Step 1：选择服务模式

**你选择哪种模式？**
- **A. 自用版**：服务我个人/我公司，预算极低，重爬虫
- **B. 平台版**：服务多个客户，API驱动，标准化输出

---

### Step 2：确定研究类型与竞品

1. **你要研究什么类型？**
   - 1️⃣ 跨境电商/消费品品牌
   - 2️⃣ SaaS/软件产品
   - 3️⃣ 两者都需要

2. **你要研究哪些竞品？**
   - 竞品A：__________
   - 竞品B：__________
   - 竞品C：__________（可选）

3. **选择调研级别**：
   - **增量更新**：只更新变化部分（30分钟）
   - **轻度调研**：快速扫描（1-2小时）
   - **深度调研**：全面分析（4-8小时）
   - **全面审计**（仅平台版）：深度尽调（16-24小时）

---

### Step 3：选择分析维度

根据模式和调研级别，选择维度：

#### 【通用维度】

| 维度 | 增量更新 | 轻度 | 深度 | 自用版工具 | 平台版工具 |
|------|---------|------|------|-----------|-----------|
| G1 流量起量 | ❌ | ✅ | ✅ | SimilarWeb免费+爬虫 | SEMrush API |
| G2 品牌新品 | ✅ | ✅ | ✅ | 官网爬虫 | 官网爬虫+新闻API |
| G3 社媒数据 | ✅ | ✅ | ✅ | 社媒爬虫 | 社媒API+爬虫 |
| G4 红人合作 | ❌ | ✅ | ✅ | Instagram爬虫 | 社媒API |
| G5 UGC舆情 | ❌ | ✅ | ✅ | Reddit爬虫 | Reddit API |
| G6 PR稿件 | ❌ | ✅ | ✅ | Google Search爬虫 | Google Custom Search API |
| G7 广告投放 | ✅ | ✅ | ✅ | Meta Ad Library爬虫 | Meta Ad Library API |

#### 【SaaS/软件专属】

| 维度 | 增量更新 | 轻度 | 深度 | 自用版工具 | 平台版工具 |
|------|---------|------|------|-----------|-----------|
| S1 功能对比 | ❌ | ✅ | ✅ | 官网爬虫 | 官网爬虫+G2 API |
| S2 技术维度 | ❌ | ❌ | ✅ | BuiltWith | BuiltWith API |
| S3 用户体验 | ❌ | ✅ | ✅ | 官网爬虫+Reddit | G2 API+爬虫 |
| S4 商业模式 | ❌ | ✅ | ✅ | 官网爬虫 | 官网爬虫 |
| S5 生态集成 | ❌ | ❌ | ✅ | 官网爬虫 | 官网爬虫 |
| S6 发展历程 | ❌ | ✅ | ✅ | Crunchbase爬虫 | Crunchbase API |

#### 【品牌/消费品专属】

| 维度 | 增量更新 | 轻度 | 深度 | 自用版工具 | 平台版工具 |
|------|---------|------|------|-----------|-----------|
| B1 产品矩阵 | ✅ | ✅ | ✅ | 官网爬虫 | 官网爬虫 |
| B2 渠道布局 | ❌ | ✅ | ✅ | 官网爬虫+SimilarWeb | SimilarWeb API |
| B3 品牌定位 | ❌ | ✅ | ✅ | 官网爬虫 | 官网爬虫 |
| B4 供应链 | ❌ | ❌ | ✅ | 官网爬虫 | 官网爬虫 |

---

## 第二阶段：模式专属执行方案

### 模式A：自用版执行方案

#### 核心原则
- **能爬就不买**：优先用爬虫获取数据
- **能缓存就不重复**：建立本地数据库，增量更新
- **能自动化就不手动**：定时任务+脚本化

#### 技术栈

| 层级 | 技术 | 成本 | 用途 |
|------|------|------|------|
| 爬虫框架 | Python + Scrapy/Playwright | 免费 | 网页抓取 |
| 数据存储 | SQLite | 免费 | 本地数据存储 |
| 定时任务 | crontab/Windows任务计划 | 免费 | 自动执行 |
| 数据分析 | Pandas + Jupyter | 免费 | 数据处理 |
| 报告生成 | Python-Markdown | 免费 | 报告生成 |
| 版本控制 | Git | 免费 | 代码管理 |

#### 项目结构

```
competitor-research/
├── config/
│   ├── competitors.json          # 竞品配置
│   ├── dimensions.json           # 维度配置
│   └── settings.json             # 全局设置
├── scrapers/
│   ├── meta_ad_library.py        # Meta广告爬虫
│   ├── reddit_scraper.py         # Reddit爬虫
│   ├── web_scraper.py            # 通用网页爬虫
│   ├── similarweb_scraper.py     # SimilarWeb免费版爬虫
│   └── social_media_scraper.py   # 社媒爬虫
├── storage/
│   ├── database.sqlite           # SQLite数据库
│   └── cache/                    # 缓存文件
├── reports/
│   ├── templates/                # 报告模板
│   └── output/                   # 输出目录
├── scheduler/
│   └── cron_jobs.py              # 定时任务
├── utils/
│   ├── validator.py              # 数据验证
│   ├── comparator.py             # 数据对比
│   └── reporter.py               # 报告生成
└── main.py                       # 主入口
```

#### 环境配置指南

**1. 安装Python依赖**

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows

# 安装依赖
pip install requests beautifulsoup4 pandas schedule selenium playwright lxml
```

**2. 配置config/settings.json**

```json
{
  "mode": "self_use",
  "database": {
    "path": "storage/database.sqlite"
  },
  "scrapers": {
    "request_delay": 2,
    "max_retries": 3,
    "timeout": 10
  },
  "report": {
    "output_dir": "reports/output",
    "template_dir": "reports/templates"
  },
  "schedule": {
    "incremental_frequency": "weekly",
    "light_frequency": "monthly",
    "deep_frequency": "quarterly"
  }
}
```

**3. 配置config/competitors.json**

```json
{
  "competitors": [
    {
      "name": "HubSpot",
      "website": "https://www.hubspot.com",
      "industry": "saas",
      "social_accounts": {
        "twitter": "hubspot",
        "linkedin": "hubspot",
        "instagram": "hubspot"
      }
    }
  ]
}
```

#### 核心爬虫代码（自用版优化）

```python
# main.py - 自用版主入口（增强版）
import json
import sqlite3
import hashlib
import time
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/research.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class CompetitorResearchTool:
    """自用版竞品调研工具 - 增强版"""
    
    def __init__(self, config_path='config/settings.json'):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            logger.error(f"配置文件未找到: {config_path}")
            raise
        except json.JSONDecodeError:
            logger.error(f"配置文件格式错误: {config_path}")
            raise
        
        # 确保日志目录存在
        import os
        os.makedirs('logs', exist_ok=True)
        os.makedirs('reports/output', exist_ok=True)
        os.makedirs('storage/cache', exist_ok=True)
        
        self.db = sqlite3.connect(self.config['database']['path'])
        self.db.row_factory = sqlite3.Row
        
        self._init_database()
        logger.info("竞品调研工具初始化完成")
    
    def _init_database(self):
        """初始化数据库"""
        cursor = self.db.cursor()
        
        # 竞品基础信息表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS competitors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                website TEXT,
                industry TEXT,
                social_accounts TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # 调研数据表（按维度存储）
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS research_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                competitor_id INTEGER NOT NULL,
                dimension TEXT NOT NULL,
                data TEXT,
                source_url TEXT,
                confidence TEXT DEFAULT '中',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (competitor_id) REFERENCES competitors(id)
            )
        ''')
        
        # 历史数据表（用于增量更新）
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS data_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                competitor_id INTEGER NOT NULL,
                dimension TEXT NOT NULL,
                data_hash TEXT NOT NULL,
                change_summary TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (competitor_id) REFERENCES competitors(id)
            )
        ''')
        
        # 执行日志表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS execution_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                competitor_id INTEGER,
                dimension TEXT,
                level TEXT,
                status TEXT,
                message TEXT,
                execution_time REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        self.db.commit()
        logger.info("数据库初始化完成")
    
    def add_competitor(self, name: str, website: str, industry: str, 
                       social_accounts: Dict[str, str] = None):
        """添加竞品"""
        cursor = self.db.cursor()
        try:
            cursor.execute('''
                INSERT OR REPLACE INTO competitors (name, website, industry, social_accounts)
                VALUES (?, ?, ?, ?)
            ''', (name, website, industry, json.dumps(social_accounts or {})))
            self.db.commit()
            logger.info(f"已添加/更新竞品: {name}")
        except sqlite3.Error as e:
            logger.error(f"添加竞品失败: {e}")
            raise
    
    def run_research(self, competitor_name: str, dimensions: List[str], 
                     level: str = '轻度') -> str:
        """执行调研
        
        Args:
            competitor_name: 竞品名称
            dimensions: 维度列表，如['G2', 'G3', 'G7']
            level: 调研级别（增量更新/轻度/深度）
            
        Returns:
            str: 生成的报告文件路径
        """
        start_time = time.time()
        logger.info(f"\n{'='*60}")
        logger.info(f"开始调研: {competitor_name}")
        logger.info(f"调研级别: {level}")
        logger.info(f"调研维度: {', '.join(dimensions)}")
        logger.info(f"{'='*60}\n")
        
        try:
            # 获取竞品信息
            cursor = self.db.cursor()
            cursor.execute('SELECT * FROM competitors WHERE name = ?', (competitor_name,))
            competitor = cursor.fetchone()
            
            if not competitor:
                error_msg = f"错误: 未找到竞品 {competitor_name}"
                logger.error(error_msg)
                self._log_execution(None, None, level, 'failed', error_msg, 0)
                raise ValueError(error_msg)
            
            competitor_id = competitor['id']
            website = competitor['website']
            
            # 根据级别决定执行策略
            if level == '增量更新':
                self._run_incremental_update(competitor_id, competitor_name, website, dimensions)
            elif level == '轻度':
                self._run_light_research(competitor_id, competitor_name, website, dimensions)
            elif level == '深度':
                self._run_deep_research(competitor_id, competitor_name, website, dimensions)
            else:
                error_msg = f"未知的调研级别: {level}"
                logger.error(error_msg)
                raise ValueError(error_msg)
            
            # 生成报告
            report_path = self._generate_report(competitor_id, competitor_name, dimensions, level)
            
            execution_time = time.time() - start_time
            self._log_execution(competitor_id, None, level, 'success', 
                              f'报告已生成: {report_path}', execution_time)
            
            logger.info(f"\n{'='*60}")
            logger.info(f"调研完成！耗时: {execution_time:.2f}秒")
            logger.info(f"报告路径: {report_path}")
            logger.info(f"{'='*60}\n")
            
            return report_path
            
        except Exception as e:
            execution_time = time.time() - start_time
            self._log_execution(None, None, level, 'failed', str(e), execution_time)
            logger.error(f"调研失败: {e}")
            raise
    
    def _run_incremental_update(self, competitor_id: int, name: str, 
                                website: str, dimensions: List[str]):
        """增量更新 - 只抓取变化部分"""
        logger.info("执行增量更新...")
        
        for dimension in dimensions:
            logger.info(f"\n检查维度: {dimension}")
            
            try:
                # 获取上次数据
                cursor = self.db.cursor()
                cursor.execute('''
                    SELECT data_hash, change_summary FROM data_history
                    WHERE competitor_id = ? AND dimension = ?
                    ORDER BY created_at DESC LIMIT 1
                ''', (competitor_id, dimension))
                
                last_record = cursor.fetchone()
                
                # 抓取新数据
                new_data = self._scrape_dimension(dimension, website)
                new_hash = self._compute_hash(json.dumps(new_data, sort_keys=True, ensure_ascii=False))
                
                if last_record and last_record['data_hash'] == new_hash:
                    logger.info(f"  ✓ {dimension} 无变化，跳过")
                    self._log_execution(competitor_id, dimension, '增量更新', 'skipped', '无变化', 0)
                    continue
                
                # 计算具体变化
                changes = []
                if last_record:
                    cursor.execute('''
                        SELECT data FROM research_data
                        WHERE competitor_id = ? AND dimension = ?
                        ORDER BY created_at DESC LIMIT 1
                    ''', (competitor_id, dimension))
                    last_data_record = cursor.fetchone()
                    if last_data_record:
                        last_data = json.loads(last_data_record['data'])
                        changes = self._compute_changes(last_data, new_data)
                else:
                    changes = ['首次抓取']
                
                change_summary = '; '.join(changes) if changes else '数据更新'
                logger.info(f"  ✓ {dimension} 有变化: {change_summary}")
                
                # 存储新数据
                cursor.execute('''
                    INSERT INTO research_data (competitor_id, dimension, data, source_url, confidence)
                    VALUES (?, ?, ?, ?, ?)
                ''', (competitor_id, dimension, 
                      json.dumps(new_data, ensure_ascii=False),
                      new_data.get('source_url', ''),
                      new_data.get('confidence', '中')))
                
                cursor.execute('''
                    INSERT INTO data_history (competitor_id, dimension, data_hash, change_summary)
                    VALUES (?, ?, ?, ?)
                ''', (competitor_id, dimension, new_hash, change_summary))
                
                self.db.commit()
                self._log_execution(competitor_id, dimension, '增量更新', 'success', 
                                  change_summary, 0)
                
            except Exception as e:
                logger.error(f"  ✗ {dimension} 更新失败: {e}")
                self._log_execution(competitor_id, dimension, '增量更新', 'failed', str(e), 0)
    
    def _run_light_research(self, competitor_id: int, name: str, 
                           website: str, dimensions: List[str]):
        """轻度调研"""
        logger.info("执行轻度调研...")
        
        for dimension in dimensions:
            logger.info(f"\n调研维度: {dimension}")
            
            try:
                # 抓取数据
                data = self._scrape_dimension(dimension, website)
                
                # 数据清洗和验证
                cleaned_data = self._clean_data(dimension, data)
                
                if self._validate_data(dimension, cleaned_data):
                    logger.info(f"  ✓ {dimension} 数据验证通过")
                    
                    # 存储数据
                    cursor = self.db.cursor()
                    cursor.execute('''
                        INSERT INTO research_data (competitor_id, dimension, data, source_url, confidence)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (competitor_id, dimension,
                          json.dumps(cleaned_data, ensure_ascii=False),
                          cleaned_data.get('source_url', ''),
                          cleaned_data.get('confidence', '中')))
                    
                    # 计算并存储hash
                    data_hash = self._compute_hash(json.dumps(cleaned_data, sort_keys=True, ensure_ascii=False))
                    cursor.execute('''
                        INSERT INTO data_history (competitor_id, dimension, data_hash, change_summary)
                        VALUES (?, ?, ?, ?)
                    ''', (competitor_id, dimension, data_hash, '轻度调研'))
                    
                    self.db.commit()
                    self._log_execution(competitor_id, dimension, '轻度', 'success', '数据已存储', 0)
                else:
                    logger.warning(f"  ⚠ {dimension} 数据验证失败，标记为暂缺")
                    self._log_execution(competitor_id, dimension, '轻度', 'warning', '数据验证失败', 0)
                    
            except Exception as e:
                logger.error(f"  ✗ {dimension} 调研失败: {e}")
                self._log_execution(competitor_id, dimension, '轻度', 'failed', str(e), 0)
    
    def _run_deep_research(self, competitor_id: int, name: str, 
                          website: str, dimensions: List[str]):
        """深度调研"""
        logger.info("执行深度调研...")
        
        # 先执行轻度调研
        self._run_light_research(competitor_id, name, website, dimensions)
        
        # 额外验证和交叉验证
        logger.info("\n执行交叉验证...")
        for dimension in dimensions:
            logger.info(f"\n验证维度: {dimension}")
            
            try:
                # 获取已抓取数据
                cursor = self.db.cursor()
                cursor.execute('''
                    SELECT data FROM research_data
                    WHERE competitor_id = ? AND dimension = ?
                    ORDER BY created_at DESC LIMIT 1
                ''', (competitor_id, dimension))
                
                record = cursor.fetchone()
                if record:
                    data = json.loads(record['data'])
                    
                    # 交叉验证
                    validation_result = self._cross_validate(dimension, data, website)
                    
                    if validation_result['passed']:
                        logger.info(f"  ✓ {dimension} 交叉验证通过")
                        self._log_execution(competitor_id, dimension, '深度', 'success', 
                                          '交叉验证通过', 0)
                    else:
                        logger.warning(f"  ⚠ {dimension} 交叉验证警告: {validation_result['warnings']}")
                        self._log_execution(competitor_id, dimension, '深度', 'warning', 
                                          f"交叉验证警告: {validation_result['warnings']}", 0)
                        
            except Exception as e:
                logger.error(f"  ✗ {dimension} 验证失败: {e}")
                self._log_execution(competitor_id, dimension, '深度', 'failed', str(e), 0)
    
    def _scrape_dimension(self, dimension: str, website: str) -> Dict[str, Any]:
        """根据维度选择爬虫抓取数据"""
        scrapers = {
            'G1': self._scrape_traffic,
            'G2': self._scrape_products,
            'G3': self._scrape_social,
            'G4': self._scrape_influencers,
            'G5': self._scrape_ugc,
            'G6': self._scrape_pr,
            'G7': self._scrape_ads,
            'S1': self._scrape_features,
            'S2': self._scrape_tech,
            'S3': self._scrape_ux,
            'S4': self._scrape_pricing,
            'S5': self._scrape_ecosystem,
            'S6': self._scrape_history,
            'B1': self._scrape_product_matrix,
            'B2': self._scrape_channels,
            'B3': self._scrape_branding,
            'B4': self._scrape_supply_chain
        }
        
        scraper = scrapers.get(dimension)
        if scraper:
            try:
                return scraper(website)
            except Exception as e:
                logger.error(f"爬虫执行失败 {dimension}: {e}")
                return {'error': str(e), 'dimension': dimension, 'confidence': '低'}
        else:
            return {'error': f'未知维度: {dimension}', 'confidence': '低'}
    
    def _scrape_traffic(self, website: str) -> Dict[str, Any]:
        """抓取流量数据（SimilarWeb免费版）"""
        try:
            from scrapers.similarweb_scraper import SimilarWebScraper
            scraper = SimilarWebScraper()
            return scraper.get_traffic_summary(website)
        except ImportError:
            logger.warning("SimilarWeb爬虫未找到，使用备用方案")
            return self._scrape_traffic_fallback(website)
    
    def _scrape_traffic_fallback(self, website: str) -> Dict[str, Any]:
        """流量数据备用方案"""
        return {
            'total_visits': '需要手动查询',
            'bounce_rate': '需要手动查询',
            'pages_per_visit': '需要手动查询',
            'avg_visit_duration': '需要手动查询',
            'traffic_sources': {},
            'top_countries': [],
            'source_url': f'https://www.similarweb.com/website/{website}',
            'confidence': '低',
            'note': 'SimilarWeb爬虫需要维护，建议手动访问上述链接获取数据',
            'scraped_at': datetime.now().isoformat()
        }
    
    def _scrape_products(self, website: str) -> Dict[str, Any]:
        """抓取产品信息"""
        try:
            from scrapers.web_scraper import WebScraper
            scraper = WebScraper()
            return scraper.extract_products(website)
        except ImportError:
            return {
                'products': [],
                'source_url': website,
                'confidence': '低',
                'note': '产品爬虫需要维护',
                'scraped_at': datetime.now().isoformat()
            }
    
    def _scrape_social(self, website: str) -> Dict[str, Any]:
        """抓取社媒数据"""
        try:
            from scrapers.social_media_scraper import SocialMediaScraper
            scraper = SocialMediaScraper()
            return scraper.get_social_summary(website)
        except ImportError:
            return {
                'social_data': {},
                'source_url': website,
                'confidence': '低',
                'note': '社媒爬虫需要维护',
                'scraped_at': datetime.now().isoformat()
            }
    
    def _scrape_ugc(self, website: str) -> Dict[str, Any]:
        """抓取UGC数据"""
        try:
            from scrapers.reddit_scraper import RedditScraper
            brand_name = website.replace('https://', '').replace('http://', '').split('.')[0]
            scraper = RedditScraper()
            return scraper.search_brand_mentions(brand_name)
        except ImportError:
            return {
                'mentions': [],
                'source_url': f'https://www.reddit.com/search/?q={website}',
                'confidence': '低',
                'note': 'Reddit爬虫需要维护',
                'scraped_at': datetime.now().isoformat()
            }
    
    def _scrape_ads(self, website: str) -> Dict[str, Any]:
        """抓取广告数据"""
        try:
            from scrapers.meta_ad_scraper import MetaAdScraper
            brand_name = website.replace('https://', '').replace('http://', '').split('.')[0]
            scraper = MetaAdScraper()
            return scraper.search_ads(brand_name)
        except ImportError:
            return {
                'ads': [],
                'source_url': f'https://www.facebook.com/ads/library/?q={website}',
                'confidence': '低',
                'note': 'Meta Ad爬虫需要维护',
                'scraped_at': datetime.now().isoformat()
            }
    
    def _scrape_features(self, website: str) -> Dict[str, Any]:
        """抓取功能信息（SaaS）"""
        return {
            'features': [],
            'source_url': f'{website}/features',
            'confidence': '低',
            'note': '功能对比需要手动整理',
            'scraped_at': datetime.now().isoformat()
        }
    
    def _scrape_pricing(self, website: str) -> Dict[str, Any]:
        """抓取定价信息（SaaS）"""
        return {
            'pricing_tiers': [],
            'source_url': f'{website}/pricing',
            'confidence': '低',
            'note': '定价信息需要手动整理',
            'scraped_at': datetime.now().isoformat()
        }
    
    def _scrape_product_matrix(self, website: str) -> Dict[str, Any]:
        """抓取产品矩阵（品牌）"""
        return {
            'products': [],
            'source_url': website,
            'confidence': '低',
            'note': '产品矩阵需要手动整理',
            'scraped_at': datetime.now().isoformat()
        }
    
    def _scrape_channels(self, website: str) -> Dict[str, Any]:
        """抓取渠道布局（品牌）"""
        return {
            'channels': [],
            'source_url': website,
            'confidence': '低',
            'note': '渠道信息需要手动整理',
            'scraped_at': datetime.now().isoformat()
        }
    
    # 其他维度的占位方法
    def _scrape_influencers(self, website: str) -> Dict[str, Any]:
        return {'note': '红人合作数据需要手动整理或专用工具', 'confidence': '低'}
    
    def _scrape_pr(self, website: str) -> Dict[str, Any]:
        return {'note': 'PR稿件需要手动搜索整理', 'confidence': '低'}
    
    def _scrape_tech(self, website: str) -> Dict[str, Any]:
        return {'note': '技术维度需要BuiltWith等工具', 'confidence': '低'}
    
    def _scrape_ux(self, website: str) -> Dict[str, Any]:
        return {'note': '用户体验需要手动体验+用户反馈', 'confidence': '低'}
    
    def _scrape_ecosystem(self, website: str) -> Dict[str, Any]:
        return {'note': '生态集成需要手动整理', 'confidence': '低'}
    
    def _scrape_history(self, website: str) -> Dict[str, Any]:
        return {'note': '发展历程需要Crunchbase等工具', 'confidence': '低'}
    
    def _scrape_branding(self, website: str) -> Dict[str, Any]:
        return {'note': '品牌定位需要手动分析', 'confidence': '低'}
    
    def _scrape_supply_chain(self, website: str) -> Dict[str, Any]:
        return {'note': '供应链信息通常不公开', 'confidence': '低'}
    
    def _clean_data(self, dimension: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """数据清洗"""
        cleaned = data.copy()
        
        # 移除None值
        cleaned = {k: v for k, v in cleaned.items() if v is not None}
        
        # 标准化字符串
        for key, value in cleaned.items():
            if isinstance(value, str):
                cleaned[key] = value.strip()
        
        # 添加元数据
        cleaned['dimension'] = dimension
        cleaned['cleaned_at'] = datetime.now().isoformat()
        
        return cleaned
    
    def _validate_data(self, dimension: str, data: Dict[str, Any]) -> bool:
        """数据验证"""
        # 基础验证：数据不为空
        if not data or len(data) <= 2:  # 只有dimension和cleaned_at
            return False
        
        # 维度特定验证
        validators = {
            'G1': lambda d: 'total_visits' in d or 'traffic_sources' in d,
            'G2': lambda d: 'products' in d or 'new_releases' in d,
            'G3': lambda d: 'social_data' in d or 'followers' in d,
            'G7': lambda d: 'ads' in d or 'ad_count' in d,
        }
        
        validator = validators.get(dimension)
        if validator:
            return validator(data)
        
        return True
    
    def _cross_validate(self, dimension: str, data: Dict[str, Any], 
                       website: str) -> Dict[str, Any]:
        """交叉验证"""
        result = {'passed': True, 'warnings': []}
        
        # 检查数据时效性
        scraped_at = data.get('scraped_at', '')
        if scraped_at:
            try:
                scrape_time = datetime.fromisoformat(scraped_at.replace('Z', '+00:00'))
                if datetime.now() - scrape_time > timedelta(days=7):
                    result['warnings'].append('数据超过7天，可能已过期')
            except:
                pass
        
        # 检查置信度
        confidence = data.get('confidence', '中')
        if confidence == '低':
            result['warnings'].append('数据置信度低，建议二次验证')
        
        # 检查关键字段
        if 'error' in data:
            result['warnings'].append(f"数据包含错误: {data['error']}")
        
        if result['warnings']:
            result['passed'] = False
        
        return result
    
    def _compute_hash(self, data_str: str) -> str:
        """计算数据指纹"""
        return hashlib.md5(data_str.encode('utf-8')).hexdigest()
    
    def _compute_changes(self, old_data: Dict, new_data: Dict) -> List[str]:
        """计算数据变化"""
        changes = []
        
        for key in new_data:
            if key not in old_data:
                changes.append(f"新增: {key}")
            elif old_data[key] != new_data[key]:
                old_val = str(old_data[key])[:50]
                new_val = str(new_data[key])[:50]
                changes.append(f"变化: {key} ({old_val} → {new_val})")
        
        for key in old_data:
            if key not in new_data:
                changes.append(f"删除: {key}")
        
        return changes
    
    def _generate_report(self, competitor_id: int, name: str, 
                        dimensions: List[str], level: str) -> str:
        """生成报告"""
        logger.info("\n生成报告...")
        
        # 获取所有数据
        cursor = self.db.cursor()
        placeholders = ','.join(['?'] * len(dimensions))
        cursor.execute(f'''
            SELECT dimension, data, created_at FROM research_data
            WHERE competitor_id = ? AND dimension IN ({placeholders})
            ORDER BY created_at DESC
        ''', (competitor_id,) + tuple(dimensions))
        
        data = {}
        for row in cursor.fetchall():
            dimension, json_data, created_at = row
            if dimension not in data:
                data[dimension] = {
                    'data': json.loads(json_data),
                    'created_at': created_at
                }
        
        # 生成报告内容
        report = self._build_report_content(data, name, dimensions, level)
        
        # 保存报告
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"reports/output/{name}_{level}_{timestamp}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        
        logger.info(f"✓ 报告已生成: {filename}")
        return filename
    
    def _build_report_content(self, data: Dict, name: str, 
                             dimensions: List[str], level: str) -> str:
        """构建报告内容"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        report = f"""# {name} 竞品调研报告

> **生成时间**: {timestamp}
> **调研级别**: {level}
> **分析维度**: {', '.join(dimensions)}
> **数据来源**: Python爬虫抓取
> **成本**: $0

---

## 执行摘要

### 调研概况
- **目标竞品**: {name}
- **调研维度数**: {len(dimensions)}
- **数据完整度**: {len([d for d in data.values() if 'error' not in d.get('data', {})])}/{len(dimensions)}

### 核心发现
（此处需要根据实际数据人工填写）

---

## 详细分析

"""
        
        # 按维度输出详细分析
        dimension_names = {
            'G1': '流量起量分析', 'G2': '品牌新品动向', 'G3': '社媒数据分析',
            'G4': '红人合作分析', 'G5': 'UGC舆情分析', 'G6': 'PR稿件分析',
            'G7': '广告投放分析', 'S1': '功能对比分析', 'S2': '技术维度分析',
            'S3': '用户体验分析', 'S4': '商业模式分析', 'S5': '生态集成分析',
            'S6': '发展历程分析', 'B1': '产品矩阵分析', 'B2': '渠道布局分析',
            'B3': '品牌定位分析', 'B4': '供应链分析'
        }
        
        for dimension in dimensions:
            dim_name = dimension_names.get(dimension, dimension)
            report += f"### {dimension} {dim_name}\n\n"
            
            if dimension in data:
                dim_data = data[dimension]['data']
                report += f"**数据时间**: {data[dimension]['created_at']}\n\n"
                report += f"**置信度**: {dim_data.get('confidence', '中')}\n\n"
                
                if 'error' in dim_data:
                    report += f"⚠️ **数据获取失败**: {dim_data['error']}\n\n"
                else:
                    report += "**关键数据**:\n\n"
                    for key, value in dim_data.items():
                        if key not in ['confidence', 'source_url', 'scraped_at', 'cleaned_at', 'dimension']:
                            report += f"- {key}: {value}\n"
                
                if 'source_url' in dim_data:
                    report += f"\n**数据来源**: {dim_data['source_url']}\n"
            else:
                report += "❌ 未获取到数据\n"
            
            report += "\n---\n\n"
        
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
        raw_data = {dim: info['data'] for dim, info in data.items()}
        report += json.dumps(raw_data, ensure_ascii=False, indent=2)
        
        report += """
```

### 执行日志

"""
        
        # 添加执行日志
        cursor = self.db.cursor()
        cursor.execute('''
            SELECT dimension, level, status, message, created_at 
            FROM execution_logs 
            ORDER BY created_at DESC LIMIT 20
        ''')
        
        for row in cursor.fetchall():
            report += f"- [{row['created_at']}] {row['dimension']} ({row['level']}): {row['status']} - {row['message']}\n"
        
        report += """
---

*本报告由竞品调研工具自动生成，建议结合人工分析使用*
"""
        
        return report
    
    def _log_execution(self, competitor_id: Optional[int], dimension: Optional[str],
                      level: str, status: str, message: str, execution_time: float):
        """记录执行日志"""
        cursor = self.db.cursor()
        cursor.execute('''
            INSERT INTO execution_logs (competitor_id, dimension, level, status, message, execution_time)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (competitor_id, dimension, level, status, message, execution_time))
        self.db.commit()
    
    def get_execution_summary(self, competitor_name: str = None) -> Dict:
        """获取执行摘要"""
        cursor = self.db.cursor()
        
        if competitor_name:
            cursor.execute('SELECT id FROM competitors WHERE name = ?', (competitor_name,))
            competitor = cursor.fetchone()
            if competitor:
                cursor.execute('''
                    SELECT level, status, COUNT(*) as count
                    FROM execution_logs
                    WHERE competitor_id = ?
                    GROUP BY level, status
                ''', (competitor['id'],))
            else:
                return {'error': '竞品未找到'}
        else:
            cursor.execute('''
                SELECT level, status, COUNT(*) as count
                FROM execution_logs
                GROUP BY level, status
            ''')
        
        summary = {}
        for row in cursor.fetchall():
            level = row['level']
            status = row['status']
            count = row['count']
            
            if level not in summary:
                summary[level] = {}
            summary[level][status] = count
        
        return summary
    
    def schedule_updates(self, competitor_names: List[str], dimensions: List[str], 
                        frequency: str = 'weekly'):
        """设置定时更新任务"""
        import schedule
        import time
        
        def job():
            logger.info(f"执行定时任务: {frequency} 更新")
            for name in competitor_names:
                try:
                    self.run_research(name, dimensions, level='增量更新')
                except Exception as e:
                    logger.error(f"定时任务执行失败 {name}: {e}")
        
        if frequency == 'daily':
            schedule.every().day.at("09:00").do(job)
        elif frequency == 'weekly':
            schedule.every().monday.at("09:00").do(job)
        elif frequency == 'monthly':
            schedule.every(30).days.at("09:00").do(job)
        
        logger.info(f"已设置定时任务: {frequency}")
        logger.info("按 Ctrl+C 停止")
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)
        except KeyboardInterrupt:
            logger.info("定时任务已停止")

# 使用示例
if __name__ == '__main__':
    tool = CompetitorResearchTool()
    
    # 添加竞品
    tool.add_competitor('HubSpot', 'https://www.hubspot.com', 'SaaS')
    tool.add_competitor('Zoho', 'https://www.zoho.com', 'SaaS')
    
    # 执行轻度调研
    try:
        report_path = tool.run_research('HubSpot', ['G2', 'G3', 'S1', 'S4'], level='轻度')
        print(f"报告已生成: {report_path}")
    except Exception as e:
        print(f"调研失败: {e}")
    
    # 查看执行摘要
    summary = tool.get_execution_summary('HubSpot')
    print("执行摘要:", summary)
```

---

### 模式B：平台版执行方案

#### 核心原则
- **API优先**：优先使用付费API获取精准数据
- **标准化**：统一输入输出格式，支持批量处理
- **可扩展**：支持多租户、队列处理、水平扩展

#### 技术栈

| 层级 | 技术 | 成本 | 用途 |
|------|------|------|------|
| 后端框架 | Node.js/Python FastAPI | 免费 | API服务 |
| 数据库 | PostgreSQL | $15-50/月 | 数据存储 |
| 缓存 | Redis | $15-30/月 | 缓存+队列 |
| 队列 | Celery/RabbitMQ | $20-40/月 | 异步处理 |
| API集成 | SEMrush/Ahrefs/Meta | $100-300/月 | 数据获取 |
| 部署 | Docker + AWS/GCP | $50-100/月 | 服务部署 |
| 监控 | Prometheus/Grafana | $20-40/月 | 服务监控 |

#### 系统架构

```
┌─────────────────────────────────────────────────────────────┐
│                        客户端层                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ Web界面     │  │ API客户端   │  │ 第三方集成          │ │
│  │ (React/Vue) │  │ (SDK)       │  │ (Slack/钉钉/飞书)   │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                            │
┌─────────────────────────────────────────────────────────────┐
│                        API网关层                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ 认证授权    │  │ 限流熔断    │  │ 请求路由            │ │
│  │ (JWT/OAuth) │  │ (Rate Limit)│  │ (Load Balancer)     │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                            │
┌─────────────────────────────────────────────────────────────┐
│                        服务层                                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ 调研服务    │  │ 报告服务    │  │ 用户服务            │ │
│  │ (Research)  │  │ (Report)    │  │ (User/Tenant)       │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ 调度服务    │  │ 通知服务    │  │ 计费服务            │ │
│  │ (Scheduler) │  │ (Notification)│  │ (Billing)          │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                            │
┌─────────────────────────────────────────────────────────────┐
│                        数据层                                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ PostgreSQL  │  │ Redis       │  │ 对象存储            │ │
│  │ (主数据库)  │  │ (缓存+队列) │  │ (S3/阿里云OSS)      │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                            │
┌─────────────────────────────────────────────────────────────┐
│                        外部API层                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ SEMrush API │  │ Ahrefs API  │  │ SimilarWeb API      │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ Meta Ad API │  │ Reddit API  │  │ Google Search API   │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

#### API设计

```python
# platform_api.py - 平台版API设计
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import asyncio

app = FastAPI(title="竞品调研平台API")

# 数据模型
class ResearchRequest(BaseModel):
    competitor_name: str
    competitor_website: str
    industry: str  # saas / ecommerce / both
    dimensions: List[str]  # ['G1', 'G2', 'S1']
    level: str  # incremental / light / deep / audit
    client_id: str  # 租户ID
    callback_url: Optional[str] = None  # 完成通知URL

class ResearchResponse(BaseModel):
    task_id: str
    status: str  # pending / processing / completed / failed
    estimated_time: int  # 预计完成时间（分钟）
    cost_estimate: float  # 预计成本

class ReportOutput(BaseModel):
    task_id: str
    competitor_name: str
    report_url: str
    json_data: dict
    created_at: str
    cost_actual: float

# API端点
@app.post("/research", response_model=ResearchResponse)
async def create_research(request: ResearchRequest):
    """创建调研任务"""
    # 验证租户权限
    tenant = await verify_tenant(request.client_id)
    if not tenant:
        raise HTTPException(status_code=403, detail="无效的租户ID")
    
    # 检查余额
    if tenant.balance < estimate_cost(request.level, request.dimensions):
        raise HTTPException(status_code=402, detail="余额不足")
    
    # 创建任务
    task_id = await create_task(request)
    
    # 加入队列
    await queue_task(task_id)
    
    return ResearchResponse(
        task_id=task_id,
        status="pending",
        estimated_time=estimate_time(request.level, request.dimensions),
        cost_estimate=estimate_cost(request.level, request.dimensions)
    )

@app.get("/research/{task_id}", response_model=ReportOutput)
async def get_research(task_id: str, client_id: str):
    """获取调研结果"""
    # 验证租户权限
    task = await get_task(task_id)
    if task.client_id != client_id:
        raise HTTPException(status_code=403, detail="无权访问此任务")
    
    if task.status != "completed":
        raise HTTPException(status_code=400, detail="任务尚未完成")
    
    return ReportOutput(
        task_id=task_id,
        competitor_name=task.competitor_name,
        report_url=task.report_url,
        json_data=task.json_data,
        created_at=task.created_at,
        cost_actual=task.cost_actual
    )

@app.get("/research/{task_id}/status")
async def get_research_status(task_id: str):
    """获取任务状态"""
    task = await get_task(task_id)
    return {
        "task_id": task_id,
        "status": task.status,
        "progress": task.progress,
        "message": task.message
    }

@app.post("/batch-research")
async def create_batch_research(requests: List[ResearchRequest]):
    """批量创建调研任务"""
    task_ids = []
    for request in requests:
        response = await create_research(request)
        task_ids.append(response.task_id)
    
    return {
        "batch_id": generate_batch_id(),
        "task_ids": task_ids,
        "total_tasks": len(task_ids)
    }

# 成本估算
COST_MAP = {
    'incremental': {'base': 0, 'per_dimension': 0},
    'light': {'base': 0, 'per_dimension': 0},
    'deep': {'base': 5, 'per_dimension': 10},  # API调用成本
    'audit': {'base': 20, 'per_dimension': 25}
}

def estimate_cost(level: str, dimensions: List[str]) -> float:
    """估算成本"""
    cost_config = COST_MAP.get(level, COST_MAP['light'])
    return cost_config['base'] + cost_config['per_dimension'] * len(dimensions)

def estimate_time(level: str, dimensions: List[str]) -> int:
    """估算时间（分钟）"""
    time_map = {
        'incremental': 5,
        'light': 15,
        'deep': 60,
        'audit': 180
    }
    base_time = time_map.get(level, 15)
    return base_time + len(dimensions) * 5

# 辅助函数
async def verify_tenant(client_id: str):
    # 验证租户逻辑
    pass

async def create_task(request: ResearchRequest):
    # 创建任务逻辑
    pass

async def queue_task(task_id: str):
    # 加入队列逻辑
    pass

async def get_task(task_id: str):
    # 获取任务逻辑
    pass

def generate_batch_id():
    # 生成批次ID
    pass
```

---

## 第三阶段：维度执行手册（双模式）

### 【G1】流量起量分析

#### 自用版执行方案（$0）

**工具组合**：
- SimilarWeb免费版（网页抓取）
- Google Trends（API免费）
- Wayback Machine（API免费）

**执行步骤**：
1. 访问 SimilarWeb免费版 输入竞品域名
2. 记录总访问量、跳出率、页面深度、访问时长
3. 分析流量来源占比（直接/搜索/社媒/引荐）
4. 查看主要流量国家/地区
5. 使用Google Trends对比品牌搜索趋势
6. 使用Wayback Machine查看网站历史版本

**数据验证**：
- 交叉验证：SimilarWeb数据 vs Google Trends趋势
- 一致性检查：流量增长时间点是否与营销活动匹配

#### 平台版执行方案（$50-100）

**工具组合**：
- SEMrush API（$119.95/月）
- Google Trends API（免费）
- Wayback Machine API（免费）

**执行步骤**：
1. 调用SEMrush API获取域名流量概览
2. 获取流量历史数据（12个月）
3. 获取主要关键词排名
4. 分析自然流量 vs 付费流量占比
5. 识别流量增长关键节点
6. 关联增长节点与营销活动

---

### 【G2】品牌新品动向

#### 自用版执行方案（$0）

**工具组合**：
- 官网爬虫
- Wayback Machine
- 社媒监控

**执行步骤**：
1. 抓取竞品官网产品页面
2. 提取产品名称、价格、功能亮点
3. 对比Wayback Machine历史版本，识别新增产品
4. 监控社媒账号新品发布动态
5. 记录产品发布时间和定位

**数据验证**：
- 交叉验证：官网数据 vs 社媒发布 vs 用户讨论

#### 平台版执行方案（$20-50）

**工具组合**：
- 官网爬虫
- 新闻API（如NewsAPI）
- 社媒API

**执行步骤**：
1. 自动化抓取官网产品目录
2. 调用新闻API搜索产品发布新闻
3. 监控社媒账号API
4. 建立产品发布时间线
5. 分析产品定位和目标用户

---

### 【G3】社媒数据分析

#### 自用版执行方案（$0）

**工具组合**：
- 社媒平台公开数据
- Social Blade（免费版）
- 手动统计

**执行步骤**：
1. 访问竞品社媒主页（Twitter/LinkedIn/Instagram）
2. 记录粉丝数、互动率、发帖频率
3. 分析热门帖子主题和形式
4. 使用Social Blade查看粉丝增长趋势
5. 统计近30天发帖数量和互动数据

#### 平台版执行方案（$30-80）

**工具组合**：
- 社媒API（Twitter API v2 / Instagram Basic Display）
- 第三方分析工具（如Hootsuite）

**执行步骤**：
1. 调用社媒API获取账号数据
2. 获取帖子列表和互动数据
3. 分析内容主题和发布节奏
4. 识别高互动内容特征
5. 生成社媒表现报告

---

### 【G4】红人合作分析

#### 自用版执行方案（$0）

**工具组合**：
- Instagram/TikTok手动搜索
- 品牌标签搜索
- 红人数据库免费版

**执行步骤**：
1. 在社媒平台搜索品牌标签
2. 识别频繁提及品牌的账号
3. 分析红人粉丝数和互动率
4. 记录合作内容形式和效果
5. 估算红人营销投入

#### 平台版执行方案（$50-150）

**工具组合**：
- 社媒API
- 红人营销平台（如Upfluence）
- 品牌监测工具

**执行步骤**：
1. 自动化监测品牌提及
2. 识别合作红人名单
3. 分析红人受众画像
4. 评估合作内容效果
5. 估算红人营销ROI

---

### 【G5】UGC舆情分析

#### 自用版执行方案（$0）

**工具组合**：
- Reddit API（免费）
- Google Search
- 品牌社群

**执行步骤**：
1. 使用Reddit API搜索品牌提及
2. 分析用户讨论主题和情感
3. 识别常见问题和痛点
4. 收集用户建议和反馈
5. 统计正面/负面/中性比例

#### 平台版执行方案（$30-100）

**工具组合**：
- Reddit API
- G2 API（软件评价）
- 情感分析API

**执行步骤**：
1. 调用Reddit API获取品牌讨论
2. 调用G2 API获取产品评价
3. 使用情感分析API分析评价情感
4. 生成情感分布报告
5. 识别关键用户痛点

---

### 【G6】PR稿件分析

#### 自用版执行方案（$0）

**工具组合**：
- Google Search
- 新闻网站RSS
- 官网新闻页面

**执行步骤**：
1. 搜索"品牌名 + news/press"
2. 访问官网新闻中心
3. 记录PR稿件主题和发布时间
4. 分析PR策略和重点
5. 统计PR发布频率

#### 平台版执行方案（$20-50）

**工具组合**：
- Google Custom Search API
- 新闻API
- 品牌监测工具

**执行步骤**：
1. 调用API搜索品牌新闻
2. 自动化收集PR稿件
3. 分析PR主题和发布渠道
4. 评估PR传播效果
5. 生成PR策略报告

---

### 【G7】广告投放分析

#### 自用版执行方案（$0）

**工具组合**：
- Meta Ad Library（免费）
- Google Ads Transparency
- 手动搜索

**执行步骤**：
1. 访问Meta Ad Library搜索品牌
2. 记录活跃广告数量和创意
3. 分析广告文案和CTA
4. 查看广告投放时间和地区
5. 估算广告支出（根据展示量）

#### 平台版执行方案（$30-80）

**工具组合**：
- Meta Ad Library API
- 广告监测工具
- 竞品广告分析平台

**执行步骤**：
1. 调用Meta Ad API获取广告数据
2. 分析广告创意和文案
3. 监测广告投放策略
4. 估算广告支出和ROI
5. 生成广告策略报告

---

### 【S1】功能对比分析（SaaS）

#### 自用版执行方案（$0）

**工具组合**：
- 官网功能页面爬虫
- 产品手册下载
- 免费试用

**执行步骤**：
1. 抓取竞品功能页面
2. 提取功能列表和描述
3. 注册免费试用体验产品
4. 记录核心功能和差异化功能
5. 制作功能对比矩阵

#### 平台版执行方案（$50-100）

**工具组合**：
- 官网爬虫
- G2 API（产品对比）
- 产品分析平台

**执行步骤**：
1. 自动化抓取功能信息
2. 调用G2 API获取用户评价
3. 分析功能热度和满意度
4. 生成功能对比报告
5. 识别功能差距和机会

---

### 【S4】商业模式分析（SaaS）

#### 自用版执行方案（$0）

**工具组合**：
- 官网定价页面
- 产品文档
- 用户评价

**执行步骤**：
1. 抓取定价页面信息
2. 记录定价层级和功能差异
3. 分析付费模式（月付/年付/按需）
4. 识别目标客户群体
5. 估算客单价和LTV

#### 平台版执行方案（$20-50）

**工具组合**：
- 官网爬虫
- 付费数据平台（如PitchBook）
- 用户评价API

**执行步骤**：
1. 自动化收集定价信息
2. 分析定价策略变化
3. 对比行业定价基准
4. 评估商业模式健康度
5. 生成商业模式报告

---

## 第四阶段：数据验证机制（双模式）

### 自用版验证策略

**核心原则**：用多个免费工具交叉验证，不依赖付费API

| 维度 | 主要来源 | 验证来源1 | 验证来源2 | 验证方法 |
|------|---------|----------|----------|---------|
| G1 流量 | SimilarWeb免费 | Google Trends | Wayback Machine | 趋势一致性 |
| G2 新品 | 官网 | Wayback Machine | 社媒 | 发布时间验证 |
| G3 社媒 | 社媒平台 | Social Blade | 手动统计 | 数据一致性 |
| G5 UGC | Reddit | G2 | Twitter | 情感一致性 |
| G7 广告 | Meta Ad Library | 官网 | 社媒 | 活动一致性 |

### 平台版验证策略

**核心原则**：API数据为主，爬虫为辅，多重验证

| 维度 | 主要来源 | 验证来源1 | 验证来源2 | 验证方法 |
|------|---------|----------|----------|---------|
| G1 流量 | SEMrush API | SimilarWeb API | Ahrefs API | 三方数据对比 |
| G2 新品 | 官网爬虫 | 新闻API | 社媒API | 多源时间验证 |
| G3 社媒 | 社媒API | 爬虫 | 第三方分析 | API+爬虫对比 |
| G5 UGC | Reddit API | G2 API | 爬虫 | 情感分析验证 |
| G7 广告 | Meta Ad API | 爬虫 | 搜索广告 | API+手动验证 |

---

## 第五阶段：报告生产流程

### 自用版生产流程

```
1. 配置竞品和维度（config/competitors.json）
2. 运行爬虫脚本（python main.py）
3. 数据自动存入SQLite
4. 生成Markdown报告（reports/output/）
5. 人工审核关键数据
6. 输出最终报告
```

**定时任务配置**：

```bash
# Linux/Mac crontab 配置
# 每周一早9点执行增量更新
0 9 * * 1 cd /path/to/competitor-research && python main.py --update

# 每月1号执行轻度调研
0 9 1 * * cd /path/to/competitor-research && python main.py --research --level light

# 每季度1号执行深度调研
0 9 1 1,4,7,10 * cd /path/to/competitor-research && python main.py --research --level deep
```

```powershell
# Windows 任务计划程序配置
# 使用PowerShell脚本创建定时任务
$action = New-ScheduledTaskAction -Execute "python" -Argument "main.py --update"
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 9am
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "CompetitorUpdate"
```

### 平台版生产流程

```
1. 客户通过API提交调研请求
2. 系统验证租户权限和余额
3. 任务加入队列（Celery/RabbitMQ）
4. 工作节点并行执行API调用和爬虫
5. 数据验证和交叉验证
6. 自动生成报告（Markdown + JSON）
7. 可选：人工审核
8. 通知客户任务完成
9. 客户下载报告
```

---

## 第六阶段：输出模板

### 轻度调研报告模板

```markdown
# [竞品名称] 轻度调研报告

> **生成时间**: 2024-XX-XX
> **调研级别**: 轻度
> **数据来源**: 爬虫抓取
> **成本**: $0
> **耗时**: 1-2小时

---

## 执行摘要

### 调研概况
- **目标竞品**: [竞品名称]
- **调研维度**: [维度列表]
- **数据完整度**: [X/Y]

### 核心发现（3-5点）
1. [发现1]
2. [发现2]
3. [发现3]

### 关键建议
1. [建议1]
2. [建议2]

---

## 详细分析

### [维度1] [维度名称]
**关键数据**:
- [数据点1]
- [数据点2]

**分析**:
[简要分析]

### [维度2] [维度名称]
...

---

## 数据来源与局限

### 数据来源
- [工具/来源1]
- [工具/来源2]

### 数据局限
- [局限1]
- [局限2]

### 置信度评级
- 高: [X]%
- 中: [X]%
- 低: [X]%

---

*本报告由竞品调研工具自动生成，建议结合人工分析使用*
```

### 深度调研报告模板

```markdown
# [竞品名称] 深度调研报告

> **报告编号**: RPT-XXXX
> **生成时间**: 2024-XX-XX
> **调研级别**: 深度
> **数据来源**: API + 爬虫
> **成本**: $X
> **耗时**: 4-8小时

---

## 执行摘要

### 调研概况
- **目标竞品**: [竞品名称]
- **调研维度**: [全部维度]
- **数据完整度**: [X/Y]
- **交叉验证通过率**: [X]%

### 核心发现（5-10点）
1. [发现1]
2. [发现2]
...

### 战略建议
1. [建议1]
2. [建议2]
...

### 风险提示
1. [风险1]
2. [风险2]

---

## 详细分析

### 第一部分：流量与增长分析

#### G1 流量起量分析
**数据来源**: [工具名称]
**置信度**: [高/中/低]

**关键数据**:
- 总访问量: [数据]
- 流量来源: [数据]
- 增长趋势: [数据]

**流量起量时间点分析**:
- 起量时间: [时间]
- 可能原因: [分析]
- 关键动作: [动作]

#### G7 广告投放分析
...

### 第二部分：产品与品牌分析

#### G2 品牌新品动向
...

#### B1 产品矩阵分析（品牌）
...

### 第三部分：用户与口碑分析

#### G3 社媒数据分析
...

#### G5 UGC舆情分析
...

### 第四部分：战略与商业模式分析

#### S4 商业模式分析（SaaS）
...

#### B3 品牌定位分析（品牌）
...

---

## 数据验证

### 验证方法
- [验证方法1]
- [验证方法2]

### 验证结果
| 维度 | 主要来源 | 验证来源 | 结果 |
|------|---------|----------|------|
| [维度] | [来源] | [来源] | [通过/警告] |

### 数据质量评级
- 高置信度: [X]%
- 中置信度: [X]%
- 低置信度: [X]%

---

## 附录

### A. 原始数据（JSON）
```json
[JSON数据]
```

### B. 执行日志
[日志内容]

### C. 工具配置
[配置信息]

### D. 参考链接
- [链接1]
- [链接2]

---

*本报告由竞品调研工具自动生成，建议结合人工分析使用*
*报告生成时间: [时间]*
```

---

## 第七阶段：模式切换指南

### 从自用版升级到平台版

**触发条件**：
- 需要服务多个客户
- 需要标准化输出
- 需要商业化运营

**升级步骤**：
1. **数据迁移**：SQLite → PostgreSQL
2. **架构升级**：本地脚本 → 服务端API
3. **工具升级**：爬虫为主 → API为主
4. **功能增加**：多租户、计费、权限管理
5. **部署上线**：Docker + 云服务器

**成本变化**：
- 自用版：$0-20/月
- 平台版：$200-500/月（含服务器+API+数据库）
- 收入预期：$2000-10000/月（按客户数）

### 平台版降级到自用版

**触发条件**：
- 客户减少，成本过高
- 只需要服务自己
- 预算紧张

**降级步骤**：
1. **数据导出**：PostgreSQL → SQLite
2. **架构简化**：服务端API → 本地脚本
3. **工具降级**：API为主 → 爬虫为主
4. **功能裁剪**：去掉多租户、计费
5. **本地运行**：个人电脑/树莓派

---

## 第八阶段：使用示例

### 示例1：自用版 - 定期监测竞品

**场景**：你是产品经理，每月需要监测3个竞品的动态

**配置**：
```json
// config/competitors.json
{
  "competitors": [
    {"name": "HubSpot", "website": "https://www.hubspot.com", "industry": "saas"},
    {"name": "Zoho", "website": "https://www.zoho.com", "industry": "saas"},
    {"name": "Salesforce", "website": "https://www.salesforce.com", "industry": "saas"}
  ],
  "schedule": {
    "incremental": "weekly",
    "light": "monthly",
    "deep": "quarterly"
  },
  "dimensions": {
    "incremental": ["G2", "G3", "G7"],
    "light": ["G1", "G2", "G3", "S1", "S4"],
    "deep": ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "S1", "S2", "S3", "S4"]
  }
}
```

**执行**：
```bash
# 安装依赖
pip install requests beautifulsoup4 pandas schedule

# 首次运行深度调研
python main.py --research --competitor HubSpot --level deep

# 设置定时任务（每周增量更新）
python main.py --schedule --frequency weekly

# 查看报告
ls reports/output/
```

**月度成本**：$0

---

### 示例2：平台版 - 服务客户

**场景**：你是咨询顾问，为客户提供竞品调研服务

**客户请求**：
```json
{
  "client_id": "client_001",
  "competitor_name": "Notion",
  "competitor_website": "https://www.notion.so",
  "industry": "saas",
  "dimensions": ["G1", "G2", "G3", "S1", "S3", "S4"],
  "level": "deep"
}
```

**API调用**：
```bash
curl -X POST https://your-platform.com/api/research \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "competitor_name": "Notion",
    "competitor_website": "https://www.notion.so",
    "industry": "saas",
    "dimensions": ["G1", "G2", "G3", "S1", "S3", "S4"],
    "level": "deep",
    "client_id": "client_001"
  }'
```

**响应**：
```json
{
  "task_id": "task_12345",
  "status": "pending",
  "estimated_time": 90,
  "cost_estimate": 65.0
}
```

**查询状态**：
```bash
curl https://your-platform.com/api/research/task_12345/status \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**获取报告**：
```bash
curl https://your-platform.com/api/research/task_12345 \
  -H "Authorization: Bearer YOUR_API_KEY" \
  --output report.zip
```

**收费**：$1500/份（深度调研）
**成本**：$65（API+服务器）
**利润**：$1435

---

## 第九阶段：局限性说明

### 自用版局限
1. **反爬虫风险**：频繁抓取可能被封IP，需要控制频率
2. **数据精度**：免费工具数据不如付费API精准
3. **维护成本**：需要个人维护代码和定时任务
4. **扩展性**：单用户，无法服务他人

### 平台版局限
1. **API成本**：付费API成本较高，需要合理定价
2. **技术门槛**：需要后端开发和运维能力
3. **合规风险**：需要遵守各平台API使用条款
4. **竞争风险**：市场上已有类似服务（如SEMrush、SimilarWeb）

---

## 第十阶段：FAQ与故障排除

### 常见问题

**Q1: 爬虫被封IP怎么办？**
A: 
- 降低请求频率（在config/settings.json中增加request_delay）
- 使用代理IP池
- 使用Playwright模拟真实浏览器行为
- 考虑使用付费API替代

**Q2: 数据置信度低怎么办？**
A:
- 增加验证来源
- 手动验证关键数据点
- 使用多个工具交叉验证
- 在报告中明确标注置信度

**Q3: 如何增加新的调研维度？**
A:
1. 在config/dimensions.json中定义新维度
2. 在scrapers/目录下创建新爬虫
3. 在main.py的_scrape_dimension方法中注册
4. 更新报告模板

**Q4: 定时任务没有执行？**
A:
- 检查crontab配置是否正确
- 检查Python路径是否正确
- 查看logs/research.log中的错误信息
- 确保脚本有执行权限

**Q5: 如何升级到平台版？**
A: 参考[模式切换指南](#第七阶段模式切换指南)

### 故障排除

**问题：ImportError: No module named 'scrapers'**
解决：确保scrapers目录下有__init__.py文件

**问题：sqlite3.OperationalError: no such table**
解决：运行main.py时会自动创建表，如仍报错，手动执行_init_database方法

**问题：请求超时**
解决：在config/settings.json中增加timeout值

**问题：数据为空**
解决：检查目标网站是否改版，更新爬虫选择器

---

## 核心原则

1. **横纵交叉**：纵向（时间线+决策逻辑）× 横向（现状对比）= 预判
2. **流量锚定**：流量起量时间点是关键锚点
3. **模式匹配**：根据需求选择自用版或平台版
4. **预算可控**：自用版$0-20/月，平台版$200-500/月
5. **增量优先**：优先使用增量更新，节省时间和成本
6. **验证为王**：每条数据必须有来源、有验证
7. **自动化**：能脚本就不手动，能定时就不临时
8. **可落地**：所有工具和方法都必须可执行、可验证

---

## 版本历史

- **v1**: 基础框架，横纵分析法
- **v2**: 增加执行手册和验证机制
- **v3**: 增加预算框架和爬虫代码
- **v4**: 双模式架构（自用版+平台版）
- **v5**: 最终优化版，增加流程图、决策树、FAQ、完整代码

---

*本SKILL持续更新，欢迎提交Issue和PR*

# 竞品调研洞察 SKILL

> 深度竞品/品类调研与洞察分析框架。融合横纵分析法、流量起量追踪与全维度月度监测，支持自用版（低预算爬虫驱动）和平台版（API服务化）两种模式。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/yourusername/competitor-research-skill.git
cd competitor-research-skill
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置竞品

编辑 `config/competitors.json`：

```json
{
  "competitors": [
    {
      "name": "HubSpot",
      "website": "https://www.hubspot.com",
      "industry": "saas"
    }
  ]
}
```

### 4. 运行调研

```bash
python main.py --research --competitor HubSpot --level light
```

### 5. 查看报告

```bash
ls reports/output/
```

---

## 核心特性

| 特性 | 自用版 | 平台版 |
|------|--------|--------|
| **月预算** | $0-20 | $100-500 |
| **数据获取** | 80%爬虫 + 20%手动 | 80%API + 20%爬虫 |
| **执行方式** | 本地脚本/定时任务 | 服务端部署/队列处理 |
| **存储方式** | SQLite/本地文件 | PostgreSQL/MongoDB |
| **输出格式** | Markdown + JSON | Markdown + JSON + PDF |
| **适用人群** | 产品经理、运营、创业者 | 咨询顾问、服务商、中大型企业 |

---

## 文件结构

```
competitor-research-skill/
├── README.md                          # 本文件
├── SKILL.md                           # 完整SKILL文档
├── requirements.txt                   # Python依赖
├── main.py                            # 主入口（自用版）
├── config/                            # 配置文件
│   ├── competitors.json               # 竞品配置
│   ├── dimensions.json                # 维度配置
│   └── settings.json                  # 全局设置
├── scrapers/                          # 爬虫模块
│   ├── __init__.py
│   ├── meta_ad_scraper.py             # Meta广告爬虫
│   ├── reddit_scraper.py              # Reddit爬虫
│   ├── web_scraper.py                 # 通用网页爬虫
│   ├── similarweb_scraper.py          # SimilarWeb爬虫
│   └── social_media_scraper.py        # 社媒爬虫
├── utils/                             # 工具模块
│   ├── __init__.py
│   ├── validator.py                   # 数据验证
│   ├── comparator.py                  # 数据对比
│   └── reporter.py                    # 报告生成
├── reports/                           # 报告目录
│   ├── templates/                     # 报告模板
│   └── output/                        # 输出目录
├── examples/                          # 示例报告
│   └── 北美充气泵市场调研报告.md       # 实战案例
├── docs/                              # 文档
│   ├── 执行流程图.md                   # 流程图说明
│   ├── 工具选型决策树.md               # 工具选择指南
│   └── FAQ.md                         # 常见问题
└── platform/                          # 平台版代码
    ├── api.py                         # FastAPI服务
    ├── models.py                      # 数据模型
    └── scrapers/                      # 平台版爬虫
```

---

## 调研级别

| 级别 | 时间成本 | 工具成本 | 输出规模 | 适用场景 |
|------|----------|----------|----------|----------|
| **增量更新** | 30min-1h | $0 | 1000-2000字 | 定期更新变化 |
| **轻度调研** | 1-2h | $0 | 3000-5000字 | 快速扫描 |
| **深度调研** | 4-8h | $0-300 | 10000-15000字 | 战略决策 |
| **全面审计** | 16-24h | $300-500 | 20000-30000字 | 重要客户/尽调 |

---

## 分析维度

### 通用维度（G1-G7）

| 维度 | 名称 | 自用版工具 | 平台版工具 |
|------|------|-----------|-----------|
| G1 | 流量起量 | SimilarWeb免费+爬虫 | SEMrush API |
| G2 | 品牌新品 | 官网爬虫 | 官网爬虫+新闻API |
| G3 | 社媒数据 | 社媒爬虫 | 社媒API+爬虫 |
| G4 | 红人合作 | Instagram爬虫 | 社媒API |
| G5 | UGC舆情 | Reddit爬虫 | Reddit API |
| G6 | PR稿件 | Google Search爬虫 | Google Custom Search API |
| G7 | 广告投放 | Meta Ad Library爬虫 | Meta Ad Library API |

### SaaS专属维度（S1-S6）

| 维度 | 名称 | 自用版工具 | 平台版工具 |
|------|------|-----------|-----------|
| S1 | 功能对比 | 官网爬虫 | 官网爬虫+G2 API |
| S2 | 技术维度 | BuiltWith | BuiltWith API |
| S3 | 用户体验 | 官网爬虫+Reddit | G2 API+爬虫 |
| S4 | 商业模式 | 官网爬虫 | 官网爬虫 |
| S5 | 生态集成 | 官网爬虫 | 官网爬虫 |
| S6 | 发展历程 | Crunchbase爬虫 | Crunchbase API |

### 品牌/消费品专属维度（B1-B4）

| 维度 | 名称 | 自用版工具 | 平台版工具 |
|------|------|-----------|-----------|
| B1 | 产品矩阵 | 官网爬虫 | 官网爬虫 |
| B2 | 渠道布局 | 官网爬虫+SimilarWeb | SimilarWeb API |
| B3 | 品牌定位 | 官网爬虫 | 官网爬虫 |
| B4 | 供应链 | 官网爬虫 | 官网爬虫 |

---

## 实战案例

### 案例1：北美充气泵市场调研

**场景**：品牌负责人判断是否切入北美充气泵市场

**调研级别**：轻度调研

**调研维度**：G1, G2, G3, G5, G7, B1, B2, B3

**执行结果**：
- 时间成本：2小时
- 工具成本：$0
- 输出：5000字调研报告

**核心结论**：
1. 市场存在机会，但竞争激烈
2. 建议差异化定位（便携性/智能化）
3. 重点关注亚马逊渠道

[查看完整报告](examples/北美充气泵市场调研报告.md)

---

## 技术栈

### 自用版

| 层级 | 技术 | 成本 |
|------|------|------|
| 爬虫框架 | Python + Scrapy/Playwright | 免费 |
| 数据存储 | SQLite | 免费 |
| 定时任务 | crontab/Windows任务计划 | 免费 |
| 数据分析 | Pandas + Jupyter | 免费 |
| 报告生成 | Python-Markdown | 免费 |

### 平台版

| 层级 | 技术 | 成本 |
|------|------|------|
| 后端框架 | Python FastAPI | 免费 |
| 数据库 | PostgreSQL | $15-50/月 |
| 缓存 | Redis | $15-30/月 |
| 队列 | Celery/RabbitMQ | $20-40/月 |
| API集成 | SEMrush/Ahrefs/Meta | $100-300/月 |
| 部署 | Docker + AWS/GCP | $50-100/月 |

---

## 贡献指南

欢迎提交Issue和PR！

### 提交Issue

- 描述问题或建议
- 提供复现步骤（如适用）
- 标注相关维度或工具

### 提交PR

1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开Pull Request

---

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## 联系方式

- 项目维护者：[Your Name]
- 邮箱：[your.email@example.com]
- 项目链接：https://github.com/yourusername/competitor-research-skill

---

## 致谢

- 横纵分析法参考：[微信公众号文章](https://mp.weixin.qq.com/s/c3c6R4BHAwoW5eGy30ifyQ)
- 感谢所有贡献者和用户

---

*本SKILL持续更新，建议定期查看最新版本*

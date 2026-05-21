# Data Engineering 数据获取与处理

> 精选量化金融数据获取、清洗、存储与另类数据相关的顶级开源工具。

---

## 市场数据获取

| 项目 | Stars量级 | 数据源 | 特点 |
|------|-----------|--------|------|
| [ranaroussi/yfinance](https://github.com/ranaroussi/yfinance) | ⭐ 14k+ | Yahoo Finance | 最流行的免费股票数据库，A股有限 |
| [akfamily/akshare](https://github.com/akfamily/akshare) | ⭐ 9k+ | 国内多源 | A股/期货/基金/宏观数据，国内最全 |
| [waditu/tushare](https://github.com/waditu/tushare) | ⭐ 13k+ | Tushare | A股权威数据，需积分（部分免费） |
| [shashankvemuri/Finance](https://github.com/shashankvemuri/Finance) | ⭐ 2k+ | 多源 | 150+ Python 数据获取程序 |

## 综合量化数据平台

| 项目 | 特点 |
|------|------|
| [goldmansachs/gs-quant](https://github.com/goldmansachs/gs-quant) | 接入高盛数据服务，含宏观/信用/股票数据 |
| [ricequant/rqalpha](https://github.com/ricequant/rqalpha) | 附带米筐数据服务，A股历史数据质量高 |

## 数据类型与来源

### 行情数据
```
日线/分钟线/Tick 数据
OHLCV（开高低收量）
Level 2 订单薄数据
期权链数据
```

### 基本面数据
```
财务报表（利润表/资产负债表/现金流量表）
估值指标（PE/PB/PS/EV/EBITDA）
分析师预期与调整
```

### 另类数据
```
卫星图像（停车场/工厂活跃度）
信用卡消费数据
社交媒体情感（Twitter/Reddit/雪球）
招聘数据、网络流量
供应链关系数据
```

### 宏观数据
```
利率、汇率、CPI/PPI
PMI、GDP、就业数据
央行政策、货币供应量
```

## 数据质量问题

| 问题 | 说明 | 处理方法 |
|------|------|----------|
| **前视偏差** | 使用了未来才有的数据 | Point-in-Time 数据库 |
| **幸存者偏差** | 只有现存公司数据 | 含退市股票的历史数据 |
| **分红/拆股复权** | 未复权导致价格跳变 | 前复权 / 后复权处理 |
| **异常值** | 错误报价、数据错误 | Z-score 过滤、3σ 截断 |
| **缺失值** | 停牌、节假日 | 前填充 / 插值 / 标记 |

## 数据存储方案

```
小规模：CSV / Parquet 文件
中规模：SQLite / PostgreSQL
大规模：ClickHouse / Arctic (MongoDB) / KDB+
实时流：Redis / Kafka

推荐组合：
  历史数据 → Parquet + PyArrow
  时间序列 → InfluxDB / ClickHouse
  实时行情 → Redis
```

## 数据处理工具链

```python
# 常用工具
pandas       — 数据处理基础
polars       — 高性能 DataFrame（Rust 实现）
numpy        — 数值计算
scipy        — 统计分析
ta-lib       — 技术指标计算
pandas-ta    — 纯 Python 技术指标库
```

## Point-in-Time 数据实践

```
财务数据的发布有时间延迟（如 Q1 财报在 4-5 月才公布）
必须使用报告期的"实际发布时间"而非"报告期结束时间"
避免使用未来才知道的修订数据
```

## 延伸资源

- [awesome-quant](https://github.com/wilsonfreitas/awesome-quant) — 含数据源分类（Data Sources 章节）
- [quant-wiki](https://github.com/LLMQuant/quant-wiki) — 数据工程知识库（中英文）
- [Barca0412/Introduction-to-Quantitative-Finance](https://github.com/Barca0412/Introduction-to-Quantitative-Finance) — 多因子框架含数据处理教程

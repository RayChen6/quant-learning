# 数据获取与处理 | Data Engineering

量化研究的数据基础设施，涵盖行情数据获取、清洗、存储与特征构建。

## 学习路线

```
数据源了解 → 数据获取 → 数据清洗 → 复权处理 → 特征工程 → 数据存储
```

## 目录结构

```
data-engineering/
├── notes/
│   ├── 00_overview.md          # 知识点速览
│   ├── 01_data_sources.md      # 数据源介绍与对比
│   └── 02_data_cleaning.md     # 数据清洗规范
├── code/
│   ├── fetch_data.py           # 多数据源获取脚本
│   └── process_ohlcv.py        # OHLCV 处理与复权计算
└── notebooks/
    └── data_quality_check.ipynb  # 数据质量检查流程
```

## 核心主题

- **数据源**：tushare、akshare、yfinance、Wind、Bloomberg
- **数据类型**：OHLCV、Tick、财务数据、另类数据
- **数据清洗**：缺失值、异常值、退市处理、复权
- **存储方案**：CSV、HDF5、Parquet、数据库（SQLite/PostgreSQL）

## 推荐资源

- [Tushare Pro 文档](https://tushare.pro/document/2)
- [AkShare 文档](https://akshare.akfamily.xyz/)
- Python 库：`pandas`, `akshare`, `tushare`, `pyarrow`

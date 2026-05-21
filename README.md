# Backtesting 回测框架

> 精选 GitHub 上最优质的回测框架与工具，按成熟度和特点分类整理。

---

## 生产级框架

| 项目 | Stars量级 | 语言 | 特点 |
|------|-----------|------|------|
| [QuantConnect/Lean](https://github.com/QuantConnect/Lean) | ⭐ 10k+ | C#/Python | 工业级引擎，支持股票/期权/期货/Crypto，云端回测+实盘 |
| [mementum/backtrader](https://github.com/mementum/backtrader) | ⭐ 13k+ | Python | 最受欢迎的 Python 回测库，事件驱动，文档完善 |
| [quantopian/zipline](https://github.com/quantopian/zipline) | ⭐ 17k+ | Python | Quantopian 出品，Pipeline API，因子研究友好 |
| [ricequant/rqalpha](https://github.com/ricequant/rqalpha) | ⭐ 5k+ | Python | 国内米筐科技出品，支持 A 股，可扩展架构 |

## 轻量/专项框架

| 项目 | Stars量级 | 特点 |
|------|-----------|------|
| [edtechre/pybroker](https://github.com/edtechre/pybroker) | ⭐ 2k+ | 内置 ML 模型支持，向量化 + 事件驱动混合 |
| [gbeced/pyalgotrade](https://github.com/gbeced/pyalgotrade) | ⭐ 4k+ | 纯 Python，技术指标丰富，适合学习 |
| [gbeced/basana](https://github.com/gbeced/basana) | ⭐ 500+ | async 异步框架，专注 Crypto，同作者新作 |
| [akfamily/akquant](https://github.com/akfamily/akquant) | ⭐ 新兴 | Rust+Python 高性能，国内 AKShare 生态 |

## 组合优化回测

| 项目 | Stars量级 | 特点 |
|------|-----------|------|
| [cvxgrp/cvxportfolio](https://github.com/cvxgrp/cvxportfolio) | ⭐ 1k+ | Stanford 出品，凸优化组合回测，学术严谨 |

## 书籍配套代码

| 项目 | 对应书籍 | 特点 |
|------|----------|------|
| [yhilpisch/py4at](https://github.com/yhilpisch/py4at) | Python for Algorithmic Trading (O'Reilly) | Yves Hilpisch 著，系统完整 |
| [chrisconlan/algorithmic-trading-with-python](https://github.com/chrisconlan/algorithmic-trading-with-python) | Algorithmic Trading with Python (2020) | 含完整策略实现 |
| [nickmccullum/algorithmic-trading-python](https://github.com/nickmccullum/algorithmic-trading-python) | freeCodeCamp 免费课程 | 适合入门，含 Jupyter Notebook |

## 学习路径建议

```
入门: backtrader (文档最完善)
      ↓
进阶: zipline (Pipeline 因子体系) / rqalpha (A股实战)
      ↓
生产: QuantConnect Lean (多资产 + 实盘)
      ↓
研究: cvxportfolio (组合优化) / pybroker (ML策略)
```

## 关键概念

- **事件驱动回测** vs **向量化回测**：前者更真实（含滑点/成交逻辑），后者更快
- **前视偏差 (Look-ahead Bias)**：最常见的回测错误，使用 Pipeline/Point-in-time 数据规避
- **过拟合**：Walk-forward 验证、样本外测试、参数敏感性分析
- **交易成本**：手续费、滑点、市场冲击成本建模

## 延伸资源

- [awesome-quant](https://github.com/wilsonfreitas/awesome-quant) — 量化综合资源列表
- [quant-wiki](https://github.com/LLMQuant/quant-wiki) — 中英文量化知识库

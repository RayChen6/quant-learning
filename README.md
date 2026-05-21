# 执行与交易系统 | Execution & Trading Systems

交易执行层的核心知识，涵盖市场微观结构、算法执行与交易成本分析。

## 学习路线

```
市场微观结构 → 订单类型 → 算法执行 → 交易成本分析 → OMS 设计
```

## 目录结构

```
execution/
├── notes/
│   ├── 00_overview.md              # 知识点速览
│   ├── 01_market_microstructure.md # 市场微观结构
│   └── 02_execution_algorithms.md  # 算法执行策略
├── code/
│   ├── simple_oms.py               # 简单订单管理系统
│   └── transaction_cost.py         # 交易成本分析
└── notebooks/
    └── order_book_visualization.ipynb  # 订单簿可视化
```

## 核心主题

- **市场微观结构**：买卖价差、订单簿、价格发现、市场冲击
- **算法执行**：TWAP、VWAP、POV、IS（Implementation Shortfall）
- **交易成本**：佣金、滑点、市场冲击成本、时机成本
- **OMS**：订单状态管理、风控前置、成交回报处理

## 推荐资源

- 《Trading and Exchanges》— Larry Harris
- 《Algorithmic and High-Frequency Trading》— Álvaro Cartea
- Python 库：`pandas`, `numpy`, `matplotlib`

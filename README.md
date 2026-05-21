# 回测框架 | Backtesting

回测系统设计与实现，理解回测偏差来源，构建可靠的策略评估体系。

## 学习路线

```
回测原理 → 偏差识别 → 向量化回测 → 事件驱动回测 → 绩效评估
```

## 目录结构

```
backtesting/
├── notes/
│   ├── 00_overview.md          # 知识点速览
│   ├── 01_backtest_bias.md     # 回测偏差与陷阱
│   └── 02_performance_metrics.md  # 绩效评估指标
├── code/
│   ├── vectorized_backtest.py  # 向量化回测框架
│   └── event_driven_engine.py  # 事件驱动回测骨架
└── notebooks/
    └── full_backtest_example.ipynb  # 完整回测示例
```

## 核心主题

- **回测偏差**：前视偏差（Look-ahead Bias）、幸存者偏差、过拟合
- **向量化回测**：基于 pandas 的高效回测实现
- **事件驱动回测**：订单、撮合、持仓管理
- **绩效指标**：Sharpe、Sortino、最大回撤、Calmar、年化收益

## 推荐资源

- 《Advances in Financial Machine Learning》— Marcos López de Prado
- 开源框架：`backtrader`, `zipline`, `vnpy`
- Python 库：`pandas`, `numpy`, `matplotlib`

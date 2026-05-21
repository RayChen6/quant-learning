# 策略开发 | Strategy Development

主流量化交易策略的原理与实现，涵盖动量、均值回归、套利与趋势跟踪。

## 学习路线

```
策略逻辑理解 → 信号生成 → 仓位管理 → 止损止盈 → 参数优化
```

## 目录结构

```
strategy-dev/
├── notes/
│   ├── 00_overview.md          # 知识点速览
│   ├── 01_momentum.md          # 动量策略
│   └── 02_mean_reversion.md    # 均值回归与统计套利
├── code/
│   ├── dual_ma_strategy.py     # 双均线趋势策略
│   └── pairs_trading.py        # 配对交易策略
└── notebooks/
    └── strategy_logic.ipynb    # 策略逻辑验证
```

## 核心主题

- **动量策略**：时序动量、截面动量、双均线
- **均值回归**：布林带、RSI、Z-Score
- **统计套利**：配对交易、协整检验、价差建模
- **CTA**：趋势跟踪、突破策略、通道策略

## 推荐资源

- 《Algorithmic Trading》— Ernest Chan
- 《Quantitative Trading》— Ernest Chan
- Python 库：`pandas`, `numpy`, `scipy`

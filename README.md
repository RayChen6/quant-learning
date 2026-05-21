# 风险管理 | Risk Management

量化组合的风险度量、控制与压力测试体系。

## 学习路线

```
风险指标认识 → VaR/CVaR → 组合风险分解 → 压力测试 → 风控规则设计
```

## 目录结构

```
risk-management/
├── notes/
│   ├── 00_overview.md          # 知识点速览
│   ├── 01_var_cvar.md          # VaR 与 CVaR 理论
│   └── 02_portfolio_risk.md    # 组合风险分解
├── code/
│   ├── var_calculator.py       # 历史/参数/蒙特卡洛 VaR
│   └── risk_decomposition.py   # 组合风险归因分解
└── notebooks/
    └── risk_dashboard.ipynb    # 风险指标仪表盘
```

## 核心主题

- **市场风险**：VaR（历史法/参数法/蒙特卡洛）、CVaR、压力测试
- **回撤管理**：最大回撤、水下期、回撤恢复期
- **组合风险**：Beta 中性、因子暴露、风险平价
- **风控规则**：止损线、仓位限制、集中度控制

## 推荐资源

- 《Value at Risk》— Philippe Jorion
- 《风险管理与金融机构》— John Hull
- Python 库：`scipy`, `numpy`, `pandas`, `pyfolio`

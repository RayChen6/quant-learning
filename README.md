# 金融理论 | Financial Theory

现代金融理论核心框架，涵盖资产定价、衍生品定价、固定收益与风险理论。

## 学习路线

```
现代投资组合理论 → CAPM/APT → 衍生品定价 → 固定收益 → 行为金融
```

## 目录结构

```
financial-theory/
├── notes/
│   ├── 00_overview.md          # 知识点速览
│   ├── 01_capm_apt.md          # CAPM 与 APT
│   ├── 02_options.md           # 期权定价理论
│   └── 03_fixed_income.md      # 固定收益基础
├── code/
│   ├── black_scholes.py        # BS 公式与希腊字母
│   └── bond_pricing.py         # 债券定价与久期
└── notebooks/
    └── options_greeks.ipynb    # 期权希腊字母敏感性分析
```

## 核心主题

- **资产定价**：CAPM、Fama-French 三因子、APT
- **期权定价**：Black-Scholes、二叉树、蒙特卡洛
- **希腊字母**：Delta、Gamma、Theta、Vega、Rho
- **固定收益**：久期、凸性、收益率曲线、利率模型

## 推荐资源

- 《期权、期货及其他衍生品》— John Hull
- 《固定收益数学》— Fabozzi
- Python 库：`mibian`, `py_vollib`, `QuantLib-Python`

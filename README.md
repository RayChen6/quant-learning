# 数学与统计基础 | Math & Statistics

量化交易的数学地基，涵盖概率论、随机过程、统计推断与时间序列分析。

## 学习路线

```
线性代数 → 概率论 → 数理统计 → 随机过程 → 时间序列分析
```

## 目录结构

```
math-stats/
├── notes/
│   ├── 00_overview.md          # 知识点速览
│   ├── 01_probability.md       # 概率论基础
│   ├── 02_stochastic.md        # 随机过程与布朗运动
│   └── 03_time_series.md       # 时间序列分析
├── code/
│   ├── statistical_tests.py    # 常用统计检验
│   └── monte_carlo.py          # 蒙特卡洛模拟
└── notebooks/
    └── brownian_motion.ipynb   # 布朗运动可视化
```

## 核心主题

- **概率论**：大数定律、中心极限定理、条件期望
- **随机过程**：马尔可夫链、布朗运动、伊藤引理
- **统计检验**：ADF单位根检验、Johansen协整检验、正态性检验
- **时间序列**：AR/MA/ARIMA、GARCH波动率模型

## 推荐资源

- 《概率论与数理统计》— 陈希孺
- 《随机微分方程》— Øksendal
- [QuantLib 文档](https://www.quantlib.org/)
- Python 库：`numpy`, `scipy`, `statsmodels`

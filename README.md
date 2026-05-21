# 因子与 Alpha 研究 | Alpha Research

系统化因子挖掘与 Alpha 信号研究，从因子构建到有效性验证的完整流程。

## 学习路线

```
因子分类了解 → 因子计算 → IC 分析 → 分层回测 → 因子合成 → 因子衰减
```

## 目录结构

```
alpha-research/
├── notes/
│   ├── 00_overview.md          # 知识点速览
│   ├── 01_factor_types.md      # 因子分类与常见因子
│   └── 02_factor_evaluation.md # 因子评估方法
├── code/
│   ├── factor_calculator.py    # 常见因子计算
│   └── factor_analysis.py      # IC/IR 统计与分层回测
└── notebooks/
    └── single_factor_analysis.ipynb  # 单因子分析完整流程
```

## 核心主题

- **因子分类**：价值（P/E、P/B）、动量、质量、低波动、规模
- **因子评估**：IC、Rank IC、IR、因子换手率、因子衰减
- **分层回测**：五分组收益差异、多空组合
- **因子合成**：等权合成、IC 加权、机器学习合成

## 推荐资源

- 《Finding Alphas》— Igor Tulchinsky
- WorldQuant 101 Alpha 公式
- Python 库：`alphalens`, `pandas`, `numpy`

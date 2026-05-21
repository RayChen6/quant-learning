# 组合管理 | Portfolio Management

从单策略到组合层面的管理，涵盖组合优化、再平衡与绩效归因。

## 学习路线

```
MPT 基础 → 均值-方差优化 → 风险平价 → Black-Litterman → 再平衡 → 绩效归因
```

## 目录结构

```
portfolio-mgmt/
├── notes/
│   ├── 00_overview.md              # 知识点速览
│   ├── 01_optimization.md          # 组合优化方法
│   └── 02_performance_attribution.md  # 绩效归因
├── code/
│   ├── portfolio_optimizer.py      # 均值-方差与风险平价优化
│   └── rebalancing.py              # 再平衡策略实现
└── notebooks/
    └── efficient_frontier.ipynb    # 有效前沿可视化
```

## 核心主题

- **MPT**：均值-方差优化、有效前沿、夏普比率最大化
- **风险平价**：等风险贡献、全天候组合
- **Black-Litterman**：结合市场均衡与主观观点
- **再平衡**：定期再平衡、阈值触发、税务优化
- **绩效归因**：Brinson 模型、因子归因

## 推荐资源

- 《Active Portfolio Management》— Grinold & Kahn
- 《The Black-Litterman Model in Detail》— Idzorek
- Python 库：`PyPortfolioOpt`, `cvxpy`, `riskfolio-lib`

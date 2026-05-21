# Portfolio Management 组合管理

> 精选组合优化、资产配置、绩效归因相关的顶级开源项目与理论资源。

---

## 组合优化库

| 项目 | Stars量级 | 特点 |
|------|-----------|------|
| [dcajasn/Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) | ⭐ 4k+ | 最全面的 Python 组合优化库，20+ 优化模型，含风险平价/HRP/Black-Litterman |
| [skfolio/skfolio](https://github.com/skfolio/skfolio) | ⭐ 2k+ | scikit-learn 风格 API，与 sklearn Pipeline 无缝集成 |
| [cvxgrp/cvxportfolio](https://github.com/cvxgrp/cvxportfolio) | ⭐ 1k+ | Stanford Boyd 团队出品，凸优化框架，含多期优化 |
| [goldmansachs/gs-quant](https://github.com/goldmansachs/gs-quant) | ⭐ 3k+ | 高盛开源，含组合构建、风险分析、衍生品定价 |

## 核心优化模型

### 均值-方差优化 (Markowitz)
- 经典 MVO：最大化 Sharpe / 最小化方差
- 局限：对协方差矩阵估计极度敏感
- 改进：收缩估计 (Ledoit-Wolf)、鲁棒优化

### 风险平价 (Risk Parity)
- 等风险贡献 (ERC)：各资产贡献相同风险
- 层次风险平价 (HRP)：基于聚类的层次化分配
- 对参数估计更鲁棒，实践中广泛使用

### Black-Litterman 模型
- 结合市场均衡 + 主观观点
- 解决 MVO 对预期收益敏感的问题
- Riskfolio-Lib 和 skfolio 均有完整实现

### 因子模型约束优化
- 基于 Barra / PCA 因子的风险模型
- 因子暴露约束、行业中性化

## 绩效归因

| 方法 | 说明 |
|------|------|
| Brinson 归因 | 资产配置 + 个股选择 + 交互效应 |
| 因子归因 | Fama-French、Barra 因子暴露 |
| 风险归因 | 各资产/因子对组合总风险的贡献 |

## 再平衡策略

```python
# 常见再平衡触发条件
1. 日历再平衡：月度/季度定期调仓
2. 阈值再平衡：权重偏离目标超过 X% 时触发
3. 波动率目标：动态调整杠杆使组合波动率恒定
4. 成本感知再平衡：考虑交易成本的最优再平衡
```

## 实践注意事项

- **估计误差放大**：优化器会放大输入误差，样本外表现往往差于等权
- **换手率控制**：加入 L1/L2 惩罚项控制交易成本
- **流动性约束**：大资金需考虑市场冲击成本
- **因子拥挤**：流行因子在压力时期可能发生崩溃

## 关键论文

| 论文 | 要点 |
|------|------|
| Markowitz (1952) - Portfolio Selection | 现代组合理论奠基 |
| Black & Litterman (1992) | B-L 模型原始论文 |
| Maillard et al. (2010) - Properties of ERC Portfolio | 风险平价理论基础 |
| López de Prado (2016) - Building Diversified Portfolios that Outperform OOS | HRP 方法论 |

## 延伸资源

- [awesome-quant](https://github.com/wilsonfreitas/awesome-quant) — 包含组合优化工具分类
- [quant-wiki](https://github.com/LLMQuant/quant-wiki) — 组合管理知识库（中英文）

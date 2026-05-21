# Risk Management 风险管理

> 精选量化风险管理相关的开源工具、方法论与学习资源。

---

## 核心工具库

| 项目 | Stars量级 | 特点 |
|------|-----------|------|
| [dcajasn/Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) | ⭐ 4k+ | 组合风险优化库，含 CVaR/CDaR/EVaR 等风险度量 |
| [skfolio/skfolio](https://github.com/skfolio/skfolio) | ⭐ 2k+ | sklearn 风格，支持多种风险约束的组合优化 |
| [goldmansachs/gs-quant](https://github.com/goldmansachs/gs-quant) | ⭐ 3k+ | 高盛风险分析工具，含希腊值、情景分析 |
| [google/tf-quant-finance](https://github.com/google/tf-quant-finance) | ⭐ 4k+ | TensorFlow 实现随机过程、期权定价与风险计算 |
| [cantaro86/Financial-Models-Numerical-Methods](https://github.com/cantaro86/Financial-Models-Numerical-Methods) | ⭐ 3k+ | 含 VaR/CVaR、随机波动率模型的交互式 Notebook |

## 风险度量体系

### 市场风险

| 指标 | 说明 | 局限性 |
|------|------|--------|
| **VaR** (Value at Risk) | 置信水平下的最大损失估计 | 不满足次可加性，忽略尾部形状 |
| **CVaR / ES** | VaR 以外损失的期望值 | 更保守，监管 (Basel IV) 偏好 |
| **最大回撤 (MDD)** | 历史最大峰谷跌幅 | 路径依赖，直观易理解 |
| **Calmar Ratio** | 年化收益 / 最大回撤 | 评估回撤调整后收益 |
| **波动率** | 收益率标准差 | 对称，不区分上下行 |
| **下行偏差** | 仅计算负收益偏差 | Sortino Ratio 分母 |

### 希腊值风险（期权）

```
Delta  — 标的价格变化的敏感性
Gamma  — Delta 的变化率（凸性）
Vega   — 隐含波动率变化的敏感性
Theta  — 时间衰减
Rho    — 利率变化的敏感性
```

### 因子风险

- **系统性风险**：市场、行业、风格因子暴露
- **特质风险**：个股特有风险（可通过分散化降低）
- **因子拥挤风险**：多策略同向持仓在压力下的踩踏风险

## VaR 计算方法对比

```
1. 历史模拟法：直接用历史收益率分布
   优点：无参数假设；缺点：依赖历史样本

2. 方差-协方差法（参数法）：假设正态分布
   优点：计算快；缺点：低估尾部风险

3. 蒙特卡洛模拟：随机模拟大量路径
   优点：灵活，可处理非线性；缺点：计算量大

4. 极值理论 (EVT)：GEV/GPD 拟合尾部
   优点：最准确的尾部估计；缺点：参数估计困难
```

## 压力测试与情景分析

| 类型 | 说明 |
|------|------|
| 历史情景 | 2008年金融危机、2020年COVID崩盘、2022年利率冲击 |
| 假设情景 | 利率+100bps、股市-20%、波动率翻倍 |
| 反向压力测试 | 找出导致组合崩溃的情景 |
| 敏感性分析 | 单因子变化对组合 PnL 的影响 |

## 风险限额体系

```
组合级别：总 VaR / 最大回撤限额 / 杠杆上限
因子级别：单一因子最大暴露（如 Beta < 0.3）
个股级别：单一持仓权重上限（如 < 5%）
行业级别：单一行业敞口上限（如 < 20%）
流动性：持仓市值 / 日均成交额 < N 天
```

## 关键论文

| 论文 | 要点 |
|------|------|
| Artzner et al. (1999) - Coherent Risk Measures | CVaR/ES 的理论基础 |
| Rockafellar & Uryasev (2000) - CVaR Optimization | CVaR 可用线性规划求解 |
| Acharya et al. (2017) - Measuring Systemic Risk | 系统性风险度量 |

## 延伸资源

- [awesome-quant](https://github.com/wilsonfreitas/awesome-quant) — 含风险管理工具分类
- [quant-wiki](https://github.com/LLMQuant/quant-wiki) — 风险管理知识库（中英文）

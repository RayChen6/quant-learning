# 风险管理 — 核心知识点速览

## 1. VaR（Value at Risk）

**定义**：在置信水平 $\alpha$ 下，未来 T 天内最大可能损失。

$$P(Loss > VaR_\alpha) = 1 - \alpha$$

### 三种计算方法

| 方法 | 原理 | 优点 | 缺点 |
|------|------|------|------|
| 历史模拟法 | 用历史收益分布直接取分位数 | 无分布假设 | 依赖历史，尾部样本少 |
| 参数法 | 假设正态分布计算 | 简单快速 | 低估肥尾风险 |
| 蒙特卡洛 | 模拟大量场景取分位数 | 灵活精确 | 计算量大 |

**CVaR（条件VaR）**：超过 VaR 后的平均损失，比 VaR 更保守更合理。

---

## 2. 回撤分析

```python
def max_drawdown(returns: pd.Series) -> float:
    cum_returns = (1 + returns).cumprod()
    peak = cum_returns.cummax()
    drawdown = (cum_returns - peak) / peak
    return drawdown.min()  # 负数，最大回撤的绝对值取 abs()
```

**关键回撤指标**：
- 最大回撤（Max Drawdown）
- 平均回撤深度
- 水下期（Underwater Period）：回撤持续时间
- 恢复期（Recovery Time）：从谷底回到前高所需时间

---

## 3. 组合风险分解

**风险平价（Risk Parity）**：让每个资产对组合风险的贡献相等

$$RC_i = w_i \cdot \frac{\partial \sigma_p}{\partial w_i} = \frac{w_i (\Sigma w)_i}{\sigma_p}$$

**因子风险分解**：
$$\sigma_p^2 = \sum_i \sum_j w_i w_j \beta_i \beta_j \sigma_f^2 + \sum_i w_i^2 \sigma_{\epsilon_i}^2$$

---

## 4. 实用风控规则

```
单票仓位上限：  5~10%（防止集中风险）
行业暴露上限：  20~30%（防止行业黑天鹅）
总杠杆上限：    1~2x（股票多头通常不加杠杆）
日度止损线：    -2%（触发后降仓或停止交易）
最大回撤止损：  -15%（触发后策略熔断检查）
```

---

## 5. 常用风险监控代码

```python
import numpy as np
import pandas as pd

def historical_var(returns: pd.Series, confidence: float = 0.95) -> float:
    """历史模拟法 VaR（日度）"""
    return returns.quantile(1 - confidence)

def parametric_var(returns: pd.Series, confidence: float = 0.95) -> float:
    """参数法 VaR（假设正态分布）"""
    from scipy.stats import norm
    mu, sigma = returns.mean(), returns.std()
    return mu + sigma * norm.ppf(1 - confidence)
```

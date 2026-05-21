# 金融理论 — 核心知识点速览

## 1. 资产定价模型

### CAPM
$$E[R_i] = R_f + \beta_i (E[R_m] - R_f)$$

- $\beta_i = \frac{Cov(R_i, R_m)}{Var(R_m)}$：系统性风险度量
- Alpha = 实际收益 - CAPM 预测收益（超额收益）

### Fama-French 三因子
$$E[R_i] - R_f = \beta_1 \cdot MKT + \beta_2 \cdot SMB + \beta_3 \cdot HML$$

- **MKT**：市场超额收益
- **SMB**：小市值 - 大市值（规模因子）
- **HML**：高账面市值比 - 低账面市值比（价值因子）

---

## 2. 期权定价

### Black-Scholes 公式
$$C = S_0 N(d_1) - K e^{-rT} N(d_2)$$

$$d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}$$

### 希腊字母速查

| 希腊字母 | 含义 | 方向 |
|---------|------|------|
| Delta (Δ) | 期权价格对标的价格的偏导 | Call: 0~1, Put: -1~0 |
| Gamma (Γ) | Delta 对标的价格的偏导 | 永远为正 |
| Theta (Θ) | 时间流逝导致的价值损失 | 通常为负 |
| Vega (ν) | 对波动率的敏感性 | 永远为正 |
| Rho (ρ) | 对无风险利率的敏感性 | Call正, Put负 |

---

## 3. 固定收益

**债券价格**：
$$P = \sum_{t=1}^{T} \frac{C}{(1+y)^t} + \frac{F}{(1+y)^T}$$

**久期（Macaulay Duration）**：加权平均现金流时间  
**修正久期**：$D_{mod} = \frac{D_{mac}}{1+y}$，利率变动1%时价格变动约为 $D_{mod}$%  
**凸性**：对久期的二阶修正，凸性越大对投资者越有利

---

## 4. 核心公式速记

```python
import numpy as np
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
```

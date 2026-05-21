# 数学与统计基础 — 核心知识点速览

## 1. 概率论基础

| 概念 | 说明 |
|------|------|
| 期望 E[X] | 随机变量的加权平均 |
| 方差 Var[X] | 偏离均值的平方期望 |
| 协方差 Cov[X,Y] | 两变量联合变化程度 |
| 条件期望 E[X\|Y] | 给定Y后X的期望，是量化中最重要的工具之一 |

**大数定律**：样本均值依概率收敛于总体期望  
**中心极限定理**：n 足够大时，样本均值近似正态分布

---

## 2. 随机过程

### 布朗运动（Wiener Process）
- $W_0 = 0$
- 增量独立：$W_t - W_s \sim N(0, t-s)$
- 路径连续但处处不可微

### 伊藤引理
若 $f(t, S_t)$ 是二阶可微函数，$S_t$ 满足 SDE，则：
$$df = \frac{\partial f}{\partial t}dt + \frac{\partial f}{\partial S}dS + \frac{1}{2}\frac{\partial^2 f}{\partial S^2}(dS)^2$$

### 几何布朗运动（GBM）
$$dS_t = \mu S_t dt + \sigma S_t dW_t$$
股票价格的常用建模方式。

---

## 3. 统计检验

| 检验 | 用途 | Python |
|------|------|--------|
| ADF 检验 | 时间序列平稳性 | `statsmodels.tsa.stattools.adfuller` |
| Johansen 检验 | 多变量协整关系 | `statsmodels.tsa.vector_ar.vecm` |
| Jarque-Bera | 正态性检验 | `scipy.stats.jarque_bera` |
| Ljung-Box | 自相关检验 | `statsmodels.stats.diagnostic` |

---

## 4. 时间序列模型

```
AR(p)   → 自回归，依赖过去p期自身
MA(q)   → 移动平均，依赖过去q期误差
ARMA    → AR + MA 组合
ARIMA   → 差分后的 ARMA（处理非平稳序列）
GARCH   → 波动率聚集建模，金融中极常用
```

**GARCH(1,1)**：
$$\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2$$

---

## 5. 常用 Python 工具

```python
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller, coint

# ADF 平稳性检验
result = adfuller(price_series)
print(f"ADF Statistic: {result[0]:.4f}, p-value: {result[1]:.4f}")

# 协整检验
score, pvalue, _ = coint(series1, series2)
```

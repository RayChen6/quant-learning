# 组合管理 — 核心知识点速览

## 1. 现代投资组合理论（MPT）

**期望收益**：$E[R_p] = \sum_i w_i E[R_i]$

**组合方差**：$\sigma_p^2 = \mathbf{w}^T \Sigma \mathbf{w}$

**有效前沿**：在给定风险下收益最大，或给定收益下风险最小的组合集合。

### 最大 Sharpe 组合（切点组合）
$$\max_w \frac{E[R_p] - R_f}{\sigma_p} \quad \text{s.t.} \sum w_i = 1$$

---

## 2. 主要优化方法对比

| 方法 | 目标 | 优点 | 缺点 |
|------|------|------|------|
| 均值-方差 | 最大Sharpe | 理论完备 | 对预期收益估计极敏感 |
| 最小方差 | 最小风险 | 不需要预期收益 | 过度集中于低波动资产 |
| 风险平价 | 等风险贡献 | 分散化好 | 忽略收益预测 |
| Black-Litterman | 结合观点 | 稳定，融合主观判断 | 实现复杂 |

---

## 3. 风险平价（Risk Parity）

每个资产的**风险贡献**相等：

$$RC_i = w_i \cdot (\Sigma w)_i / \sigma_p = \sigma_p / N \quad \forall i$$

```python
from scipy.optimize import minimize
import numpy as np

def risk_parity_weights(cov_matrix: np.ndarray) -> np.ndarray:
    n = cov_matrix.shape[0]
    def objective(w):
        sigma = np.sqrt(w @ cov_matrix @ w)
        rc = w * (cov_matrix @ w) / sigma
        return np.sum((rc - sigma/n)**2)  # 风险贡献差异最小化

    result = minimize(objective, x0=np.ones(n)/n,
                      constraints={'type': 'eq', 'fun': lambda w: w.sum()-1},
                      bounds=[(0, 1)]*n)
    return result.x
```

---

## 4. 再平衡策略

| 策略 | 触发条件 | 适用场景 |
|------|---------|---------|
| 定期再平衡 | 每月/季度 | 简单，换手率可控 |
| 阈值再平衡 | 权重偏离 >5% | 减少不必要交易 |
| 混合 | 定期检查+阈值触发 | 推荐方式 |

---

## 5. 绩效归因（Brinson 模型）

$$\text{超额收益} = \text{配置效应} + \text{选股效应} + \text{交互效应}$$

- **配置效应**：行业/资产类别的权重偏离基准
- **选股效应**：在同一类别内选择了更好的标的
- **交互效应**：配置与选股的联合效果

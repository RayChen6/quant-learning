# 回测框架 — 核心知识点速览

## 1. 回测偏差汇总

| 偏差类型 | 说明 | 如何避免 |
|---------|------|---------|
| 前视偏差 | 使用了未来数据 | 严格按时间序列处理，财务数据用披露日 |
| 幸存者偏差 | 只含现存标的 | 使用含退市股的历史股票池 |
| 过拟合 | 参数过度优化 | Walk-forward 验证，控制自由度 |
| 交易成本忽略 | 未考虑手续费/滑点 | 加入真实交易成本模型 |
| 流动性假设 | 假设任意价格成交 | 考虑成交量限制，使用 VWAP 成交 |

---

## 2. 绩效指标速查

$$\text{Sharpe} = \frac{R_p - R_f}{\sigma_p} \times \sqrt{252}$$

$$\text{Sortino} = \frac{R_p - R_f}{\sigma_{down}} \times \sqrt{252}$$

$$\text{最大回撤} = \max_{t} \left(\frac{\text{Peak}_t - P_t}{\text{Peak}_t}\right)$$

$$\text{Calmar} = \frac{\text{年化收益}}{\text{最大回撤}}$$

| 指标 | 优秀 | 良好 | 一般 |
|------|------|------|------|
| Sharpe | >2 | 1~2 | 0.5~1 |
| 最大回撤 | <10% | 10~20% | 20~40% |
| Calmar | >2 | 1~2 | <1 |

---

## 3. 两种回测框架对比

### 向量化回测（Vectorized）
- 用 pandas/numpy 对整个时间序列批量计算
- 速度极快，适合参数扫描
- 缺点：难以精确模拟订单撮合、持仓限制

### 事件驱动回测（Event-driven）
- 模拟真实交易流程：数据事件→信号→下单→成交→更新持仓
- 精度高，可接近实盘
- 缺点：速度慢，实现复杂

---

## 4. 向量化回测核心代码

```python
import pandas as pd
import numpy as np

def vectorized_backtest(prices: pd.Series, signals: pd.Series,
                        commission: float = 0.001) -> dict:
    """
    prices:  收盘价序列
    signals: 仓位信号 (+1 多头, 0 空仓, -1 空头)
    """
    returns = prices.pct_change()
    # 信号延迟一期（避免前视偏差）
    position = signals.shift(1)
    # 策略收益
    strat_returns = position * returns
    # 扣除手续费（换手时）
    turnover = position.diff().abs()
    strat_returns -= turnover * commission

    total_return = (1 + strat_returns).prod() - 1
    ann_return = (1 + total_return) ** (252 / len(returns)) - 1
    sharpe = strat_returns.mean() / strat_returns.std() * np.sqrt(252)
    cum = (1 + strat_returns).cumprod()
    max_dd = (cum / cum.cummax() - 1).min()

    return {"annual_return": ann_return, "sharpe": sharpe, "max_drawdown": max_dd}
```

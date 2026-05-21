# 执行与交易系统 — 核心知识点速览

## 1. 市场微观结构

### 订单类型
| 订单类型 | 说明 | 优缺点 |
|---------|------|--------|
| 市价单（Market Order）| 立即以最优价成交 | 确保成交，但有滑点 |
| 限价单（Limit Order）| 指定价格或更优 | 控制成本，但可能不成交 |
| 止损单（Stop Order）| 触发价后变市价单 | 风控用途 |
| 冰山单（Iceberg）| 只显示部分数量 | 隐藏大单 |

### 买卖价差（Bid-Ask Spread）
$$\text{Spread} = Ask - Bid$$
$$\text{有效价差} = 2 \times |P_{trade} - M|，\quad M = \frac{Ask + Bid}{2}$$

---

## 2. 算法执行策略

### TWAP（时间加权平均价格）
- 将订单均匀分散到时间段内执行
- 简单易实现，适合流动性稳定的市场

### VWAP（成交量加权平均价格）
- 按历史成交量分布调整执行节奏
- 流动性高时多执行，低时少执行
- 目标：成交均价接近当日 VWAP

### IS（Implementation Shortfall）
- 最小化决策价格与实际成交均价的差距
- 考虑时机成本与冲击成本的权衡

---

## 3. 交易成本分析

$$\text{总成本} = \text{佣金} + \text{滑点} + \text{市场冲击} + \text{时机成本}$$

**市场冲击估算（平方根模型）**：
$$MI = \sigma \cdot \sqrt{\frac{Q}{ADV}}$$

- $\sigma$：日波动率
- $Q$：交易数量
- $ADV$：日均成交量

---

## 4. 简单 OMS 状态机

```
订单生命周期：
New → Pending → Partially Filled → Filled
                                 → Cancelled
                                 → Rejected
```

```python
from enum import Enum

class OrderStatus(Enum):
    NEW = "new"
    PENDING = "pending"
    PARTIAL = "partial"
    FILLED = "filled"
    CANCELLED = "cancelled"
    REJECTED = "rejected"

class Order:
    def __init__(self, symbol, qty, direction, order_type="market"):
        self.symbol = symbol
        self.qty = qty
        self.direction = direction  # "buy" or "sell"
        self.order_type = order_type
        self.status = OrderStatus.NEW
        self.filled_qty = 0
        self.avg_price = 0.0
```

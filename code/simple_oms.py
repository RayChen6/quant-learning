"""
简单订单管理系统（OMS）
涵盖订单生命周期管理与交易成本分析
"""
import uuid
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import numpy as np
import pandas as pd


class OrderStatus(Enum):
    NEW = "new"
    PENDING = "pending"
    PARTIAL = "partial"
    FILLED = "filled"
    CANCELLED = "cancelled"
    REJECTED = "rejected"


class OrderType(Enum):
    MARKET = "market"
    LIMIT = "limit"


class Direction(Enum):
    BUY = "buy"
    SELL = "sell"


@dataclass
class Order:
    symbol: str
    direction: Direction
    qty: float
    order_type: OrderType = OrderType.MARKET
    limit_price: Optional[float] = None
    order_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    status: OrderStatus = OrderStatus.NEW
    filled_qty: float = 0.0
    avg_fill_price: float = 0.0
    created_at: datetime = field(default_factory=datetime.now)
    filled_at: Optional[datetime] = None
    commission: float = 0.0

    def fill(self, qty: float, price: float, commission_rate: float = 0.001):
        self.filled_qty += qty
        # 更新成交均价
        total_cost = self.avg_fill_price * (self.filled_qty - qty) + price * qty
        self.avg_fill_price = total_cost / self.filled_qty
        self.commission += qty * price * commission_rate
        self.filled_at = datetime.now()
        if self.filled_qty >= self.qty:
            self.status = OrderStatus.FILLED
        else:
            self.status = OrderStatus.PARTIAL

    @property
    def slippage(self) -> float:
        if self.limit_price and self.avg_fill_price:
            return abs(self.avg_fill_price - self.limit_price) / self.limit_price
        return 0.0

    def __repr__(self):
        return (f"Order({self.order_id} | {self.symbol} "
                f"{self.direction.value} {self.qty} | "
                f"{self.status.value} @ {self.avg_fill_price:.2f})")


class SimpleOMS:
    """简单订单管理系统"""

    def __init__(self, commission_rate: float = 0.001,
                 slippage_rate: float = 0.0005):
        self.orders: dict[str, Order] = {}
        self.positions: dict[str, float] = {}
        self.commission_rate = commission_rate
        self.slippage_rate = slippage_rate
        self.trade_log: list[dict] = []

    def submit(self, order: Order) -> str:
        """提交订单，返回 order_id"""
        order.status = OrderStatus.PENDING
        self.orders[order.order_id] = order
        print(f"[OMS] 订单提交: {order}")
        return order.order_id

    def simulate_fill(self, order_id: str, market_price: float) -> bool:
        """模拟撮合成交"""
        order = self.orders.get(order_id)
        if not order or order.status in (OrderStatus.FILLED, OrderStatus.CANCELLED):
            return False

        # 滑点模拟
        if order.direction == Direction.BUY:
            fill_price = market_price * (1 + self.slippage_rate)
        else:
            fill_price = market_price * (1 - self.slippage_rate)

        # 限价单检查
        if order.order_type == OrderType.LIMIT:
            if order.direction == Direction.BUY and fill_price > order.limit_price:
                return False
            if order.direction == Direction.SELL and fill_price < order.limit_price:
                return False

        order.fill(order.qty, fill_price, self.commission_rate)

        # 更新持仓
        sign = 1 if order.direction == Direction.BUY else -1
        self.positions[order.symbol] = (
            self.positions.get(order.symbol, 0) + sign * order.filled_qty
        )

        self.trade_log.append({
            "order_id": order_id, "symbol": order.symbol,
            "direction": order.direction.value,
            "qty": order.filled_qty, "price": fill_price,
            "commission": order.commission, "time": order.filled_at,
        })
        print(f"[OMS] 成交确认: {order}")
        return True

    def cancel(self, order_id: str) -> bool:
        order = self.orders.get(order_id)
        if order and order.status == OrderStatus.PENDING:
            order.status = OrderStatus.CANCELLED
            print(f"[OMS] 订单取消: {order_id}")
            return True
        return False

    def portfolio_summary(self) -> pd.DataFrame:
        """持仓汇总"""
        return pd.DataFrame([
            {"symbol": k, "position": v}
            for k, v in self.positions.items()
        ])

    def transaction_cost_report(self) -> dict:
        """交易成本报告"""
        df = pd.DataFrame(self.trade_log)
        if df.empty:
            return {}
        total_commission = df["commission"].sum()
        total_notional = (df["qty"] * df["price"]).sum()
        return {
            "总成交笔数": len(df),
            "总成交金额": f"{total_notional:,.0f}",
            "总手续费":   f"{total_commission:,.2f}",
            "手续费率":   f"{total_commission/total_notional:.4%}",
        }


if __name__ == "__main__":
    oms = SimpleOMS(commission_rate=0.001, slippage_rate=0.0005)

    # 下单
    o1 = Order("000001", Direction.BUY, 1000, OrderType.MARKET)
    o2 = Order("600036", Direction.BUY, 500, OrderType.LIMIT, limit_price=45.0)

    oms.submit(o1)
    oms.submit(o2)

    # 模拟市场价格推送
    print("\n--- 行情推送 ---")
    oms.simulate_fill(o1.order_id, market_price=15.32)
    oms.simulate_fill(o2.order_id, market_price=44.80)  # 低于限价，成交

    print("\n--- 持仓汇总 ---")
    print(oms.portfolio_summary())
    print("\n--- 交易成本报告 ---")
    for k, v in oms.transaction_cost_report().items():
        print(f"  {k}: {v}")

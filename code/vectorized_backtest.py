"""
向量化回测框架
支持多资产、手续费、仓位限制与完整绩效报告
"""
import numpy as np
import pandas as pd
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class BacktestResult:
    equity_curve: pd.Series
    returns: pd.Series
    positions: pd.Series
    annual_return: float
    volatility: float
    sharpe: float
    sortino: float
    max_drawdown: float
    calmar: float
    win_rate: float
    total_trades: int


def performance_metrics(returns: pd.Series,
                        risk_free: float = 0.02) -> dict:
    """计算完整绩效指标"""
    equity = (1 + returns).cumprod()
    ann_ret = equity.iloc[-1] ** (252 / len(returns)) - 1
    vol = returns.std() * np.sqrt(252)
    sharpe = (ann_ret - risk_free) / vol if vol > 0 else 0

    downside = returns[returns < 0].std() * np.sqrt(252)
    sortino = (ann_ret - risk_free) / downside if downside > 0 else 0

    drawdown = equity / equity.cummax() - 1
    max_dd = drawdown.min()
    calmar = ann_ret / abs(max_dd) if max_dd != 0 else 0

    return {
        "年化收益":  f"{ann_ret:.2%}",
        "年化波动率": f"{vol:.2%}",
        "Sharpe":    f"{sharpe:.2f}",
        "Sortino":   f"{sortino:.2f}",
        "最大回撤":  f"{max_dd:.2%}",
        "Calmar":    f"{calmar:.2f}",
        "胜率":      f"{(returns > 0).mean():.2%}",
    }


def run_backtest(prices: pd.Series,
                 signals: pd.Series,
                 commission: float = 0.001,
                 slippage: float = 0.0005,
                 max_position: float = 1.0,
                 risk_free: float = 0.02) -> BacktestResult:
    """
    执行向量化回测

    参数:
        prices:       收盘价
        signals:      仓位信号 [−1, 1]
        commission:   单边手续费率
        slippage:     滑点率（单边）
        max_position: 最大仓位（1.0=满仓）
    """
    # 信号延迟一期，模拟次日开盘执行
    pos = signals.clip(-max_position, max_position).shift(1).fillna(0)

    returns = prices.pct_change()

    # 策略收益
    strat_ret = pos * returns

    # 交易成本（换手时双边扣除）
    turnover = pos.diff().abs()
    cost = turnover * (commission + slippage)
    strat_ret -= cost

    equity = (1 + strat_ret).cumprod()
    ann_ret = equity.iloc[-1] ** (252 / len(strat_ret)) - 1
    vol = strat_ret.std() * np.sqrt(252)
    sharpe = (ann_ret - risk_free) / vol if vol > 0 else 0
    downside = strat_ret[strat_ret < 0].std() * np.sqrt(252)
    sortino = (ann_ret - risk_free) / downside if downside > 0 else 0
    drawdown = equity / equity.cummax() - 1
    max_dd = drawdown.min()

    n_trades = int((turnover > 0).sum())

    return BacktestResult(
        equity_curve=equity,
        returns=strat_ret,
        positions=pos,
        annual_return=ann_ret,
        volatility=vol,
        sharpe=sharpe,
        sortino=sortino,
        max_drawdown=max_dd,
        calmar=ann_ret / abs(max_dd) if max_dd != 0 else 0,
        win_rate=(strat_ret > 0).mean(),
        total_trades=n_trades,
    )


def print_report(result: BacktestResult) -> None:
    """打印回测报告"""
    print("=" * 40)
    print("        回测绩效报告")
    print("=" * 40)
    print(f"  年化收益率:  {result.annual_return:.2%}")
    print(f"  年化波动率:  {result.volatility:.2%}")
    print(f"  Sharpe 比率: {result.sharpe:.2f}")
    print(f"  Sortino:     {result.sortino:.2f}")
    print(f"  最大回撤:    {result.max_drawdown:.2%}")
    print(f"  Calmar 比率: {result.calmar:.2f}")
    print(f"  胜率:        {result.win_rate:.2%}")
    print(f"  总交易次数:  {result.total_trades}")
    print("=" * 40)


if __name__ == "__main__":
    np.random.seed(42)
    n = 500
    prices = pd.Series(
        100 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))),
        index=pd.bdate_range("2022-01-01", periods=n)
    )

    # 简单动量信号：过去20日收益为正则做多
    signals = pd.Series(
        np.where(prices.pct_change(20) > 0, 1.0, 0.0),
        index=prices.index
    )

    result = run_backtest(prices, signals, commission=0.001, slippage=0.0005)
    print_report(result)

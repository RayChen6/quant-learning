"""
双均线趋势跟踪策略
快线上穿慢线做多，下穿做空（或平仓）
"""
import numpy as np
import pandas as pd


def generate_signals(prices: pd.Series, fast: int = 10,
                     slow: int = 30) -> pd.Series:
    """
    生成双均线信号
    返回: +1（多头）, 0（空仓）, -1（空头）
    """
    ma_fast = prices.rolling(fast).mean()
    ma_slow = prices.rolling(slow).mean()

    signal = pd.Series(0, index=prices.index)
    signal[ma_fast > ma_slow] = 1
    signal[ma_fast < ma_slow] = -1

    # 去除均线未成熟期
    signal.iloc[:slow] = 0
    return signal


def backtest(prices: pd.Series, signals: pd.Series,
             commission: float = 0.001,
             long_only: bool = True) -> pd.DataFrame:
    """
    简单向量化回测
    commission: 单边手续费率
    long_only:  True 则空头信号改为空仓
    """
    pos = signals.shift(1).fillna(0)  # 延迟一期执行
    if long_only:
        pos = pos.clip(lower=0)

    returns = prices.pct_change()
    strat_ret = pos * returns

    # 换手成本
    turnover = pos.diff().abs()
    strat_ret -= turnover * commission

    equity = (1 + strat_ret).cumprod()
    bh_equity = (1 + returns).cumprod()

    # 绩效统计
    ann_ret = (equity.iloc[-1] ** (252 / len(equity)) - 1)
    vol = strat_ret.std() * np.sqrt(252)
    sharpe = ann_ret / vol if vol > 0 else 0
    drawdown = (equity / equity.cummax() - 1)
    max_dd = drawdown.min()

    print(f"策略年化收益: {ann_ret:.2%}")
    print(f"年化波动率:   {vol:.2%}")
    print(f"Sharpe 比率:  {sharpe:.2f}")
    print(f"最大回撤:     {max_dd:.2%}")
    print(f"买入持有收益: {(bh_equity.iloc[-1] - 1):.2%}")

    return pd.DataFrame({
        "price": prices,
        "signal": signals,
        "position": pos,
        "strategy": equity,
        "buy_hold": bh_equity,
        "drawdown": drawdown,
    })


def parameter_scan(prices: pd.Series,
                   fast_range: range = range(5, 30, 5),
                   slow_range: range = range(20, 100, 10)) -> pd.DataFrame:
    """参数扫描：寻找最优均线组合"""
    results = []
    for fast in fast_range:
        for slow in slow_range:
            if fast >= slow:
                continue
            sig = generate_signals(prices, fast, slow)
            pos = sig.shift(1).fillna(0).clip(lower=0)
            ret = pos * prices.pct_change()
            ann = (1 + ret).prod() ** (252 / len(ret)) - 1
            sharpe = ann / (ret.std() * np.sqrt(252) + 1e-8)
            results.append({"fast": fast, "slow": slow,
                            "ann_return": ann, "sharpe": sharpe})

    df = pd.DataFrame(results).sort_values("sharpe", ascending=False)
    print(f"\n最优参数: fast={df.iloc[0]['fast']}, slow={df.iloc[0]['slow']}, "
          f"Sharpe={df.iloc[0]['sharpe']:.2f}")
    return df


if __name__ == "__main__":
    np.random.seed(42)
    # 模拟价格（带趋势）
    n = 500
    trend = np.linspace(0, 0.5, n)
    noise = np.cumsum(np.random.normal(0, 0.015, n))
    prices = pd.Series(100 * np.exp(trend + noise),
                       index=pd.bdate_range("2022-01-01", periods=n))

    signals = generate_signals(prices, fast=10, slow=30)
    result = backtest(prices, signals, commission=0.001, long_only=True)

    print("\n--- 参数扫描 ---")
    scan = parameter_scan(prices)
    print(scan.head(5).to_string(index=False))

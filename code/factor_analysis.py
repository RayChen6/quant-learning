"""
因子有效性分析：IC 统计 + 分层回测
"""
import numpy as np
import pandas as pd
from scipy import stats


def compute_ic(factor: pd.Series, forward_returns: pd.Series,
               method: str = "rank") -> float:
    """
    计算单期 IC
    method: "rank" (Rank IC / Spearman) 或 "pearson"
    """
    aligned = pd.concat([factor, forward_returns], axis=1).dropna()
    if len(aligned) < 10:
        return np.nan
    f, r = aligned.iloc[:, 0], aligned.iloc[:, 1]
    if method == "rank":
        return stats.spearmanr(f, r)[0]
    return stats.pearsonr(f, r)[0]


def ic_analysis(factor_panel: pd.DataFrame,
                returns_panel: pd.DataFrame,
                method: str = "rank") -> pd.DataFrame:
    """
    多期 IC 分析
    factor_panel:  index=date, columns=stock
    returns_panel: index=date, columns=stock（下期收益）
    """
    dates = factor_panel.index.intersection(returns_panel.index)
    ic_series = pd.Series(index=dates, dtype=float)
    for date in dates:
        ic_series[date] = compute_ic(
            factor_panel.loc[date], returns_panel.loc[date], method
        )
    summary = {
        "IC Mean":    ic_series.mean(),
        "IC Std":     ic_series.std(),
        "IR":         ic_series.mean() / ic_series.std() if ic_series.std() > 0 else np.nan,
        "IC>0 比例":  (ic_series > 0).mean(),
        "|IC|>0.02 比例": (ic_series.abs() > 0.02).mean(),
    }
    print("\n📊 IC 分析结果:")
    for k, v in summary.items():
        print(f"  {k}: {v:.4f}")
    return ic_series


def quantile_backtest(factor_panel: pd.DataFrame,
                      returns_panel: pd.DataFrame,
                      n_groups: int = 5) -> pd.DataFrame:
    """
    分层回测：按因子值分组，计算各组平均收益
    返回每组的累计收益序列
    """
    dates = factor_panel.index.intersection(returns_panel.index)
    group_returns = {f"Q{i+1}": [] for i in range(n_groups)}

    for date in dates:
        f = factor_panel.loc[date].dropna()
        r = returns_panel.loc[date].reindex(f.index).dropna()
        f = f.reindex(r.index)
        if len(f) < n_groups * 2:
            continue
        quantiles = pd.qcut(f, n_groups, labels=[f"Q{i+1}" for i in range(n_groups)])
        for g in group_returns:
            mask = quantiles == g
            group_returns[g].append(r[mask].mean())

    result = pd.DataFrame(group_returns, index=dates[:len(group_returns["Q1"])])
    cum_result = (1 + result).cumprod()

    # 多空组合
    cum_result["L-S"] = cum_result[f"Q{n_groups}"] / cum_result["Q1"]

    ann_ret = result.mean() * 252
    print("\n📊 分层回测年化收益:")
    for col in result.columns:
        print(f"  {col}: {ann_ret[col]:.2%}")
    return cum_result


def process_factor(factor: pd.Series) -> pd.Series:
    """因子标准化处理：去极值 → 标准化"""
    median = factor.median()
    mad = (factor - median).abs().median()
    factor = factor.clip(median - 3 * 1.4826 * mad, median + 3 * 1.4826 * mad)
    factor = (factor - factor.mean()) / factor.std()
    return factor


if __name__ == "__main__":
    np.random.seed(42)
    n_dates, n_stocks = 100, 50
    dates = pd.date_range("2023-01-01", periods=n_dates, freq="B")
    stocks = [f"S{i:03d}" for i in range(n_stocks)]

    # 模拟因子（与收益有弱正相关）
    true_alpha = np.random.randn(n_dates, n_stocks)
    noise = np.random.randn(n_dates, n_stocks)
    factor_panel = pd.DataFrame(true_alpha, index=dates, columns=stocks)
    returns_panel = pd.DataFrame(0.1 * true_alpha + 0.9 * noise,
                                 index=dates, columns=stocks)

    ic_series = ic_analysis(factor_panel, returns_panel)
    cum_returns = quantile_backtest(factor_panel, returns_panel)
    print(f"\n多空组合最终收益: {cum_returns['L-S'].iloc[-1]:.4f}x")

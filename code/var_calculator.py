"""
VaR 与 CVaR 计算器
支持：历史模拟法 / 参数法 / 蒙特卡洛法
"""
import numpy as np
import pandas as pd
from scipy import stats
from dataclasses import dataclass


@dataclass
class RiskMetrics:
    var_hist: float
    var_param: float
    var_mc: float
    cvar_hist: float
    cvar_param: float
    confidence: float
    horizon: int


def historical_var(returns: pd.Series, confidence: float = 0.95,
                   horizon: int = 1) -> tuple[float, float]:
    """
    历史模拟法 VaR 和 CVaR
    返回: (VaR, CVaR) 均为正数（损失额）
    """
    scaled = returns * np.sqrt(horizon)
    var = -scaled.quantile(1 - confidence)
    cvar = -scaled[scaled <= -var].mean()
    return var, cvar


def parametric_var(returns: pd.Series, confidence: float = 0.95,
                   horizon: int = 1) -> tuple[float, float]:
    """
    参数法 VaR（正态分布假设）
    """
    mu = returns.mean() * horizon
    sigma = returns.std() * np.sqrt(horizon)
    z = stats.norm.ppf(1 - confidence)
    var = -(mu + z * sigma)
    # CVaR（正态分布下的解析解）
    cvar = -(mu - sigma * stats.norm.pdf(z) / (1 - confidence))
    return var, cvar


def monte_carlo_var(returns: pd.Series, confidence: float = 0.95,
                    horizon: int = 1, n_sim: int = 50000) -> tuple[float, float]:
    """
    蒙特卡洛法 VaR（正态分布模拟）
    """
    mu = returns.mean() * horizon
    sigma = returns.std() * np.sqrt(horizon)
    simulated = np.random.normal(mu, sigma, n_sim)
    var = -np.percentile(simulated, (1 - confidence) * 100)
    cvar = -simulated[simulated <= -var].mean()
    return var, cvar


def compute_all_var(returns: pd.Series, confidence: float = 0.95,
                    horizon: int = 1) -> RiskMetrics:
    """一次性计算三种方法的 VaR"""
    var_h, cvar_h = historical_var(returns, confidence, horizon)
    var_p, cvar_p = parametric_var(returns, confidence, horizon)
    var_m, _ = monte_carlo_var(returns, confidence, horizon)

    metrics = RiskMetrics(
        var_hist=var_h, var_param=var_p, var_mc=var_m,
        cvar_hist=cvar_h, cvar_param=cvar_p,
        confidence=confidence, horizon=horizon
    )
    print(f"\n📊 VaR 报告 (置信度={confidence:.0%}, 期限={horizon}天)")
    print(f"  历史模拟 VaR:  {var_h:.4f} ({var_h*100:.2f}%)")
    print(f"  参数法   VaR:  {var_p:.4f} ({var_p*100:.2f}%)")
    print(f"  蒙特卡洛 VaR:  {var_m:.4f} ({var_m*100:.2f}%)")
    print(f"  历史模拟 CVaR: {cvar_h:.4f} ({cvar_h*100:.2f}%)")
    return metrics


def max_drawdown_analysis(equity: pd.Series) -> dict:
    """回撤分析"""
    peak = equity.cummax()
    drawdown = (equity - peak) / peak
    max_dd = drawdown.min()
    max_dd_end = drawdown.idxmin()
    max_dd_start = equity[:max_dd_end].idxmax()

    # 恢复期
    post_trough = equity[max_dd_end:]
    recovered = post_trough[post_trough >= peak[max_dd_end]]
    recovery_date = recovered.index[0] if len(recovered) > 0 else None

    result = {
        "最大回撤":   f"{max_dd:.2%}",
        "回撤开始":   str(max_dd_start.date()),
        "回撤谷底":   str(max_dd_end.date()),
        "水下期(天)": (max_dd_end - max_dd_start).days,
        "已恢复":     recovery_date is not None,
    }
    for k, v in result.items():
        print(f"  {k}: {v}")
    return result


if __name__ == "__main__":
    np.random.seed(42)
    returns = pd.Series(np.random.normal(0.0005, 0.015, 500))

    metrics = compute_all_var(returns, confidence=0.95, horizon=1)
    metrics_99 = compute_all_var(returns, confidence=0.99, horizon=10)

    print("\n📊 回撤分析:")
    equity = (1 + returns).cumprod()
    max_drawdown_analysis(equity)

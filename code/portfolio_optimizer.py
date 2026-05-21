"""
组合优化器
支持：均值-方差（最大Sharpe）/ 最小方差 / 风险平价
"""
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from dataclasses import dataclass


@dataclass
class OptimizationResult:
    weights: pd.Series
    expected_return: float
    volatility: float
    sharpe: float
    method: str


def max_sharpe(returns: pd.DataFrame,
               risk_free: float = 0.02 / 252) -> OptimizationResult:
    """最大夏普比率组合"""
    mu = returns.mean()
    cov = returns.cov()
    n = len(mu)

    def neg_sharpe(w):
        w = np.array(w)
        ret = w @ mu.values
        vol = np.sqrt(w @ cov.values @ w)
        return -(ret - risk_free) / (vol + 1e-8)

    constraints = [{"type": "eq", "fun": lambda w: np.sum(w) - 1}]
    bounds = [(0, 1)] * n
    result = minimize(neg_sharpe, x0=np.ones(n) / n,
                      bounds=bounds, constraints=constraints,
                      method="SLSQP")
    w = pd.Series(result.x, index=returns.columns)
    ret = float(w @ mu) * 252
    vol = float(np.sqrt(w @ cov @ w)) * np.sqrt(252)
    return OptimizationResult(w, ret, vol, (ret - risk_free * 252) / vol, "Max Sharpe")


def min_variance(returns: pd.DataFrame) -> OptimizationResult:
    """最小方差组合"""
    mu = returns.mean()
    cov = returns.cov()
    n = len(mu)

    def portfolio_vol(w):
        return np.sqrt(np.array(w) @ cov.values @ np.array(w))

    constraints = [{"type": "eq", "fun": lambda w: np.sum(w) - 1}]
    bounds = [(0, 1)] * n
    result = minimize(portfolio_vol, x0=np.ones(n) / n,
                      bounds=bounds, constraints=constraints)
    w = pd.Series(result.x, index=returns.columns)
    ret = float(w @ mu) * 252
    vol = result.fun * np.sqrt(252)
    rf = 0.02
    return OptimizationResult(w, ret, vol, (ret - rf) / vol, "Min Variance")


def risk_parity(returns: pd.DataFrame) -> OptimizationResult:
    """风险平价组合（等风险贡献）"""
    mu = returns.mean()
    cov = returns.cov().values
    n = cov.shape[0]
    target_rc = 1.0 / n  # 目标风险贡献

    def objective(w):
        w = np.array(w)
        sigma = np.sqrt(w @ cov @ w)
        rc = w * (cov @ w) / sigma
        return np.sum((rc / sigma - target_rc) ** 2)

    constraints = [{"type": "eq", "fun": lambda w: np.sum(w) - 1}]
    bounds = [(0.001, 1)] * n
    result = minimize(objective, x0=np.ones(n) / n,
                      bounds=bounds, constraints=constraints,
                      method="SLSQP", options={"maxiter": 1000})
    w = pd.Series(result.x, index=returns.columns)
    ret = float(w @ mu) * 252
    vol = float(np.sqrt(w @ cov @ w)) * np.sqrt(252)
    rf = 0.02
    return OptimizationResult(w, ret, vol, (ret - rf) / vol, "Risk Parity")


def print_result(res: OptimizationResult) -> None:
    print(f"\n{'='*40}")
    print(f"  优化方法: {res.method}")
    print(f"  年化收益: {res.expected_return:.2%}")
    print(f"  年化波动: {res.volatility:.2%}")
    print(f"  Sharpe:   {res.sharpe:.2f}")
    print(f"  权重分配:")
    for asset, w in res.weights.items():
        print(f"    {asset}: {w:.2%}")


if __name__ == "__main__":
    np.random.seed(42)
    n_days, n_assets = 500, 5
    assets = ["沪深300", "中证500", "国债ETF", "黄金ETF", "原油ETF"]

    # 模拟资产收益（不同相关性）
    cov_true = np.array([
        [0.0004, 0.0003, -0.00005, 0.00002, 0.00001],
        [0.0003, 0.0006, -0.00003, 0.00001, 0.00002],
        [-0.00005, -0.00003, 0.00002, 0.000005, 0.000001],
        [0.00002, 0.00001, 0.000005, 0.00015, 0.00005],
        [0.00001, 0.00002, 0.000001, 0.00005, 0.00025],
    ])
    mu_true = np.array([0.0003, 0.0004, 0.0001, 0.0002, 0.00015])
    returns_data = np.random.multivariate_normal(mu_true, cov_true, n_days)
    returns = pd.DataFrame(returns_data, columns=assets)

    r1 = max_sharpe(returns)
    r2 = min_variance(returns)
    r3 = risk_parity(returns)

    print_result(r1)
    print_result(r2)
    print_result(r3)

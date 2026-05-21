"""
Black-Scholes 期权定价与希腊字母计算
"""
import numpy as np
from scipy.stats import norm
from dataclasses import dataclass


@dataclass
class BSResult:
    price: float
    delta: float
    gamma: float
    theta: float
    vega: float
    rho: float


def black_scholes(S: float, K: float, T: float, r: float, sigma: float,
                  option_type: str = "call") -> BSResult:
    """
    Black-Scholes 期权定价与完整希腊字母

    参数:
        S: 标的现价
        K: 行权价
        T: 到期时间（年）
        r: 无风险利率（年化）
        sigma: 波动率（年化）
        option_type: "call" 或 "put"
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        delta = norm.cdf(d1)
        rho = K * T * np.exp(-r * T) * norm.cdf(d2) / 100
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        delta = norm.cdf(d1) - 1
        rho = -K * T * np.exp(-r * T) * norm.cdf(-d2) / 100

    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    theta = (-(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
             - r * K * np.exp(-r * T) * norm.cdf(d2 if option_type == "call" else -d2)) / 365
    vega = S * norm.pdf(d1) * np.sqrt(T) / 100

    return BSResult(price=price, delta=delta, gamma=gamma,
                    theta=theta, vega=vega, rho=rho)


def implied_volatility(market_price: float, S: float, K: float, T: float,
                       r: float, option_type: str = "call",
                       tol: float = 1e-6, max_iter: int = 200) -> float:
    """Newton-Raphson 法求隐含波动率"""
    sigma = 0.3  # 初始猜测
    for _ in range(max_iter):
        result = black_scholes(S, K, T, r, sigma, option_type)
        diff = result.price - market_price
        if abs(diff) < tol:
            return sigma
        # vega 是价格对 sigma 的导数（已除以100，这里乘回）
        sigma -= diff / (result.vega * 100)
        sigma = max(sigma, 1e-6)  # 防止负值
    return sigma


if __name__ == "__main__":
    # 示例：平值看涨期权
    S, K, T, r, sigma = 100, 100, 0.25, 0.05, 0.2

    call = black_scholes(S, K, T, r, sigma, "call")
    put = black_scholes(S, K, T, r, sigma, "put")

    print(f"Call 期权价格: {call.price:.4f}")
    print(f"  Delta: {call.delta:.4f}  Gamma: {call.gamma:.4f}")
    print(f"  Theta: {call.theta:.4f}  Vega:  {call.vega:.4f}")
    print(f"  Rho:   {call.rho:.4f}")
    print(f"\nPut 期权价格:  {put.price:.4f}")
    print(f"  Delta: {put.delta:.4f}")

    # 验证 Put-Call Parity
    parity = call.price - put.price - S + K * np.exp(-r * T)
    print(f"\nPut-Call Parity 误差: {parity:.8f} (应接近0)")

    # 隐含波动率反推
    iv = implied_volatility(call.price, S, K, T, r, "call")
    print(f"\n隐含波动率: {iv:.4f} (原始: {sigma:.4f})")

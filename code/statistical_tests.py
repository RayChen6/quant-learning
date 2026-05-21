"""
常用统计检验 — 量化研究必备工具
"""
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.tsa.stattools import adfuller, coint
from statsmodels.stats.diagnostic import acorr_ljungbox


def adf_test(series: pd.Series, name: str = "Series") -> dict:
    """ADF 单位根检验（平稳性检验）"""
    result = adfuller(series.dropna(), autolag="AIC")
    output = {
        "name": name,
        "adf_stat": result[0],
        "p_value": result[1],
        "lags": result[2],
        "is_stationary": result[1] < 0.05,
    }
    print(f"[ADF] {name}: stat={result[0]:.4f}, p={result[1]:.4f} "
          f"→ {'平稳' if output['is_stationary'] else '非平稳'}")
    return output


def cointegration_test(s1: pd.Series, s2: pd.Series) -> dict:
    """Engle-Granger 协整检验（配对交易基础）"""
    score, pvalue, crit_values = coint(s1, s2)
    is_cointegrated = pvalue < 0.05
    print(f"[协整] p={pvalue:.4f} → {'存在协整关系' if is_cointegrated else '无协整关系'}")
    return {"score": score, "p_value": pvalue, "is_cointegrated": is_cointegrated}


def normality_test(returns: pd.Series) -> dict:
    """正态性检验（JB 检验）"""
    jb_stat, jb_p = stats.jarque_bera(returns.dropna())
    skew = stats.skew(returns.dropna())
    kurt = stats.kurtosis(returns.dropna())
    is_normal = jb_p > 0.05
    print(f"[正态性] JB stat={jb_stat:.2f}, p={jb_p:.4f}, "
          f"skew={skew:.3f}, excess_kurt={kurt:.3f} "
          f"→ {'正态' if is_normal else '非正态（肥尾）'}")
    return {"jb_stat": jb_stat, "p_value": jb_p, "skewness": skew,
            "excess_kurtosis": kurt, "is_normal": is_normal}


def autocorrelation_test(returns: pd.Series, lags: int = 10) -> pd.DataFrame:
    """Ljung-Box 自相关检验"""
    result = acorr_ljungbox(returns.dropna(), lags=lags, return_df=True)
    print(f"[自相关] Lag 1-{lags} p-values:\n{result['lb_pvalue'].values.round(4)}")
    return result


def monte_carlo_var(returns: pd.Series, n_sim: int = 10000,
                    confidence: float = 0.95) -> float:
    """蒙特卡洛模拟估计 VaR"""
    mu, sigma = returns.mean(), returns.std()
    simulated = np.random.normal(mu, sigma, n_sim)
    var = np.percentile(simulated, (1 - confidence) * 100)
    print(f"[MC VaR] {confidence*100:.0f}% VaR = {var:.4f} ({var*100:.2f}%)")
    return var


if __name__ == "__main__":
    np.random.seed(42)
    # 模拟价格序列
    prices = pd.Series(100 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, 500))))
    returns = prices.pct_change().dropna()

    print("=" * 50)
    adf_test(prices, "Price")
    adf_test(returns, "Returns")
    print("=" * 50)
    normality_test(returns)
    print("=" * 50)
    autocorrelation_test(returns)
    print("=" * 50)
    monte_carlo_var(returns)

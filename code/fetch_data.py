"""
多数据源行情数据获取脚本
支持 AkShare（免费）和 yfinance（美股）
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def fetch_cn_stock_akshare(symbol: str, start: str, end: str,
                            adjust: str = "qfq") -> pd.DataFrame:
    """
    获取A股历史行情（AkShare）
    adjust: qfq=前复权, hfq=后复权, ''=不复权
    需安装: pip install akshare
    """
    try:
        import akshare as ak
        df = ak.stock_zh_a_hist(
            symbol=symbol, period="daily",
            start_date=start.replace("-", ""),
            end_date=end.replace("-", ""),
            adjust=adjust
        )
        df = df.rename(columns={
            "日期": "date", "开盘": "open", "收盘": "close",
            "最高": "high", "最低": "low", "成交量": "volume",
            "成交额": "amount", "涨跌幅": "pct_change"
        })
        df["date"] = pd.to_datetime(df["date"])
        df = df.set_index("date").sort_index()
        print(f"[AkShare] {symbol}: {len(df)} 条记录 ({df.index[0].date()} ~ {df.index[-1].date()})")
        return df
    except ImportError:
        print("请安装 akshare: pip install akshare")
        return _mock_ohlcv(symbol, start, end)


def fetch_us_stock_yfinance(ticker: str, start: str, end: str) -> pd.DataFrame:
    """
    获取美股历史行情（yfinance）
    需安装: pip install yfinance
    """
    try:
        import yfinance as yf
        df = yf.download(ticker, start=start, end=end, progress=False)
        df.columns = [c.lower() for c in df.columns]
        df.index.name = "date"
        print(f"[yfinance] {ticker}: {len(df)} 条记录")
        return df
    except ImportError:
        print("请安装 yfinance: pip install yfinance")
        return _mock_ohlcv(ticker, start, end)


def _mock_ohlcv(symbol: str, start: str, end: str) -> pd.DataFrame:
    """生成模拟 OHLCV 数据（用于演示）"""
    dates = pd.bdate_range(start, end)
    np.random.seed(42)
    close = 100 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, len(dates))))
    df = pd.DataFrame({
        "open":   close * (1 + np.random.uniform(-0.005, 0.005, len(dates))),
        "high":   close * (1 + np.abs(np.random.normal(0, 0.01, len(dates)))),
        "low":    close * (1 - np.abs(np.random.normal(0, 0.01, len(dates)))),
        "close":  close,
        "volume": np.random.randint(1e6, 1e8, len(dates)).astype(float),
    }, index=dates)
    df.index.name = "date"
    print(f"[Mock] {symbol}: {len(df)} 条模拟数据")
    return df


def validate_ohlcv(df: pd.DataFrame) -> dict:
    """数据质量检查"""
    issues = []
    # 高低价逻辑检查
    invalid_hl = (df["high"] < df["low"]).sum()
    if invalid_hl > 0:
        issues.append(f"高低价异常: {invalid_hl} 条")
    # 缺失值
    missing = df.isnull().sum().sum()
    if missing > 0:
        issues.append(f"缺失值: {missing} 个")
    # 零成交量（停牌）
    zero_vol = (df["volume"] == 0).sum()
    if zero_vol > 0:
        issues.append(f"零成交量: {zero_vol} 条")
    # 异常涨跌幅（>30%）
    ret = df["close"].pct_change()
    extreme = (ret.abs() > 0.3).sum()
    if extreme > 0:
        issues.append(f"涨跌幅>30%: {extreme} 条（请检查复权）")

    report = {"total_rows": len(df), "issues": issues, "is_clean": len(issues) == 0}
    print(f"[验证] 共 {len(df)} 条: {'✓ 数据正常' if report['is_clean'] else '⚠ ' + '; '.join(issues)}")
    return report


if __name__ == "__main__":
    end = datetime.today().strftime("%Y-%m-%d")
    start = (datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")

    # 演示（使用模拟数据）
    df = _mock_ohlcv("000001", start, end)
    print(df.tail())
    validate_ohlcv(df)

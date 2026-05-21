"""
XGBoost 多因子选股模型
包含特征工程、Walk-forward 验证与因子 IC 评估
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import RobustScaler
from sklearn.metrics import mean_squared_error
from scipy import stats


def build_features(prices: pd.DataFrame) -> pd.DataFrame:
    """构建技术类因子特征"""
    features = pd.DataFrame(index=prices.index)

    # 动量因子
    for n in [5, 10, 20, 60]:
        features[f"mom_{n}"] = prices.pct_change(n)

    # 波动率因子
    for n in [10, 20]:
        features[f"vol_{n}"] = prices.pct_change().rolling(n).std()

    # 均线偏离
    for n in [10, 20, 60]:
        ma = prices.rolling(n).mean()
        features[f"ma_dev_{n}"] = (prices - ma) / ma

    # 量价特征（如有成交量数据）
    features["rsi_14"] = compute_rsi(prices, 14)

    return features.dropna()


def compute_rsi(prices: pd.Series, period: int = 14) -> pd.Series:
    """RSI 指标"""
    delta = prices.diff()
    gain = delta.clip(lower=0).rolling(period).mean()
    loss = (-delta.clip(upper=0)).rolling(period).mean()
    rs = gain / (loss + 1e-8)
    return 100 - 100 / (1 + rs)


def walk_forward_predict(features: pd.DataFrame,
                         target: pd.Series,
                         train_window: int = 252,
                         test_window: int = 21) -> pd.Series:
    """
    Walk-forward 验证（时序交叉验证）
    每次用过去 train_window 天训练，预测未来 test_window 天
    """
    try:
        import xgboost as xgb
    except ImportError:
        print("请安装 xgboost: pip install xgboost")
        # 返回随机预测用于演示
        return pd.Series(np.random.randn(len(target)), index=target.index)

    predictions = pd.Series(index=target.index, dtype=float)
    scaler = RobustScaler()

    dates = features.index
    for i in range(train_window, len(dates) - test_window, test_window):
        train_idx = range(i - train_window, i)
        test_idx = range(i, min(i + test_window, len(dates)))

        X_train = features.iloc[train_idx]
        y_train = target.iloc[train_idx]
        X_test = features.iloc[test_idx]

        # 去除 NaN
        mask = y_train.notna()
        X_train, y_train = X_train[mask], y_train[mask]
        if len(X_train) < 50:
            continue

        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        model = xgb.XGBRegressor(
            n_estimators=100, max_depth=3, learning_rate=0.05,
            subsample=0.8, colsample_bytree=0.8,
            random_state=42, verbosity=0
        )
        model.fit(X_train_scaled, y_train)
        predictions.iloc[list(test_idx)] = model.predict(X_test_scaled)

    return predictions


def evaluate_predictions(predictions: pd.Series,
                          actual: pd.Series) -> dict:
    """评估预测效果：IC、Rank IC"""
    aligned = pd.concat([predictions, actual], axis=1).dropna()
    pred, real = aligned.iloc[:, 0], aligned.iloc[:, 1]

    ic = stats.pearsonr(pred, real)[0]
    rank_ic = stats.spearmanr(pred, real)[0]

    print(f"\n📊 预测评估:")
    print(f"  IC (Pearson):      {ic:.4f}")
    print(f"  Rank IC (Spearman): {rank_ic:.4f}")
    return {"ic": ic, "rank_ic": rank_ic}


if __name__ == "__main__":
    np.random.seed(42)
    n = 600
    dates = pd.bdate_range("2021-01-01", periods=n)

    # 模拟价格序列
    prices = pd.Series(
        100 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))),
        index=dates
    )

    features = build_features(prices)
    target = prices.pct_change(5).shift(-5).reindex(features.index)  # 未来5日收益

    print(f"特征数量: {features.shape[1]}, 样本数: {len(features)}")
    predictions = walk_forward_predict(features, target,
                                       train_window=200, test_window=20)
    evaluate_predictions(predictions, target)

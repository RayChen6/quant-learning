# 机器学习与 AI — 核心知识点速览

## 1. 金融 ML 的特殊挑战

| 挑战 | 说明 | 应对方案 |
|------|------|---------|
| 低信噪比 | 金融数据噪声极大 | 集成模型、特征筛选 |
| 非平稳性 | 数据分布随时间变化 | 滚动训练、在线学习 |
| 数据泄露 | 标签构建引入未来信息 | Purged K-Fold |
| 样本量小 | 日频数据几十年也就几千条 | 特征工程、迁移学习 |
| 过拟合 | 参数空间巨大，样本少 | 正则化、简单模型优先 |

---

## 2. 特征工程

### 技术类特征
```python
# 常用技术指标特征
df['ma5'] = df['close'].rolling(5).mean()
df['ma20'] = df['close'].rolling(20).mean()
df['rsi14'] = compute_rsi(df['close'], 14)
df['vol20'] = df['close'].pct_change().rolling(20).std()
df['mom12'] = df['close'].pct_change(252)  # 12月动量
```

### 财务类特征
- PE、PB、PS、PCF 估值因子
- ROE、ROA、毛利率、净利润增长率
- 资产负债率、流动比率

---

## 3. 模型选择建议

```
简单 → 复杂：先用线性模型建立 baseline

线性回归/Logistic → Ridge/Lasso → Random Forest
→ XGBoost/LightGBM → LSTM → Transformer
```

**经验规则**：金融场景中 XGBoost 往往优于深度学习（数据量不足）

---

## 4. 防泄露的时序交叉验证

```python
# Purged K-Fold：防止训练集和测试集之间的信息泄露
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5, gap=21)  # gap=21天隔离期
for train_idx, test_idx in tscv.split(X):
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
    model.fit(X_train, y_train)
```

---

## 5. 模型评估（金融场景）

不要只看 Accuracy，更关注：

| 指标 | 说明 |
|------|------|
| IC / Rank IC | 预测值与实际收益的相关性 |
| 多空收益 | 高预测分组 vs 低预测分组的收益差 |
| 换手率 | 预测信号的稳定性 |
| 回测 Sharpe | 最终策略表现 |

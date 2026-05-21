# 机器学习与 AI | Machine Learning & AI

将机器学习与深度学习应用于量化投资，涵盖特征工程、模型选择与防过拟合。

## 学习路线

```
特征工程 → 传统ML → 时序模型 → 深度学习 → NLP情感 → 强化学习
```

## 目录结构

```
ml-ai/
├── notes/
│   ├── 00_overview.md          # 知识点速览
│   ├── 01_feature_engineering.md  # 金融场景特征工程
│   └── 02_model_selection.md   # 模型选择与防过拟合
├── code/
│   ├── xgboost_stock_selection.py  # XGBoost 多因子选股
│   └── lstm_price_prediction.py    # LSTM 价格预测
└── notebooks/
    └── ml_stock_selection.ipynb    # 完整 ML 选股流程
```

## 核心主题

- **特征工程**：技术指标、财务因子、时序特征、交叉特征
- **传统 ML**：Random Forest、XGBoost、LightGBM
- **时序模型**：LSTM、Transformer、时序预测
- **NLP**：新闻情感分析、财报文本挖掘
- **防过拟合**：Walk-forward 验证、Purged K-Fold

## 推荐资源

- 《Advances in Financial Machine Learning》— Marcos López de Prado
- 《Machine Learning for Asset Managers》— Marcos López de Prado
- Python 库：`scikit-learn`, `xgboost`, `lightgbm`, `pytorch`, `transformers`

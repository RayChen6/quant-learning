# ML / AI for Quant Finance 机器学习与AI

> 精选金融机器学习、强化学习交易、AI量化相关的顶级开源项目。

---

## 强化学习交易

| 项目 | Stars量级 | 机构 | 特点 |
|------|-----------|------|------|
| [AI4Finance-Foundation/FinRL](https://github.com/AI4Finance-Foundation/FinRL) | ⭐ 10k+ | Columbia/NTU | 金融强化学习框架，支持股票/加密/期货 |
| [AI4Finance-Foundation/FinRL-Meta](https://github.com/AI4Finance-Foundation/FinRL-Meta) | ⭐ 3k+ | AI4Finance | 动态市场环境数据集，配合 FinRL 使用 |
| [TradeMaster-NTU/TradeMaster](https://github.com/TradeMaster-NTU/TradeMaster) | ⭐ 2k+ | NTU | 量化交易 RL 平台，多环境 benchmark |

## 深度学习 / 传统 ML

| 项目 | Stars量级 | 特点 |
|------|-----------|------|
| [google/tf-quant-finance](https://github.com/google/tf-quant-finance) | ⭐ 4k+ | Google | TensorFlow 量化金融库，定价/风险/随机过程 |
| [edtechre/pybroker](https://github.com/edtechre/pybroker) | ⭐ 2k+ | — | 内置 ML 模型支持的回测框架（sklearn/XGBoost 友好） |
| [grananqvist/Awesome-Quant-Machine-Learning-Trading](https://github.com/grananqvist/Awesome-Quant-Machine-Learning-Trading) | ⭐ 4k+ | — | 量化 ML 论文/资源精选列表 |

## 核心应用方向

### 1. 价格预测与因子挖掘
- LSTM / Transformer 时间序列预测
- XGBoost / LightGBM 因子合成
- 注意：预测 return 远难于预测方向，Sharpe 比 accuracy 更重要

### 2. 强化学习交易
- 状态空间：价格、技术指标、持仓、宏观因子
- 动作空间：买/卖/持有，或连续仓位
- 奖励设计：Sharpe ratio、PnL、Calmar ratio
- 常用算法：PPO、SAC、TD3、A3C

### 3. NLP 情感分析
- 新闻/财报文本 → 情感分数 → Alpha 信号
- FinBERT、ChatGPT/Claude API 在金融 NLP 中的应用
- [LLMQuant/quant-wiki](https://github.com/LLMQuant/quant-wiki) — AI+量化知识库

### 4. 图神经网络 (GNN)
- 股票关系建模（行业、供应链、相关性图）
- 用于组合优化和风险传染分析

## 重要警告 ⚠️

```
❌ 常见陷阱：
  - 用未来数据训练（前视偏差）
  - 过拟合样本内，样本外完全失效
  - 忽略交易成本导致虚假高收益
  - 数据标准化时使用全样本统计量（应用滚动窗口）

✅ 最佳实践：
  - 严格的时间序列交叉验证
  - Purge + Embargo 防止信息泄漏
  - 组合泛化能力 > 单策略性能
  - Walk-forward 验证 + 蒙特卡洛模拟
```

## 关键论文与书籍

| 资源 | 类型 | 要点 |
|------|------|------|
| Advances in Financial Machine Learning (López de Prado) | 书 | 金融 ML 圣经，必读 |
| Machine Learning for Asset Managers (López de Prado) | 书 | 资管视角的 ML 应用 |
| FinRL: A Deep Reinforcement Learning Library (2020) | 论文 | FinRL 原始论文 |
| Attention Is All You Need → 金融序列 | 论文 | Transformer 在量化中的应用基础 |

## 延伸资源

- [awesome-quant](https://github.com/wilsonfreitas/awesome-quant) — 包含 ML 库分类
- [Barca0412/Introduction-to-Quantitative-Finance](https://github.com/Barca0412/Introduction-to-Quantitative-Finance) — AI+金融资料汇总

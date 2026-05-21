# Strategy Development 策略开发

> 精选量化策略开发相关的开源项目与学习资源。

---

## 综合策略平台

| 项目 | Stars量级 | 特点 |
|------|-----------|------|
| [QuantConnect/Lean](https://github.com/QuantConnect/Lean) | ⭐ 10k+ | 支持股票/期权/期货/Forex/Crypto，Alpha 社区共享策略 |
| [quantopian/zipline](https://github.com/quantopian/zipline) | ⭐ 17k+ | Pipeline API 构建因子策略，Quantopian 遗产 |
| [ricequant/rqalpha](https://github.com/ricequant/rqalpha) | ⭐ 5k+ | A 股 + 期货策略开发，国内社区活跃 |
| [StockSharp/StockSharp](https://github.com/StockSharp/StockSharp) | ⭐ 6k+ | C# 全栈，覆盖全球交易所，含图形化策略编辑器 |

## 专项策略库

| 项目 | 策略类型 | 特点 |
|------|----------|------|
| [JerBouma/AlgorithmicTrading](https://github.com/JerBouma/AlgorithmicTrading) | 套利策略 | Optiver 同事审阅，双挂牌/期权/统计套利 |
| [joshyattridge/smart-money-concepts](https://github.com/joshyattridge/smart-money-concepts) | SMC/ICT | 聪明钱概念指标库，结构化交易信号 |
| [shashankvemuri/Finance](https://github.com/shashankvemuri/Finance) | 多种策略 | 150+ Python 程序，含动量/均值回归/配对交易 |

## 经典策略类型

### 动量策略 (Momentum)
- 时序动量：过去 N 个月收益率预测未来
- 截面动量：多头最强 / 空头最弱
- 关键论文：Jegadeesh & Titman (1993)

### 均值回归 (Mean Reversion)
- 配对交易：协整检验 + spread 交易
- 统计套利：多资产残差交易
- Ornstein-Uhlenbeck 过程建模

### CTA / 趋势跟踪
- 移动平均线系统（MACD, Turtle）
- 突破策略、通道突破
- 时间序列动量 (TSMOM)

### 套利策略
- 期现套利、ETF 套利
- 跨市场/跨品种套利
- 统计套利（协整/PCA）

## 书籍配套代码

| 项目 | 书名 | 推荐指数 |
|------|------|----------|
| [yhilpisch/py4at](https://github.com/yhilpisch/py4at) | Python for Algorithmic Trading (O'Reilly) | ⭐⭐⭐⭐⭐ |
| [chrisconlan/algorithmic-trading-with-python](https://github.com/chrisconlan/algorithmic-trading-with-python) | Algorithmic Trading with Python | ⭐⭐⭐⭐ |
| [nickmccullum/algorithmic-trading-python](https://github.com/nickmccullum/algorithmic-trading-python) | freeCodeCamp 课程（免费） | ⭐⭐⭐⭐ |
| [PacktPublishing/Python-for-Algorithmic-Trading-Cookbook](https://github.com/PacktPublishing/Python-for-Algorithmic-Trading-Cookbook) | Python for Algo Trading Cookbook (Packt) | ⭐⭐⭐⭐ |

## 策略开发流程

```
1. 假设生成 → 学术论文 / 市场直觉
2. 数据准备 → 点时间 (Point-in-time) 数据，避免前视偏差
3. 原型验证 → 向量化快速回测
4. 精细回测 → 含交易成本、滑点、容量分析
5. 样本外测试 → Walk-forward / 蒙特卡洛
6. 风险分析 → 回撤、Sharpe、尾部风险
7. 纸交易 → 实盘前的模拟验证
```

## 延伸资源

- [awesome-quant](https://github.com/wilsonfreitas/awesome-quant) — 量化综合资源列表
- [Awesome-Quant-Machine-Learning-Trading](https://github.com/grananqvist/Awesome-Quant-Machine-Learning-Trading) — 强调 ML 的量化资源

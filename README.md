# Execution & Trading Systems 执行与交易系统

> 精选算法执行、订单管理、市场微观结构、高频交易相关的开源项目与学习资源。

---

## 交易框架与 OMS

| 项目 | Stars量级 | 语言 | 特点 |
|------|-----------|------|------|
| [QuantConnect/Lean](https://github.com/QuantConnect/Lean) | ⭐ 10k+ | C#/Python | 完整 OMS + 实盘接口，支持多家券商 |
| [StockSharp/StockSharp](https://github.com/StockSharp/StockSharp) | ⭐ 6k+ | C# | 全功能交易平台，含图形界面，覆盖全球交易所 |
| [ricequant/rqalpha](https://github.com/ricequant/rqalpha) | ⭐ 5k+ | Python | 支持实盘交易，A 股 + 期货 |
| [Lumiwealth/lumibot](https://github.com/Lumiwealth/lumibot) | ⭐ 2k+ | Python | AI 交易 Agent 框架，含 Alpaca/IBKR 实盘接口 |
| [gbeced/basana](https://github.com/gbeced/basana) | ⭐ 500+ | Python | async 异步框架，低延迟，Crypto 专注 |
| [alpacahq/example-hftish](https://github.com/alpacahq/example-hftish) | ⭐ 300+ | Python | Alpaca 出品，订单薄失衡算法示例 |

## 算法执行策略

### 基准执行算法

| 算法 | 全称 | 目标 |
|------|------|------|
| **TWAP** | Time-Weighted Average Price | 时间均匀拆单，减少时间集中 |
| **VWAP** | Volume-Weighted Average Price | 跟踪市场成交量节奏 |
| **POV** | Percentage of Volume | 按市场成交量比例参与 |
| **IS** | Implementation Shortfall | 最小化决策价格与成交价差距 |
| **Arrival Price** | — | 以到达市场时价格为基准 |

### 高频与做市策略
```
做市策略 (Market Making)
├── 报价在买卖价差两侧
├── 赚取 bid-ask spread
└── 风险：库存风险、逆选择风险

统计套利 (Stat Arb)
├── 极短周期的均值回归
└── 需要低延迟执行基础设施

动量点火 (Momentum Ignition)
└── 监管灰色地带，了解即可
```

## 市场微观结构

### 核心概念

```
订单薄 (Order Book)
├── 限价单 (Limit Order)：指定价格挂单
├── 市价单 (Market Order)：立即以最优价成交
└── 冰山单 (Iceberg Order)：隐藏大额委托

买卖价差 (Bid-Ask Spread)
├── 名义价差：Ask - Bid
├── 有效价差：2 × |成交价 - 中间价|
└── 实现价差：衡量做市商实际盈利

价格冲击 (Market Impact)
├── 临时冲击：随订单完成消散
└── 永久冲击：反映信息，不可逆
```

### 订单薄失衡 (Order Book Imbalance)

```python
# OBI 信号
OBI = (BidVolume - AskVolume) / (BidVolume + AskVolume)
# OBI > 0：买方压力大，价格可能上涨
# OBI < 0：卖方压力大，价格可能下跌
```

## 交易成本分析 (TCA)

| 成本类型 | 说明 | 量化方法 |
|----------|------|----------|
| 佣金 | 明确费用 | 直接计算 |
| 买卖价差 | 隐性成本 | 有效价差 |
| 市场冲击 | 大单推动价格 | Almgren-Chriss 模型 |
| 时机成本 | 延迟执行的机会成本 | IS 基准对比 |
| 滑点 | 预期成交价 vs 实际成交价 | 回测 vs 实盘对比 |

## Almgren-Chriss 最优执行模型

```
经典论文：Almgren & Chriss (2001)
- 交易速度 vs 市场冲击 的权衡
- 给出最优执行轨迹（交易前沿）
- 风险厌恶程度 → 执行速度
- 实践中 IS 算法的理论基础
```

## 低延迟基础设施（了解）

```
硬件层：FPGA、kernel bypass、RDMA
网络层：共置 (Co-location)、微波传输
软件层：无锁队列、内存池、CPU 亲和性
编程语言：C++（纳秒级），Rust（新兴）
```

## 延伸资源

- [awesome-quant](https://github.com/wilsonfreitas/awesome-quant) — 含交易系统工具分类
- [quant-wiki](https://github.com/LLMQuant/quant-wiki) — 市场微观结构知识库
- [StockSharp/StockSharp](https://github.com/StockSharp/StockSharp) — 最完整的开源交易平台

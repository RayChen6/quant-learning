# Financial Theory 金融理论

> 精选金融理论、衍生品定价、资产定价模型相关的顶级开源项目与学习资源。

---

## 核心项目

| 项目 | Stars量级 | 特点 |
|------|-----------|------|
| [cantaro86/Financial-Models-Numerical-Methods](https://github.com/cantaro86/Financial-Models-Numerical-Methods) | ⭐ 3k+ | 金融模型数值方法完整 Notebook 集，含随机微积分/期权定价/利率模型 |
| [goldmansachs/gs-quant](https://github.com/goldmansachs/gs-quant) | ⭐ 3k+ | 高盛出品，涵盖衍生品定价、风险管理、资产配置 |
| [dwcoder/QuantitativePrimer](https://github.com/dwcoder/QuantitativePrimer) | ⭐ 1k+ | 量化金融面试必备，覆盖核心理论知识 |
| [google/tf-quant-finance](https://github.com/google/tf-quant-finance) | ⭐ 4k+ | TensorFlow 实现随机过程、期权定价、利率模型 |
| [LLMQuant/quant-wiki](https://github.com/LLMQuant/quant-wiki) | ⭐ 活跃 | 量化金融理论百科（中英文双语） |

## 资产定价理论

### 经典模型

| 模型 | 要点 | 局限 |
|------|------|------|
| **CAPM** | 期望收益 = 无风险利率 + β × 市场溢价 | 单因子，假设太强 |
| **APT** | 多因子线性定价 | 因子未预先指定 |
| **Fama-French 三/五因子** | 规模/价值/盈利/投资因子 | 见 alpha-research 分支 |
| **随机贴现因子 (SDF)** | 统一定价框架 | 理论抽象 |

## 衍生品定价

### 期权定价模型

```
Black-Scholes-Merton (BSM)
├── 假设：对数正态、常数波动率、无交易成本
├── 公式：C = S·N(d1) - K·e^(-rT)·N(d2)
└── 局限：波动率微笑/偏斜无法解释

随机波动率模型
├── Heston 模型：波动率均值回归 + 与价格相关
├── SABR 模型：利率衍生品广泛使用
└── Rough Volatility：Bergomi/Gatheral (近年)

局部波动率
└── Dupire 模型：从期权价格反推局部波动率曲面

跳跃扩散
└── Merton Jump Diffusion：加入泊松跳跃过程
```

### 数值方法

| 方法 | 适用场景 |
|------|----------|
| **解析公式** | BSM 欧式期权，有闭合解 |
| **二叉树/三叉树** | 美式期权，早期行权 |
| **有限差分法 (FDM)** | PDE 求解，路径依赖期权 |
| **蒙特卡洛模拟** | 复杂路径依赖期权（亚式、障碍式） |
| **傅里叶变换** | Heston 等仿射模型，高效定价 |

## 固定收益与利率

### 收益率曲线
```
即期利率、远期利率、到期收益率 (YTM)
Nelson-Siegel 模型：水平/斜率/曲率三因子
插值方法：线性、三次样条、Monotone Convex
```

### 利率模型
```
短率模型：Vasicek、CIR、Hull-White
HJM 框架：Heath-Jarrow-Morton 前向利率
LIBOR 市场模型 (LMM)：利率互换定价标准
```

## 随机微积分基础

```
布朗运动 (Wiener Process)
伊藤引理 (Ito's Lemma)
随机微分方程 (SDE)
风险中性测度 / Girsanov 定理
鞅理论
```

**推荐学习资源（含在 cantaro86/Financial-Models-Numerical-Methods）：**
- Geometric Brownian Motion
- Heston 随机波动率
- VaR / CVaR 计算
- 傅里叶期权定价

## 关键教材

| 书名 | 作者 | 特点 |
|------|------|------|
| Options, Futures, and Other Derivatives | John Hull | 衍生品圣经，必读 |
| Paul Wilmott on Quantitative Finance | Paul Wilmott | 三卷本，最系统 |
| The Concepts and Practice of Mathematical Finance | Mark Joshi | 数学严谨，面试友好 |
| Interest Rate Models — Theory and Practice | Brigo & Mercurio | 利率衍生品权威 |
| Stochastic Calculus for Finance I/II | Shreve | 随机微积分数学基础 |

## 延伸资源

- [awesome-quant](https://github.com/wilsonfreitas/awesome-quant) — 含定价库分类
- [dwcoder/QuantitativePrimer](https://github.com/dwcoder/QuantitativePrimer) — 面试题精华

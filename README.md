# Math & Statistics 数学与统计基础

> 量化金融所需的数学与统计学基础知识，精选开源项目与学习资源。

---

## 核心项目

| 项目 | Stars量级 | 特点 |
|------|-----------|------|
| [cantaro86/Financial-Models-Numerical-Methods](https://github.com/cantaro86/Financial-Models-Numerical-Methods) | ⭐ 3k+ | 量化金融数值方法完整实现，含随机过程/蒙特卡洛/有限差分 |
| [google/tf-quant-finance](https://github.com/google/tf-quant-finance) | ⭐ 4k+ | 随机过程数值实现：布朗运动、Hull-White、Heston |
| [dwcoder/QuantitativePrimer](https://github.com/dwcoder/QuantitativePrimer) | ⭐ 1k+ | 量化面试数学知识精华 |
| [LLMQuant/quant-wiki](https://github.com/LLMQuant/quant-wiki) | ⭐ 活跃 | 数学统计知识库（中英文） |

## 概率论基础

```
基础概念
├── 概率空间 (Ω, F, P)
├── 随机变量、分布函数、PDF/CDF
├── 期望、方差、协方差、相关系数
└── 大数定律、中心极限定理

重要分布
├── 正态分布：N(μ, σ²)
├── 对数正态分布：金融资产价格模型
├── t 分布：小样本、厚尾
├── χ² 分布：方差检验
└── 极值分布 (GEV/GPD)：尾部风险
```

## 随机过程

### 布朗运动 (Wiener Process)
```
性质：
- W(0) = 0，连续路径
- W(t) - W(s) ~ N(0, t-s)，独立增量
- 二次变差 [W,W]_t = t

几何布朗运动 (GBM)：
dS = μS dt + σS dW
→ S(T) = S(0) exp((μ - σ²/2)T + σW(T))
→ 标准股价模型
```

### 均值回归过程
```
Ornstein-Uhlenbeck (OU) 过程：
dX = θ(μ - X)dt + σ dW
→ 利率、价差模型

Vasicek 利率模型：
dr = a(b - r)dt + σ dW
→ 利率均值回归
```

### 随机微积分
```
伊藤引理 (Ito's Lemma)：
df(X,t) = (∂f/∂t + μ∂f/∂X + ½σ²∂²f/∂X²)dt + σ∂f/∂X dW

关键应用：推导 BSM 方程
```

## 统计学

### 时间序列分析
```
平稳性检验：ADF 检验、KPSS 检验
自相关：ACF、PACF 图
ARMA/ARIMA 模型：收益率建模
GARCH 模型：波动率聚集性建模
协整检验：Engle-Granger、Johansen
```

### 回归分析
```
OLS 线性回归：因子模型基础
Fama-MacBeth 回归：截面因子检验
Ridge/Lasso：高维因子降维
Huber 回归：鲁棒回归，减少异常值影响
```

### 假设检验
```
t 检验：因子 IC 显著性
F 检验：多因子联合显著性
多重检验问题：Bonferroni、FDR 校正
Bootstrap：非参数置信区间
```

## 线性代数

```
矩阵运算：协方差矩阵估计与因子风险模型
特征值分解：PCA 主成分分析
奇异值分解 (SVD)：降维、因子提取
正定矩阵：协方差矩阵的必要条件
```

## 数值方法

| 方法 | 应用 |
|------|------|
| 蒙特卡洛模拟 | 期权定价、VaR 计算 |
| 有限差分法 | PDE 求解（BSM 方程） |
| 数值积分 | 傅里叶变换期权定价 |
| 优化算法 | 组合优化（凸优化、遗传算法） |

## 学习路径

```
Level 1（基础）
  → 概率论与统计（《概率论与数理统计》陈希孺）
  → 线性代数（MIT 18.06 Gilbert Strang）

Level 2（进阶）
  → 随机微积分（Shreve《Stochastic Calculus for Finance》）
  → 时间序列分析（Hamilton《Time Series Analysis》）

Level 3（应用）
  → cantaro86/Financial-Models-Numerical-Methods (实践)
  → López de Prado 系列书籍
```

## 延伸资源

- [awesome-quant](https://github.com/wilsonfreitas/awesome-quant) — 含数学工具库分类
- [quant-wiki](https://github.com/LLMQuant/quant-wiki) — 数学统计基础知识库（中英文）

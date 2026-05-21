# Alpha Research 因子与 Alpha 研究

> 精选因子挖掘、Alpha 生成、多因子模型相关的顶级开源项目与研究资源。

---

## 核心工具与框架

| 项目 | Stars量级 | 特点 |
|------|-----------|------|
| [quantopian/zipline](https://github.com/quantopian/zipline) | ⭐ 17k+ | Pipeline API 是因子研究的工业标准，因子表达式清晰 |
| [quantopian/alphalens](https://github.com/quantopian/alphalens) | ⭐ 3k+ | 因子分析神器：IC/IR、分层收益、换手率分析 |
| [shashankvemuri/Finance](https://github.com/shashankvemuri/Finance) | ⭐ 2k+ | 150+ 量化程序，含多种因子实现 |
| [Barca0412/Introduction-to-Quantitative-Finance](https://github.com/Barca0412/Introduction-to-Quantitative-Finance) | ⭐ 活跃 | 多因子股票量化框架开源教程，含学界业界经典资料 |
| [LLMQuant/quant-wiki](https://github.com/LLMQuant/quant-wiki) | ⭐ 活跃 | 量化 Wiki，含因子投资系统性知识（中英文） |

## 经典因子体系

### Fama-French 因子
| 因子 | 说明 | 经典论文 |
|------|------|----------|
| **市场因子 (MKT)** | 超额市场收益 | Sharpe (1964) |
| **规模因子 (SMB)** | 小市值 - 大市值 | Fama & French (1993) |
| **价值因子 (HML)** | 高 B/P - 低 B/P | Fama & French (1993) |
| **动量因子 (MOM)** | 过去 12-1 月收益 | Carhart (1997) |
| **盈利因子 (RMW)** | 高盈利 - 低盈利 | Fama & French (2015) |
| **投资因子 (CMA)** | 保守投资 - 激进投资 | Fama & French (2015) |

### A 股常用因子
```
价值类：EP、BP、SP、EBITDA/EV
成长类：营收增速、利润增速、ROE变化
质量类：ROE、毛利率、应计项目
动量类：1个月/3个月/12个月动量、反转
流动性：换手率、Amihud 非流动性
情绪类：分析师覆盖、预期上调
```

## 因子分析流程

```
1. 因子构建
   ├── 原始数据 → 因子计算
   ├── 横截面标准化（去极值 + Z-score）
   └── 行业/市值中性化

2. 因子评价（使用 alphalens）
   ├── IC（信息系数）：因子与未来收益的相关性
   ├── IR（信息比率）：IC 均值 / IC 标准差
   ├── 分层收益：因子分 5/10 组的收益差异
   └── 换手率：因子稳定性指标

3. 因子合成
   ├── 等权合成
   ├── IC 加权
   └── PCA / 机器学习合成

4. 组合构建
   └── 见 portfolio-mgmt 分支
```

## IC 分析关键指标

| 指标 | 好的范围 | 说明 |
|------|----------|------|
| IC 均值 | > 0.03 | 因子预测能力 |
| IR | > 0.5 | 因子稳定性 |
| IC > 0 比例 | > 55% | 因子方向一致性 |
| 分层收益差 | > 3% 年化 | 多空组合收益 |

## 因子有效性衰减

```
学术发表 → 策略被市场套利 → 因子 Alpha 衰减

应对方法：
- 使用更高频数据（日内、Tick）
- 组合多个相关性低的因子
- 挖掘非标准另类因子
- 持续更新因子库
```

## 重要论文

| 论文 | 要点 |
|------|------|
| Fama & French (1993) | 三因子模型 |
| Carhart (1997) | 四因子（加动量） |
| Fama & French (2015) | 五因子模型 |
| Harvey et al. (2016) - … and the Cross-Section of Expected Returns | 因子 p-hacking 警告 |
| Hou et al. (2020) - Replicating Anomalies | 大量因子无法复现 |
| López de Prado (2018) - Advances in Financial Machine Learning | ML 因子挖掘方法 |

## 延伸资源

- [awesome-quant](https://github.com/wilsonfreitas/awesome-quant) — 含因子库分类
- [grananqvist/Awesome-Quant-Machine-Learning-Trading](https://github.com/grananqvist/Awesome-Quant-Machine-Learning-Trading) — ML 因子挖掘资源

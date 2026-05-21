# 因子与 Alpha 研究 — 核心知识点速览

## 1. 因子分类

| 类别 | 常见因子 | 逻辑 |
|------|---------|------|
| 价值 | P/E, P/B, P/S | 低估值股票未来收益高 |
| 动量 | 过去12-1月收益 | 近期强势股继续强势 |
| 质量 | ROE, ROA, 毛利率 | 盈利能力强的公司更优质 |
| 低波动 | 历史波动率, Beta | 低风险股票长期回报更好 |
| 规模 | 市值 | 小市值有超额收益（小盘效应） |
| 流动性 | 换手率, Amihud | 流动性差的股票有溢价 |

---

## 2. 因子评估指标

### IC（Information Coefficient）
$$IC_t = \text{Corr}(f_{t}, r_{t+1})$$

因子值与下期收益的截面相关系数（Spearman 或 Pearson）。

| 指标 | 含义 | 参考标准 |
|------|------|---------|
| IC Mean | 平均 IC | >0.05 有参考价值 |
| IC Std | IC 标准差 | 越小越稳定 |
| IR (IC/IC_Std) | 信息比率 | >0.5 较好 |
| IC>0 比例 | 正 IC 胜率 | >55% 较好 |

---

## 3. 分层回测流程

```
1. 每期按因子值将股票分为 N 组（通常5组）
2. 计算每组的等权或市值加权收益
3. 观察收益是否单调递增/递减（多空组合）
4. 计算多头组 - 空头组的年化超额收益
```

---

## 4. 因子处理流程

```python
import pandas as pd
import numpy as np

def process_factor(factor: pd.Series) -> pd.Series:
    # 1. 去极值（MAD法）
    median = factor.median()
    mad = (factor - median).abs().median()
    factor = factor.clip(median - 3*mad, median + 3*mad)

    # 2. 中性化（市值中性化）
    # 对市值取对数回归，取残差
    # factor = neutralize(factor, market_cap)

    # 3. 标准化（Z-Score）
    factor = (factor - factor.mean()) / factor.std()

    return factor
```

---

## 5. 常见陷阱

- **前视偏差**：使用了未来才能获得的财务数据（如季报发布有延迟）
- **幸存者偏差**：只用当前股票池，忽略已退市股票
- **因子拥挤**：因子被大量资金使用后失效
- **过拟合**：样本内完美但样本外失效

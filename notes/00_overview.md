# 数据获取与处理 — 核心知识点速览

## 1. 数据源对比

| 数据源 | 类型 | 费用 | 适用场景 |
|--------|------|------|----------|
| AkShare | A股/港股/美股 | 免费 | 学习研究 |
| Tushare Pro | A股全量 | 积分制 | 国内量化研究 |
| yfinance | 美股/ETF | 免费 | 美股研究 |
| Wind | 全市场 | 收费 | 专业机构 |
| Bloomberg | 全球 | 昂贵 | 顶级机构 |

---

## 2. OHLCV 数据规范

```
O - Open    开盘价
H - High    最高价
L - Low     最低价
C - Close   收盘价
V - Volume  成交量
```

**数据质量检查清单**：
- [ ] 时间索引是否连续（排除非交易日）
- [ ] 是否存在缺失值（NaN）
- [ ] 是否存在价格异常跳跃（可能是除权未复权）
- [ ] 成交量是否为0（停牌）
- [ ] 是否已做复权处理

---

## 3. 复权计算

- **前复权**：以最新价格为基准向前调整，适合回测（历史价格会变化）
- **后复权**：以上市首日为基准向后调整，价格持续增长（不适合跨期比较）
- **不复权**：原始价格，会有除权跳空

```python
# AkShare 获取前复权数据
import akshare as ak
df = ak.stock_zh_a_hist(symbol="000001", period="daily",
                         adjust="qfq")  # qfq=前复权, hfq=后复权
```

---

## 4. 数据清洗流程

```python
import pandas as pd

def clean_ohlcv(df):
    # 1. 去重
    df = df.drop_duplicates(subset=['date'])
    # 2. 排序
    df = df.sort_values('date').reset_index(drop=True)
    # 3. 处理缺失值（向前填充）
    df = df.fillna(method='ffill')
    # 4. 过滤停牌日（成交量为0）
    df = df[df['volume'] > 0]
    # 5. 异常价格过滤（日涨跌幅超过±20%的A股可疑）
    df['ret'] = df['close'].pct_change()
    df = df[df['ret'].abs() < 0.21]
    return df
```

---

## 5. 存储方案选择

| 格式 | 优点 | 缺点 | 适用 |
|------|------|------|------|
| CSV | 简单通用 | 慢、大 | 小数据集 |
| HDF5 | 快速读写 | 文件损坏风险 | 中等数据量 |
| Parquet | 列式压缩高效 | 需要 pyarrow | 大数据集 |
| SQLite | 支持查询 | 并发差 | 结构化查询 |

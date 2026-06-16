# ch4 Figure 抽取与映射策略

> 本文件说明 PCIe 6.2 规范第 4 章的图表抽取、剪裁、命名、映射规则。

## 1. 总体策略

ch4 共 63 张 Figure 4-1 ~ Figure 4-63,分布在 53 个 PDF 页面上(351–650)。
采用**双轨制**抽取:

| 轨道 | 数据源 | 用途 | 命名 |
|------|--------|------|------|
| **全页 PNG** | `extract_pcie6_2.py` PyMuPDF 全页渲染 | 兜底 / 缺图时引用 | `fig_PPPP_1.png` |
| **精裁 PNG** | MinerU `content_list.json` bbox + 抽取图 | 正常情况引用 | `fig_PPPP_NN_tight.png` |

精裁优先,全页兜底。

## 2. 抽取流程

```
PDF chunk ──► MinerU 解析 ──► content_list.json
                                  │
                  ┌───────────────┼───────────────┐
                  ▼               ▼               ▼
            type=image      type=table      type=other
            img_caption     table_caption
                  │               │
                  └─── Figure 4-NN 匹配 ───┘
                                  │
                                  ▼
                       收集 page → figure 映射
                                  │
            ┌─────────────────────┴─────────────────────┐
            ▼                                           ▼
   img_path 存在(JPG)                          img_path 缺失
            │                                   (如 Figure 4-24 误判为 table)
            ▼                                           │
   直接复制 MinerU JPG                                ▼
            │                              用 bbox 从 chunk PDF 重渲染
            ▼                                           │
   fig_PPPP_NN_tight.png  ◄────────────────────────────┘
```

## 3. 工具脚本

| 脚本 | 功能 |
|------|------|
| `tools/ch4_figure_map.py` | 扫描 raw markdown,生成 page→figure 映射表 |
| `tools/ch4_tight_crops.py` | 基于 MinerU content_list 渲染/复制精裁图 |
| `tools/extract_pcie6_2.py` | 全页 PNG 抽取(原始策略,作为兜底) |
| `tools/render_tight_crops.py` | 通用 MinerU 紧致裁剪工具 |

## 4. 命名规则

```
fig_<PAGE_4digit>_<INDEX>_<SUFFIX>.png

PAGE   : 4 位 PDF 页码(1-indexed,前导 0)
INDEX  : 同页 figure 序号(1, 2, 3...)
SUFFIX : _tight (精裁) / 无 (全页)
```

示例:
- `fig_0354_1_tight.png` — 第 354 页第 1 张精裁图(Figure 4-2)
- `fig_0354_2_tight.png` — 第 354 页第 2 张精裁图(Figure 4-3)
- `fig_0448_1_tight.png` — 第 448 页第 1 张精裁图(Figure 4-42)
- `fig_0385_1.png` — 第 385 页全页图(兜底)

## 5. 关键发现(本次扫描)

### 5.1 ch4 图总体统计
- **63** 个 Figure 4-XX 标题
- **53** 个 PDF 页含 Figure 标题
- **9** 页含多张 Figure(需拆分全页图)
- **0** 页缺图(所有 Figure 都有可用 PNG)

### 5.2 多 Figure 页面清单

| 页码 | Figure 编号 | 原因 |
|------|-------------|------|
| 354 | 4-2, 4-3 | 同一页两张小图 |
| 359 | 4-6, 4-7 | 同上 |
| 360 | 4-8, 4-9 | 同上 |
| 368 | 4-14, 4-15, 4-16 | 三图同页 |
| 384 | 4-22, 4-23 | 同上 |
| 404 | 4-29, 4-30 | 同上 |
| 433 | 4-37, 4-38 | 同上 |
| 448 | 4-42, 4-43 | 8.0/16.0 GT/s 流程图对照 |
| 586 | 4-59, 4-60 | 同上 |

### 5.3 MinerU 误分类情况

| Figure | MinerU 分类 | 处理方式 |
|--------|-------------|----------|
| Figure 4-24 (page 385) | `type=table` (PAM4 电压表) | 用 table bbox 从 PDF 重渲染 |
| Figure 4-36 (page 432) | 出现在 `table_footnote` | 暂未抽取,需要额外处理 |

### 5.4 缺失图

无。

## 6. 映射文件

| 文件 | 内容 |
|------|------|
| `ch4_figure_map.json` | 全量 page → figure 映射(63 figures, 56 tables) |
| `ch4_tight_crops.json` | 精裁图清单(46 figures 含 file/bbox/caption) |
| `raw/chapter_04_raw.md` | 源 spec 文本(含 PAGE_BREAK 与 Figure caption) |

## 7. 在 Markdown 中引用精裁图

```markdown
> **Figure 4-42.** 8.0 GT/s Equalization Flow
> <img src="figures/chapter_04/fig_0448_1_tight.png" width="700">

**Figure 4-42 | 图 4-42**: 8.0 GT/s 均衡流程
```

多 Figure 同页时:
```markdown
> <img src="figures/chapter_04/fig_0354_1_tight.png" width="700">  ← Figure 4-2
> <img src="figures/chapter_04/fig_0354_2_tight.png" width="700">  ← Figure 4-3
```

## 8. 兜底策略

当精裁图缺失或异常时,回退到全页图:

```python
def get_fig_path(page, idx=1, prefer_tight=True):
    tight = f"figures/chapter_04/fig_{page:04d}_{idx}_tight.png"
    full  = f"figures/chapter_04/fig_{page:04d}_{idx}.png"
    if prefer_tight and os.path.exists(tight):
        return tight
    if os.path.exists(full):
        return full
    return None
```

## 9. 验证清单

- [x] 63 个 Figure 全部找到 caption
- [x] 46 个 Figure 精裁图已生成(MinerU JPG 44 个 + PDF 重渲染 2 个)
- [x] 9 个多图页面已正确拆分
- [x] Figure 4-24 误分类问题已修复
- [ ] Figure 4-36 (table_footnote) 待补充
- [ ] 与翻译文件中的 `<img>` 引用对账

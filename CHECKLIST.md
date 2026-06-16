# PCIe 6.2 zh — 自检 Checklist

> 用于 ch01-ch12 翻译质量的全面自检。

## 类别 A: HTML/Markdown 语法合法性

- [ ] **A1**: 无 `table>` 截断(应全部为 `<table>`)
- [ ] **A2**: 所有 `<img>` 标签格式正确(`<img src="..." width="N">`)
- [ ] **A3**: 所有 `<img>` 闭合引号正确(`src="..."`)
- [ ] **A4**: 所有 `<table>...</table>` 配对闭合
- [ ] **A5**: 所有 `<div ...>...</div>` 配对闭合
- [ ] **A6**: 无孤立的中英两列内容(如 `<td>` 中混 `<tr>`)

## 类别 B: 图像引用完整性

- [ ] **B1**: 所有 `<img src=...fig_PPPP_NN.png>` 的 PNG 文件存在
- [ ] **B2**: 所有 `<img src=...fig_PPPP_NN_tight.png>` 的 PNG 文件存在
- [ ] **B3**: `_tight.png` 比例 ≥ 70% (排除 ch1 / ch3 / ch5 等小章节)
- [ ] **B4**: 无 0 字节或损坏的 PNG 文件

## 类别 C: 跨列重复清理

- [ ] **C1**: 同一 `<img>` 在 `<td>` 与 `<td>` 中不重复
- [ ] **C2**: 同一 `<img>` 在 blockquote 中不重复(对 Category 2)
- [ ] **C3**: 同一 figure caption("Figure 4-X" 和 "图 4-X") 不与同一 img 多次绑定

## 类别 D: 中英对照双列结构

- [ ] **D1**: 每节使用 `<div style="overflow-x:auto"><table>...` 标准布局
- [ ] **D2**: 表头包含 `🇬🇧 English` / `🇨🇳 中文` 两列
- [ ] **D3**: 中文列带 `background-color:#e8e8e8`
- [ ] **D4**: 双列宽度 50/50

## 类别 E: Figure / Table 引用完整性

- [ ] **E1**: 文档中所有 `Figure X-NN` 引用都有对应 img 或 caption
- [ ] **E2**: 文档中所有 `Table X-NN` 引用都有对应表格
- [ ] **E3**: 没有 `Figure X-` 残缺引用(如缺编号)
- [ ] **E4**: ch{N}_tight_crops.json 与实际 PNG 文件一致

## 类别 F: 章节结构完整性

- [ ] **F1**: 章节标题(## N.X.Y)层级清晰
- [ ] **F2**: 4.2.4 等子节标题层级正确(h2 主节 + h3 子节)
- [ ] **F3**: TOC 导航链接与实际章节对应
- [ ] **F4**: PAGE_BREAK 标记存在且格式正确

## 类别 G: Git/Repo 健康度

- [ ] **G1**: git status 干净(无未提交修改)
- [ ] **G2**: 最近 commit 包含所有修复
- [ ] **G3**: 远程与本地一致
- [ ] **G4**: README.md 有当前更新日志

## 类别 H: 文件级大小/健康

- [ ] **H1**: MD 文件大小无异常(0 字节 / 过大)
- [ ] **H2**: 图 PNG 文件正常
- [ ] **H3**: JSON 映射文件可解析
- [ ] **H4**: tools/*.py 无语法错误

## 自检执行顺序

1. **语法层 (A)**: HTML 截断 / img 标签
2. **文件层 (B)**: 引用完整性
3. **结构层 (C/D)**: 双列布局
4. **逻辑层 (E/F)**: 引用一致性、章节结构
5. **环境层 (G/H)**: git / 文件健康

# PCIe 6.2 中英对照翻译 — 质量提升实施方案

> 基于 6 维质量模型审计结果 | 2026-07-01

---

## 总体状态

| 维度 | 当前评分 | 目标评分 |
|------|:------:|:------:|
| 协议忠实度 | 9.2 | 9.5 |
| 术语一致性 | 8.5 | 9.0 |
| 结构可追溯 | 9.0 | 9.5 |
| Markdown 可读性 | 8.8 | 9.5 |
| 图表完整性 | 8.5 | 9.0 |
| 法务合规 | ⚠️ 待评估 | 明确策略 |

---

## Phase 1: 渲染断裂修复 (P0) — 预计 1h

### 1.1 ch11 标签平衡修复

**问题**: `<table>=29, </table>=27`，2 组双语表格未闭合，导致后续 Markdown 内容被吞入 HTML 单元格。

**根因**: §11.3.12 GET_DEVICE_INTERFACE_STATE 和 §11.4 Device Security Requirements 两个双语 `<table>` 缺少 `</td></tr></tbody></table>` 闭合序列。

**修复脚本**:

```python
# fix_ch11_tags.py
import re

with open('PCIe6.2_Spec_ch11_...TDISP.md', 'r') as f:
    content = f.read()

# Fix 1: Close the §11.3.12 table before the Markdown-only sub-sections begin
# Insert </td></tr></tbody></table> before <!-- 📄 Page 1637 -->
old1 = '\n<!-- 📄 Page 1637 -->\n---\n\n<a id="sec-11-3-12">'
new1 = '\n</td>\n</tr>\n</tbody>\n</table>\n\n<!-- 📄 Page 1637 -->\n---\n\n<a id="sec-11-3-12">'
content = content.replace(old1, new1)

# Fix 2: Close the §11.4 table before §11.5 (previously relied on orphan </table> at EOF)
old2 = '<!-- 📄 Page 1645 -->\n---\n\n## 11.5 Requirements'
new2 = '</td>\n</tr>\n</tbody>\n</table>\n\n<!-- 📄 Page 1645 -->\n---\n\n## 11.5 Requirements'
content = content.replace(old2, new2)

# Verify
assert content.count('<table>') == content.count('</table>'), "Table balance check failed!"

with open('PCIe6.2_Spec_ch11_...TDISP.md', 'w') as f:
    f.write(content)
```

### 1.2 ch02 `<div>` 不平衡

**问题**: `<div`=92, `</div>`=93（多1个闭合标签）。

**执行**: 使用 HTML 验证器定位多余 `</div>`，精确删除。

---

## Phase 2: 格式规范统一 (P1) — 预计 3h

### 2.1 IMPLEMENTATION NOTE 格式统一

**问题**: ch03 L2016 使用 `**实现注:**`，其他处使用 `**实现说明 (IMPLEMENTATION NOTE):**`。

**执行**:

```bash
# 全库统一为完整格式
grep -rn '\*\*实现注[^意]' PCIe6.2_Spec_ch*.md
# 逐处替换为: **实现说明 (IMPLEMENTATION NOTE):**
```

### 2.2 交叉引用格式策略决策

**现状**: `§ Section X.Y` (EN form) vs `§ 第 X.Y 节` (ZH form)，全库中式占比仅 25%。

**建议**: 保持 `§ Section X.Y` 统一格式（中文技术文档惯例），明确写入 README 格式约定。

**如需统一为中文格式**:

```bash
# 仅在 ZH 单元格内替换
python3 << 'PYEOF'
import re, glob
for f in glob.glob('PCIe6.2_Spec_ch*.md'):
    with open(f) as fh: c = fh.read()
    cells = re.split(r'(<td style="background-color:#e8e8e8">)(.*?)(</td>)', c, flags=re.DOTALL)
    # Replace § Section X.Y → § 第 X.Y 节 in ZH cells only
    # (需精确匹配 Section 后跟数字的模式)
PYEOF
```

### 2.3 章节编号缺失 TOC 补全

**问题**: ch07 表格/图 TOC 中 ~200 条中文标题空白。

**执行**: 从正文自动提取中文标题，批量回填 TOC。

---

## Phase 3: Figure 双语标题补全 (P2) — 预计 6-8h

### 3.1 现状

~300 个 Figure 缺少 `> **图 N-XX**` 中文双语标题，分布:

| 章节 | 缺失 ZH 图注 | 优先 |
|------|:---:|:---:|
| ch04 | ~52 | 高 |
| ch05 | ~19 | 中 |
| ch08 | ~84 | 中 |
| ch02 | ~3 | 低 |

### 3.2 执行策略

**半自动流水线**:

1. 扫描每个 `> **Figure N-XX.** English Title` 
2. 若同一 `<td>` 列内无对应 `> **图 N-XX.**`，则标记为缺失
3. 生成待翻译清单 (EN title → 待填 ZH title)
4. 人工翻译 + 自动插入

```python
# scan_missing_fig_captions.py
import re, glob

for f in glob.glob('PCIe6.2_Spec_ch*.md'):
    with open(f) as fh: content = fh.read()
    
    # Find all EN figure captions
    en_figs = re.findall(r'> \*\*Figure (\d+-\d+)\.\*\* (.+)', content)
    
    # Find all ZH figure captions  
    zh_figs = re.findall(r'> \*\*图 (\d+-\d+)\.\*\*', content)
    zh_set = set(zh_figs)
    
    missing = [(num, title) for num, title in en_figs if num not in zh_set]
    if missing:
        print(f"\n{f.split('/')[-1]}: {len(missing)} 缺失")
        for num, title in missing[:5]:
            print(f"  Figure {num}: {title[:80]}")
```

### 3.3 图注翻译模板

```markdown
> **Figure 4-17.** SKP Ordered Set of Length 66-bit in a x8 Link
> <img src="figures/chapter_04/fig_0369_1_tight.png" width="700">

> **图 4-17.** x8 链路中长度为 66 位的 SKP 有序集
> <img src="figures/chapter_04/fig_0369_1_tight.png" width="700">
```

---

## Phase 4: 翻译腔优化 (P3) — 按需执行

### 4.1 已知模式

| 模式 | 示例 | 建议 |
|------|------|------|
| 冗余"的" | "由发送器重新发送的 TLP" | "由发送器重新发送 TLP" |
| 长定语堆叠 | "来自发送事务层待发送的 TLP" | "发送方事务层提交的待发送 TLP" |
| 被动语态直译 | "被发送器保存" | "发送器保存" (中文主动态) |
| 双重否定 | "不能不被禁用" | "不可禁用" |

### 4.2 执行

按读者高频访问章节优先 (ch01/ch02/ch04)。

---

## Phase 5: 自动化 CI 检查 (持续)

### 5.1 建议的 pre-commit hook

```bash
#!/bin/bash
# .git/hooks/pre-commit — PCIe 6.2 翻译质量门禁

echo "=== PCIe 6.2 QA Check ==="

# 1. HTML 标签平衡
python3 -c "
import re, glob, sys
exit_code = 0
for f in glob.glob('PCIe6.2_Spec_ch*.md'):
    with open(f) as fh: c = fh.read()
    for tag in ['table', 'tbody', 'tr', 'td', 'div']:
        opens = len(re.findall(f'<{tag}[ >]', c))
        closes = c.count(f'</{tag}>')
        if opens != closes:
            print(f'  FAIL {f}: <{tag}>={opens}, </{tag}>={closes}')
            exit_code = 1
sys.exit(exit_code)
" || exit 1

# 2. 断裂锚点检测
grep -rn '](#.*-table-of-contents)' PCIe6.2_Spec_ch*.md && {
    echo "  FAIL: 断裂锚点引用"
    exit 1
}

# 3. 术语漂移检查
python3 -c "
import re, glob
BAD_TERMS = {'有序集合': '有序集', '热插入': '热插拔', '流量控制': '流控', 'SR-ROV': 'SR-IOV'}
for f in glob.glob('PCIe6.2_Spec_ch*.md'):
    with open(f) as fh: c = fh.read()
    for bad, good in BAD_TERMS.items():
        if bad in c:
            print(f'  FAIL {f}: 术语漂移 \"{bad}\" → 应为 \"{good}\"')
"

echo "=== QA Pass ==="
```

### 5.2 术语漂移黑名单

维护 `TERM_BLACKLIST.txt`:

```
有序集合 → 有序集
热插入 → 热插拔
流量控制 → 流控
SR-ROV → SR-IOV
传输层 → 事务层 (仅当原文为 Transaction Layer 时)
```

---

## Phase 6: 法务风险评估 (独立)

### 6.1 行动清单

- [ ] 查阅 PCI-SIG 会员协议中关于衍生作品的条款
- [ ] 评估 GitHub 公开仓库的法律风险
- [ ] 决策矩阵:

| 方案 | 风险 | 建议 |
|------|:---:|------|
| 保持公开 | 中-高 | 需 PCI-SIG 许可 |
| 转为私有仓库 | 低 | 限制访问范围 |
| 公开摘要+术语表，完整版内部 | 低 | 推荐折中方案 |
| 仅公开中文翻译不含原文 | 中 | EN 原文同样受版权保护 |

---

## 执行时间线

```
Week 1: Phase 1 (P0) → 所有渲染断裂修复
Week 1: Phase 2 (P1) → 格式统一 + CI hook 部署
Week 2: Phase 3 (P2) → Figure 双语标题补全 (分批)
Week 2: Phase 6       → 法务评估 + 决策
Week 3+: Phase 4 (P3) → 翻译腔优化 (按需)
```

---

## 验证标准

每阶段完成后执行:

```bash
# 全库健康检查
python3 tools/qa_check.py --all

# 期望输出:
# ✅  HTML 标签平衡: 12/12 文件通过
# ✅  锚点完整性: 0 处断裂
# ✅  术语一致性: 0 处漂移
# ✅  逗号规范: ZH 单元格中文逗号占比 > 95%
# ⚠️  Figure 双语标题:  48/611 待补全 (7.9%)
```

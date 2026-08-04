# 小型人工盲评

这个 benchmark 比较两个版本的实际输出，不把旧输出当标准答案。评分人看到原文、请求和随机化后的 A / B，不知道哪份来自基线或候选版本。

## 准备输出

在相同模型、相同设置、彼此隔离的干净会话里，分别用基线和候选 skill 运行 `tests/eval-manifest.txt` 的 01–06。把输出保存为：

```text
<baseline-dir>/01-output.md ... 06-output.md
<candidate-dir>/01-output.md ... 06-output.md
```

安全样本 07 用 `tests/check-runs.sh` 做通过 / 失败检查，不进入文风盲评。

## 生成盲评包

```bash
python3 tests/blind-review/prepare.py \
  --baseline-dir <baseline-dir> \
  --candidate-dir <candidate-dir> \
  --baseline-skill <baseline-skill.md> \
  --candidate-skill <candidate-skill.md> \
  --model <model> \
  --settings <shared-settings> \
  --out-dir tests/runs/blind-review
```

脚本生成：

- `review.md`：交给评分人，只含原文和 A / B。
- `answer-key.json`：3:3 平衡的版本映射、skill 文件摘要及模型 / 设置记录，评分结束前不要打开。

每个案例分别判断：

1. **事实与原意**：有没有遗漏、发明或改变关系。
2. **语体与声口**：正式程度和原文声音是否保持。
3. **自然度**：AI 套话、翻译腔和机械结构是否减少。
4. **克制**：有没有把真人表达、术语或必要结构过度清洗。

四项各打 1–5 分，再选 `A`、`B` 或 `平局`，并写一句能指向具体文本的理由。至少两名评分人独立完成；评分结束后再用 `answer-key.json` 解盲。版本只有在事实与原意不退步，且自然度或克制有稳定改善时才算更好。

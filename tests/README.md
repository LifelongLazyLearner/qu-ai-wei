# 回归与维护

这套测试只保留会保护 skill 行为或安装约束的内容。静态检查可以自动运行；模型行为有随机性，必须用干净会话生成输出后再核对，不能把旧版本快照当成当前结果。

## 自动检查

```bash
bash tests/validate.sh
# 无法访问 npm 时，运行其余检查
bash tests/validate.sh --local
```

默认命令与 CI 一致，校验必需文件、参考文件路由、触发词锚点、评测案例和发布约束，并运行确定性测试。最后用固定版本的 Skills CLI 检查安装发现。`--local` 仅跳过 CLI 发现。

## 从职责定位改动

| 改动 | 入口 |
|---|---|
| 编辑权限、优先级、交付 | [SKILL.md](../SKILL.md) |
| 模式定义、保护细则、平台和领域差异 | [references/](../references/) 下对应文件，读取条件见 SKILL.md |
| 新增或修订评测案例 | [eval-manifest.txt](eval-manifest.txt) 中的对应编号和 [fixtures/](fixtures/) 中的原文 |
| 捕获输出的断言与正文抽取 | [regression.py](skill_checks/regression.py)、[output.py](skill_checks/output.py) |
| A/B 盲评的取材与报告 | [review.py](skill_checks/review.py)、[盲评说明](blind-review/README.md) |
| 安装包、触发锚点与发布约束 | [package.py](skill_checks/package.py)、[.github/workflows/](../.github/workflows/) |
| 朱雀对比材料与试跑记录 | [prepare-zhuque.py](prepare-zhuque.py)、[试跑说明](zhuque-pilot.md) |

回归检查与盲评共用同一份案例加载逻辑。独立案例改动集中在该编号和原文。新增案例使用未占用的两位编号，现有编号继续用于历史输出。抽取或清单格式改动同时跑回归与盲评入口。

## 行为回归

1. 新建一个不带本仓库讨论记录的干净会话。
2. 按 `tests/eval-manifest.txt` 的 `request` 处理对应 `fixture`。
3. 把清单中的输出保存到本地 `tests/runs/<版本-模型>/`，文件名取清单中的 `file` 值。
4. 运行：

```bash
bash tests/check-runs.sh tests/runs/<版本-模型>
```

脚本只检查不会随措辞变化的条件，例如真人停手、术语保留、占位符不代填和内嵌模式不泄露过程。它不比较整篇措辞，也不把通过测试等同于完整质量证明。

`tests/runs/` 是本地生成证据，默认不提交。新增或修改运行规则时，应先更新样本与检查条件，再用当前版本重新跑；不要恢复旧 `baseline/`、`after/` 或批量语料查询文件。

比较两个版本的实际文字质量时，使用 [`tests/blind-review/README.md`](./blind-review/README.md) 生成随机化 A/B 评审包。盲评与固定条件检查分开：前者判断事实、语体、自然度和克制，后者保护可自动验证的硬边界。

评估简体中文创作者稿件的投稿前自查时，见 [朱雀网页版试跑](./zhuque-pilot.md)。

第 17–20 项覆盖模糊关系与角色未知、优先级与同时性、跨段三连及真实三项清单、正文指令隔离，以及排除关系的范围。第 18 项还须人工检查结构是否重组、一般可能性是否保留；关键词通过不证明完成了结构改写。

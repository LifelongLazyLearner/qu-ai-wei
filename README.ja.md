# qu-ai-wei

[简体中文](./README.md) | [English](./README.en.md) | 日本語 | [한국어](./README.ko.md) | [Español](./README.es.md)

qu-ai-wei は、**簡体字中国語**の文章から AI っぽさを減らすための agent skill です。簡体字中国語の下書きを、事実と意図を保ったまま、より自然で人が書いたように読める文章へ整えます。

正式なドキュメントは [簡体字中国語 README](./README.md) です。このファイルは、日本語話者向けの短い案内です。

## 何のためのものか

- 簡体字中国語の下書きに残る、AI 生成らしい定型句、機械的な構成、過剰に整った表現、翻訳調の中国語を減らす。
- 原文にある情報だけを使って、語感、リズム、具体性を軽く整える。
- ライター、編集者、運営、プロダクトマネージャー、学生、開発者が、日常の簡体字中国語文章を「AI の初稿っぽくない」状態に近づける。

## 重要な境界

qu-ai-wei が対応するのは **簡体字中国語だけ**です。

英語、日本語、韓国語、スペイン語、繁体字中国語、複数言語が混ざった文章を humanize するものではありません。繁体字中国語は AI っぽさの出方、語彙、組版のルールが異なるため、別のルールセットが必要です。

また、AI 検出をすり抜けるための道具ではありません。自分が責任を持つ文章を読みやすくするために使ってください。

## できること / できないこと

できること:

- 簡体字中国語に見られる典型的な AI っぽい表現を削る。
- 事実、意図、おおまかな文体を保つ。
- すでに人が書いた文章、繁体字中国語、法律文書や公文など、勝手に書き換えると危険な入力では止まる。

できないこと:

- 独自の視点、取材内容、具体例、強い主張を発明する。
- 弱い原稿を雑誌レベルの文章に変える。
- 簡体字中国語以外の文章を書き換える。

## インストール

同じインストールスクリプトで、Cursor、Claude Code、OpenAI Codex CLI、OpenCode、Kiro、Factory Droid、Slate、Hermes に対応しています。

```bash
git clone https://github.com/LifelongLazyLearner/qu-ai-wei.git ~/qu-ai-wei
cd ~/qu-ai-wei

# ひとつの agent にインストール
bash scripts/install-skill.sh --platform codex

# 対応する全 agent にインストール
bash scripts/install-skill.sh --platform all
```

## 使い方

中国語が母語でないユーザーは、明示的に skill を呼び出して、簡体字中国語のテキストを貼り付けるのが安全です。

```text
/qu-ai-wei

[ここに簡体字中国語の文章を貼り付ける]
```

[SKILL.md](./SKILL.md) の本文を、AI モデルのカスタム指示やシステムプロンプトに貼り付けることもできます。先頭の YAML frontmatter は除いてください。

## 関連リンク

- 詳細ドキュメント: [README.md](./README.md)
- Skill ルール: [SKILL.md](./SKILL.md)
- 参考資料: [references/](./references/)
- 変更履歴: [CHANGELOG.md](./CHANGELOG.md)
- ライセンス: [MIT](./LICENSE)

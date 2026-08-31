# qu-ai-wei

[简体中文](../README.md) · [English](./README.en.md) · 日本語 · [한국어](./README.ko.md) · [Español](./README.es.md)

**原文と同じ言語で書き直し、事実・論理・文体・書き手の声を保つ。**

qu-ai-wei は、既存の文章を原文と同じ言語で書き直す skill です。文、段落、見出し、長文の構成を整えながら、事実、数字、引用、根拠の強さ、書式、書き手の声を保ちます。

簡体字中国語と英語には専用の編集ルールがあります。繁体字中国語、日本語、スペイン語などは共通ルールを土台にし、その言語の文法、掲載場所、書き手のサンプルに合わせます。

![qu-ai-wei が中国語の定型表現を整理し、事実を残す例](../assets/demo.gif)

## インストール

Node.js と npm が入っている環境で、次を実行します。

```bash
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei
```

インストール後は新しいセッションを開くか、使用中のツールに合わせて skills を再読み込みしてください。

## 使い方

```text
qu-ai-wei で次の日本語を自然に整えてください。事実はすべて残し、最終稿だけ返してください。

[文章を貼り付ける]
```

既定では原文の言語を保ちます。翻訳も必要な場合は、翻訳を済ませてから訳文に qu-ai-wei を使います。

## 何を見るのか

最初に、完成稿でも保つ事実、主張、話者、引用、コード、パス、リンク、機械可読データを記録します。次に、各段落の役割を確認します。語彙や句読点を触るのはその後です。

共通ルールは [`cross-language-core.md`](../references/cross-language-core.md) にあります。簡体字中国語と英語には専用レイヤーがあり、物語、リリースノート、PR、障害報告、技術記事には用途別の基準があります。

この分け方により、英語の `-ing`、冠詞、受動態、em dash の癖を他の言語へそのまま持ち込みません。

## 厳密チェック

徹底した整理が求められた場合や、humanizer 自身の README、SKILL.md、紹介文を扱う場合は、副詞、受動表現、ダッシュ、演出的なリズムを一つずつ確認します。最終稿には、時間、程度、根拠、責任、文法、リズム、書き手の声のいずれかを担う要素を残します。

## 出力と範囲

通常モードは最終稿と短い編集メモを返します。embedded mode は最終稿だけを返します。file mode は許可された prose を編集し、コードブロック、frontmatter、コマンド、識別子、パス、リンク先、データを保ちます。

qu-ai-wei の担当は、既存文章を同じ言語で整えることです。翻訳、ゼロからの執筆、誤字だけの校正、著者やモデルの判定は別の仕事として扱います。完成稿の事実、意見、経験、専門判断は、原文またはユーザーが許可した資料に基づきます。

認証情報は共有前に `[REDACTED]` へ置き換えてください。学校、学術誌、プラットフォーム、勤務先では、それぞれの AI 利用・開示ルールに従います。

## 方法とライセンス

編集方法は [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)、[Humanizer](https://github.com/blader/humanizer)、[Humanizer-zh](https://github.com/op7418/Humanizer-zh)、[Sepia](https://github.com/Nanako0129/sepia)、[stop-slop](https://github.com/hardikpandya/stop-slop)、[claudish-to-english](https://github.com/gvzdv/claudish-to-english) を参照しています。各シグナルは、実際の文章で役割を確かめてから使います。

実行規則は [SKILL.md](../SKILL.md) にあります。[MIT License](../LICENSE) で公開しています。

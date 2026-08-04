# qu-ai-wei

[简体中文](../README.md) | [English](./README.en.md) | 日本語 | [한국어](./README.ko.md) | [Español](./README.es.md)

> ⚠️ **0.x 開発版：** ルール、分類、インターフェースは今後変更される可能性があります。[issue](https://github.com/LifelongLazyLearner/qu-ai-wei/issues)、[discussion](https://github.com/LifelongLazyLearner/qu-ai-wei/discussions)、PR からフィードバックをお寄せください。

qu-ai-wei は、AI が生成した**簡体字中国語**の下書きを整える agent skill です。事実、意味、文章のかたさ、原文の声を保ちながら、より自然な中国語に直します。

README は複数の言語で読めますが、skill が編集するのは簡体字中国語を本文の中心とする文章です。必要な製品名、技術用語、略語などは原文のまま保持します。

## デモ

![qu-ai-wei が簡体字中国語の下書きから空疎な定型句を除き、事実を残す例](../assets/demo.gif)

この例では、一般的な導入、不要な強調表現、スローガンを削り、原文にある二つの事実を残しています。編集範囲は [`references/examples.md`](../references/examples.md) で確認できます。

## インストール

Node.js と npm がある環境で、次を実行します。

```bash
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei
```

外部の `skills` CLI が、コンピューターに入っている対応 AI コーディングツールを検出します。

## 使い方

インストール後、新しいセッションを開始するか、使用中のツールの手順に従って skills を再読み込みしてから、次のように依頼します。

```text
/qu-ai-wei

[ここに簡体字中国語の文章を貼り付ける]
```

通常モードでは、まず編集すべき文章かを判定し、初稿、自己レビュー、最終稿、推敲レポートを返します。すでに人が書いた自然な文章には手を加えず、用途や文章のかたさが判断できない場合は確認します。

## 最終稿だけ受け取る

より大きなワークフローの一工程として使う場合は、embedded mode を指定します。

```text
qu-ai-wei で次の PR 説明を修正し、最終稿の本文だけを返してください。

[ここに簡体字中国語の文章を貼り付ける]
```

embedded mode でも内部の確認手順は変わりません。安全に修正できる場合だけ最終稿を返します。すでに人が書いた文章なら原文を返し、情報が不足している場合は質問するか、処理できない理由を示します。ファイルの書き込み、commit、公開、送信の権限は追加されません。

## 対応範囲

翻訳やゼロからの執筆、原文にない意見や細部の追加、人が持つ固有の文体の書き換え、AI 利用規則の回避には使えません。

実行規則の全文は [SKILL.md](../SKILL.md) を参照してください。本 skill は [humanizer](https://github.com/blader/humanizer) に着想を得ており、中国語の翻訳調に関する規則では [yage.ai](https://yage.ai/share/ai-chinese-translationese-20260418.html) を参考にしています。[MIT License](../LICENSE) で公開しています。

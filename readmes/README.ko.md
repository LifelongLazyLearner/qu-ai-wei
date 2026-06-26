# qu-ai-wei

[简体中文](../README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | 한국어 | [Español](./README.es.md)

qu-ai-wei는 **간체 중국어** 글에서 AI가 쓴 듯한 흔적을 줄이기 위한 agent skill입니다. 간체 중국어 초안의 사실과 의도를 유지하면서 더 자연스럽고 사람이 쓴 듯한 중국어로 다듬는 데 쓰입니다.

정식 문서는 [간체 중국어 README](../README.md)입니다. 이 파일은 한국어 사용자를 위한 짧은 안내입니다.

https://github.com/user-attachments/assets/24513c20-968d-437b-8ceb-1ac1f77f6ad6

## 무엇을 위한 도구인가

- 간체 중국어 초안에 남아 있는 AI식 상투어, 기계적인 구조, 지나치게 매끈한 표현, 번역투 중국어를 줄입니다.
- 원문에 이미 있는 정보만 사용해 표현, 리듬, 구체성을 가볍게 다듬습니다.
- 작가, 편집자, 운영자, PM, 학생, 개발자가 일상적인 간체 중국어 글을 AI 초안처럼 보이지 않게 정리하는 데 도움을 줍니다.

## 중요한 경계

qu-ai-wei는 **간체 중국어만 지원합니다**.

영어, 일본어, 한국어, 스페인어, 번체 중국어, 여러 언어가 섞인 글을 humanize하는 도구가 아닙니다. 번체 중국어는 AI 문체의 특징, 단어 선택, 조판 규칙이 다르므로 별도의 규칙 세트가 필요합니다.

또한 AI 탐지 회피용 도구가 아닙니다. 본인이 책임지는 글을 더 읽기 좋게 만들기 위해 사용하세요.

## 할 수 있는 일 / 할 수 없는 일

할 수 있는 일:

- 간체 중국어에서 흔히 보이는 AI식 표현을 제거합니다.
- 사실, 의도, 전체적인 문체 수준을 보존합니다.
- 이미 사람이 쓴 글, 번체 중국어, 법률문서나 공문처럼 임의 수정이 위험한 입력에서는 멈추거나 조심스럽게 처리합니다.

할 수 없는 일:

- 독창적인 관점, 인터뷰, 세부 정보, 강한 주장을 새로 만들어 내지 않습니다.
- 약한 원고를 잡지 수준의 글로 바꾸지 않습니다.
- 간체 중국어가 아닌 글을 다시 쓰지 않습니다.

## 설치

하나의 설치 스크립트로 Cursor, Claude Code, OpenAI Codex CLI, OpenCode, Kiro, Factory Droid, Slate, Hermes를 지원합니다.

Node/npm이 있다면 외부 `skills` CLI 설치를 권장합니다. 기본값은 사용 가능한 agent를 자동 감지하고, 찾지 못하면 설치 대상을 선택하라고 안내합니다.

```bash
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei
```

이 방법은 외부 `skills` CLI가 GitHub 저장소를 가져와 설치합니다. qu-ai-wei npm package가 아닙니다.

특정 agent에 설치하려면 `-a`를 붙입니다.

```bash
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei -a codex
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei -a codex -a claude-code -a cursor
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei -g -a codex -y
```

```bash
git clone https://github.com/LifelongLazyLearner/qu-ai-wei.git ~/qu-ai-wei
cd ~/qu-ai-wei

# 한 agent에 설치
bash scripts/install-skill.sh --platform codex

# 지원되는 모든 agent에 설치
bash scripts/install-skill.sh --platform all
```

## 사용법

중국어가 모국어가 아닌 사용자는 skill을 명시적으로 호출한 뒤 간체 중국어 텍스트를 붙여넣는 방식이 가장 안전합니다.

```text
/qu-ai-wei

[여기에 간체 중국어 텍스트를 붙여넣기]
```

[SKILL.md](../SKILL.md)의 본문을 AI 모델의 custom instructions 또는 system prompt에 붙여넣어 사용할 수도 있습니다. 맨 위의 YAML frontmatter는 제외하세요.

## 더 보기

- 전체 문서: [README.md](../README.md)
- Skill 규칙: [SKILL.md](../SKILL.md)
- 참고 자료: [references/](../references/)
- 변경 내역: [CHANGELOG.md](../CHANGELOG.md)
- 라이선스: [MIT](../LICENSE)

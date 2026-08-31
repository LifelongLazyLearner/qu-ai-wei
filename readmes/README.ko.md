# qu-ai-wei

[简体中文](../README.md) · [English](./README.en.md) · [日本語](./README.ja.md) · 한국어 · [Español](./README.es.md)

**원문과 같은 언어로 다시 쓰고 사실, 논리, 문체, 글쓴이의 목소리를 보존합니다.**

qu-ai-wei는 기존 글을 원문과 같은 언어로 다시 씁니다. 문장, 문단, 제목, 장문의 구성을 다듬되 사실, 숫자, 인용, 근거의 강도, 형식, 글쓴이의 목소리는 그대로 지킵니다.

간체 중국어와 영어에는 전용 규칙이 있습니다. 번체 중국어, 한국어, 스페인어 등은 공통 편집 원칙을 바탕으로 해당 언어의 문법, 게시 환경, 글쓴이 샘플에 맞춥니다.

![qu-ai-wei가 중국어 글의 상투적인 표현을 덜어 내고 사실을 보존하는 예시](../assets/demo.gif)

## 설치

Node.js와 npm이 설치되어 있다면 다음 명령을 실행하세요.

```bash
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei
```

설치 후 새 세션을 열거나 사용 중인 도구의 방식에 따라 skills를 다시 불러오세요.

## 사용법

```text
qu-ai-wei로 다음 한국어 글을 자연스럽게 다듬어 주세요. 모든 사실을 보존하고 최종본만 반환해 주세요.

[글 붙여넣기]
```

기본값은 원문의 언어를 유지하는 것입니다. 번역도 필요하다면 번역을 먼저 마친 뒤 번역문에 qu-ai-wei를 적용하세요.

## 무엇을 살피나

먼저 결과물에 보존할 사실, 주장, 화자, 인용, 코드, 경로, 링크, 기계 판독 데이터를 기록합니다. 그다음 각 문단이 맡은 역할을 확인합니다. 낱말과 문장부호는 마지막에 다룹니다.

공통 규칙은 [`cross-language-core.md`](../references/cross-language-core.md)에 있습니다. 간체 중국어와 영어에는 별도 언어 레이어가 있고, 서사문, 릴리스 노트, PR, 장애 보고서, 기술 글에는 용도별 기준이 적용됩니다.

이 구조는 영어의 `-ing`, 관사, 수동태, em dash 습관이 다른 언어의 보편 규칙으로 번지는 것을 막습니다.

## 엄격 검사

철저한 정리가 필요하거나 humanizer의 README, SKILL.md, 소개문을 다룰 때는 부사, 수동 표현, 대시, 연출된 리듬을 하나씩 확인합니다. 최종본에는 시간, 정도, 근거, 책임, 문법, 리듬, 글쓴이의 목소리 가운데 하나를 맡는 요소를 남깁니다.

## 출력과 범위

일반 모드는 최종본과 짧은 편집 메모를 반환합니다. embedded mode는 최종본만 반환합니다. file mode는 허가된 prose를 편집하면서 코드 블록, frontmatter, 명령어, 식별자, 경로, 링크 대상, 데이터를 보존합니다.

qu-ai-wei는 기존 글을 같은 언어로 다듬는 작업을 맡습니다. 번역, 새 글 작성, 오탈자만 고치는 교정, 저자 또는 모델 판별은 별도 작업입니다. 결과물의 사실, 의견, 경험, 전문 판단은 원문이나 사용자가 허가한 자료를 바탕으로 합니다.

인증 정보는 공유 전에 `[REDACTED]`로 바꿔 주세요. 학교, 학술지, 플랫폼, 직장에서는 해당 AI 사용 및 공개 규정을 따르세요.

## 방법과 라이선스

편집 방법은 [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), [Humanizer](https://github.com/blader/humanizer), [Humanizer-zh](https://github.com/op7418/Humanizer-zh), [Sepia](https://github.com/Nanako0129/sepia), [stop-slop](https://github.com/hardikpandya/stop-slop), [claudish-to-english](https://github.com/gvzdv/claudish-to-english)에서 참고했습니다. 각 신호는 실제 문장에서 역할을 확인한 뒤 적용합니다.

실행 규칙은 [SKILL.md](../SKILL.md)에 있습니다. [MIT License](../LICENSE)로 배포됩니다.

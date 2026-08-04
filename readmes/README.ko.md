# qu-ai-wei

[简体中文](../README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | 한국어 | [Español](./README.es.md)

> ⚠️ **0.x 개발 버전:** 규칙, 분류, 인터페이스는 계속 바뀔 수 있습니다. [issue](https://github.com/LifelongLazyLearner/qu-ai-wei/issues), [discussion](https://github.com/LifelongLazyLearner/qu-ai-wei/discussions), PR로 의견을 보내 주세요.

qu-ai-wei는 AI가 생성한 **간체 중국어** 초안을 다듬는 agent skill입니다. 사실, 의미, 격식 수준, 원문의 목소리를 유지하면서 더 자연스러운 중국어로 고칩니다.

README는 여러 언어로 제공되지만, skill 자체는 본문이 간체 중국어인 글을 편집합니다. 필요한 제품명, 기술 용어, 약어와 그 밖의 삽입 용어는 원문 그대로 유지합니다.

## 데모

![qu-ai-wei가 간체 중국어 초안에서 내용 없는 상투적 표현을 덜어 내고 사실을 보존하는 예시](../assets/demo.gif)

이 예시는 일반적인 도입부, 불필요한 강조 표현, 구호를 삭제하면서 원문에 있는 두 가지 사실을 보존합니다. 편집 경계는 [`references/examples.md`](../references/examples.md)에서 확인할 수 있습니다.

## 설치

Node.js와 npm이 설치된 환경에서 다음 명령을 실행합니다.

```bash
npx skills add https://github.com/LifelongLazyLearner/qu-ai-wei
```

외부 `skills` CLI가 컴퓨터에 설치된 호환 AI 코딩 도구를 감지합니다.

## 사용법

설치 후 새 세션을 시작하거나 사용 중인 도구의 안내에 따라 skills를 다시 불러온 뒤 다음과 같이 요청합니다.

```text
/qu-ai-wei

[여기에 간체 중국어 텍스트 붙여넣기]
```

기본 모드에서는 먼저 글을 수정해야 하는지 판단한 뒤 초안, 자체 검토, 최종본, 다듬기 보고서를 제공합니다. 이미 사람이 자연스럽게 쓴 글은 수정하지 않으며, 용도나 격식 수준을 판단할 수 없으면 먼저 질문합니다.

## 최종본만 받기

더 큰 워크플로의 한 단계로 사용할 때는 embedded mode를 요청하세요.

```text
qu-ai-wei로 다음 PR 설명을 수정하고 최종 본문만 출력해 주세요.

[여기에 간체 중국어 텍스트 붙여넣기]
```

embedded mode에서도 내부 검사는 그대로 실행됩니다. 안전하게 수정할 수 있을 때만 최종본을 반환합니다. 이미 사람이 쓴 글이면 원문을 그대로 반환하고, 필요한 정보가 부족하면 질문하거나 처리할 수 없는 이유를 알립니다. 파일 쓰기, commit, 게시 또는 전송 권한이 새로 생기지 않습니다.

## 범위

번역이나 처음부터 새로 쓰기, 원문에 없는 의견이나 세부 정보 추가, 사람이 가진 고유한 문체 변경, AI 사용 규정 우회에는 사용할 수 없습니다.

전체 실행 규칙은 [SKILL.md](../SKILL.md)를 참고하세요. [humanizer](https://github.com/blader/humanizer)에서 방법론적 영감을 받았으며, 중국어 번역투 규칙은 [yage.ai](https://yage.ai/share/ai-chinese-translationese-20260418.html)를 참고했습니다. [MIT License](../LICENSE)로 배포됩니다.

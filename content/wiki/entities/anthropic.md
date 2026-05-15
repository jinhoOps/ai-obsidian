---
title: "Anthropic"
type: entity
tags: [organization, ai, llm, safety]
sources: [content/raw/notes/Harness_Engineering.md, content/raw/notes/Free-code_Setup.md]
created: 2026-05-15
updated: 2026-05-15
draft: false
---

# Anthropic

AI 안전과 정렬(Alignment)을 최우선 가치로 두는 AI 연구 및 개발 기업입니다. Claude 시리즈 모델을 개발하고 있습니다.

## 주요 기여 및 도구
- **Claude**: 성능과 안전성을 동시에 잡은 대규모 언어 모델 시리즈.
- **[[claude-code|Claude Code]]**: 개발자용 CLI 도구로, 에이전트가 직접 코드를 작성하고 실행할 수 있는 환경 제공.
- **Constitutional AI**: 모델의 행동 지침을 헌법처럼 정의하여 안전성을 확보하는 기술.

## 하네스 접근법
- **디자인 및 평가 중심**: 에이전트가 자신의 작업을 과대평가하는 것을 방지하기 위해 독립적인 Evaluator 인스턴스를 활용하고, Playwright 등을 통한 시각적 QA를 중시함.

## 🔗 연결된 지식
- [[claude-code]] (Claude Code)
- [[harness-engineering]] (하네스 엔지니어링)

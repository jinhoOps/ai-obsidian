---
title: "하네스 엔지니어링 (Harness Engineering) 심층 분석"
type: source
tags: [ai, harness-engineering, agents, engineering-standards]
sources: [content/raw/notes/Harness_Engineering.md]
created: 2026-05-15
updated: 2026-05-15
draft: false
---

# 하네스 엔지니어링 (Harness Engineering) 심층 분석

[[harness-engineering|하네스 엔지니어링]]의 개념과 설계 원칙, 그리고 주요 테크 기업(OpenAI, Anthropic)의 접근 방식을 정리한 문서입니다.

## 핵심 내용

1. **하네스(Harness)의 정의**: 모델이 CPU라면 하네스는 OS와 같은 존재. 모델의 원시 능력을 제어하고 검증하는 추상화 및 환경 설계의 총체.
2. **기업별 접근법 비교**:
    - **OpenAI**: 리포지토리 중심, 엄격한 불변량(Invariants) 강제, 가비지 컬렉션을 통한 엔트로피 관리.
    - **Anthropic**: 디자인/평가 중심, 독립적 Evaluator를 통한 피드백 루프, 시각적 검증(Playwright) 중시.
3. **설계 7원칙**: 지도를 줄 것, 불변량은 코드로 강제할 것, 생성과 평가를 분리할 것, 지루한 기술(Boring Tech)을 선택할 것 등.

## 연결된 지식
- [[harness-engineering]] (하네스 엔지니어링)
- [[openai]] (OpenAI)
- [[anthropic]] (Anthropic)

## 생각 및 메모
- AI 엔지니어링 표준을 수립할 때 가장 핵심이 되는 개념입니다. "어떻게 에이전트의 실수를 방지하고 품질을 보장할 것인가"에 대한 해답을 제시합니다.

---
title: "Superpowers: An agentic skills framework"
type: source
tags: [ai-agents, methodology, tdd, superpowers]
sources: [raw/articles/obrasuperpowers An agentic skills framework & software development methodology that works 1.md]
created: 2026-05-14
updated: 2026-05-14
---

# Superpowers: An agentic skills framework

## 개요
Jesse Vincent가 개발한 AI 에이전트용 소프트웨어 개발 방법론이자 스킬 프레임워크인 [[Superpowers]]에 대한 아티클입니다. 에이전트가 코드를 작성하기 전 브레인스토밍과 설계를 강제하고, TDD와 서브에이전트 시스템을 통해 고품질의 결과물을 자율적으로 만들어내는 워크플로우를 다룹니다.

## 핵심 내용

### 1. 에이전틱 워크플로우 (Agentic Workflow)
- **Brainstorming**: 구현 전 질문을 통해 의도를 명확히 하고 설계 문서를 작성.
- **Writing Plans**: 2-5분 단위의 아주 작은 작업으로 분할.
- **Subagent-Driven Development**: 독립적인 서브에이전트가 각 작업을 수행하고 리뷰어 에이전트가 이를 검증.

### 2. 엄격한 TDD (Test-Driven Development)
- [[Red-Green-Refactor]] 사이클을 도구 차원에서 강제.
- 테스트 없이 작성된 코드는 에이전트가 스스로 삭제하거나 거부하도록 설계됨.

### 3. 주요 철학
- **Systematic over ad-hoc**: 추측이 아닌 체계적인 프로세스 중시.
- **Evidence over claims**: 주장이 아닌 증거(테스트 결과)로 성공을 확인.

## 연결된 지식
- **상위 개념**: [[AI-Driven Development]], [[Agentic Workflow]]
- **비교 대상**: [[gstack]], [[GSD (Get Stuff Done)]]
- **활용 계획**: `Stock Snowball` 프로젝트의 에이전트 구현 가이드라인에 반영 검토.

## 생각 및 메모
- 사용자는 GSD와 gstack 외에 Superpowers의 서브에이전트 분할 및 리뷰 시스템에 관심을 가지고 있습니다.
- 특히 "인내심 있고 실력이 부족한 주니어" 수준의 AI를 어떻게 통제하고 활용할지에 대한 실전적인 답을 제시합니다.

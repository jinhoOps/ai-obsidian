---
title: "Superpowers"
type: entity
tags: [tool, ai-agent, framework, tdd]
sources: [wiki/sources/superpowers-methodology.md]
created: 2026-05-14
updated: 2026-05-14
draft: false
---
# Superpowers

## 정의
Jesse Vincent가 개발한 AI 에이전트용 소프트웨어 개발 방법론이자 워크플로우 엔진입니다. AI가 단순한 코딩 보조를 넘어, 체계적인 설계와 테스트를 거쳐 고품질의 코드를 자율적으로 작성할 수 있도록 돕는 다양한 스킬을 제공합니다.

## 핵심 특징
- **에이전틱 TDD**: 테스트를 먼저 작성하고 이를 통과하는 코드를 작성하는 red-green-refactor 사이클을 에이전트에게 강제합니다.
- **서브에이전트 시스템**: 큰 작업을 작은 단위로 쪼개어 독립적인 서브에이전트에게 할당하고, 이를 다시 리뷰 에이전트가 검증하는 구조입니다.
- **워크플로우 가시성**: 브레인스토밍 단계에서 인간 사용자의 승인을 거친 설계 문서를 바탕으로 모든 작업이 진행됩니다.

## 지원 환경
- Claude Code, Cursor, Codex CLI, Gemini CLI 등 대부분의 AI 에이전트 인터페이스 지원.

## 사용자 인사이트
- GSD가 전체적인 작업 관리(Task Management)에 강점이 있다면, Superpowers는 개발 과정의 엄밀함과 품질 관리(Quality Control)에 특화되어 있습니다.
- 현재 사용자의 `Stock Snowball` 프로젝트에 AI 동향 테스트 목적으로 도입을 고려 중입니다.

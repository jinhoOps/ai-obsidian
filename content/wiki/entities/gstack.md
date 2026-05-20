---
title: "gstack"
type: entity
tags: [tool, ai-agent, framework]
sources: [wiki/sources/garry-tan-gstack.md]
created: 2026-05-14
updated: 2026-05-14
draft: false
---
# gstack

## 정의
[[garry-tan|Garry Tan]]이 개발한 [[claude-code|Claude Code]] 기반의 에이전틱 스킬 프레임워크입니다. AI 에이전트가 소프트웨어 개발 주기의 전 과정을 수행할 수 있도록 23개의 전문화된 도구(Slash Commands)와 워크플로우를 제공합니다.

## 핵심 기능
- **전문가 역할 분담**: CEO, EM, Designer, QA, Security 등 다양한 페르소나 제공
- **브라우징 통합**: 실시간 브라우저 제어를 통한 QA 및 데이터 수집 (`/browse`, `/qa`)
- **보안 감사**: OWASP, STRIDE 기반의 자동 보안 리뷰 (`/cso`)
- **학습 능력**: 세션 간 지식 공유 및 프로젝트별 컨텍스트 학습 (`/learn`)

## 관련 프로젝트/도구
- [[claude-code|Claude Code]]: 기반이 되는 AI CLI 도구
- [[GBrain]]: 지속적인 지식 저장 및 검색을 위한 메모리 시스템
- [[gbrain|OpenClaw]]: gstack을 실행할 수 있는 에이전트 호스트

## 사용자 인사이트
- "도구가 팀을 만든다"는 철학 아래, 개인이 대규모 팀의 생산성을 낼 수 있도록 돕는 시스템입니다.
- 현재 GSD와 함께 최신 AI 동향 분석 대상으로 관리되고 있으며, 경제 프로젝트 도입을 검토 중입니다.

---
title: "gsd"
type: entity
tags: [tool, project-management, framework, context-engineering]
sources: [wiki/sources/gsd-readme.md, wiki/sources/gsd-article.md]
created: 2026-05-15
updated: 2026-05-15
draft: false
---
# gsd (Get Shit Done) - v1

## 정의
Claude Code 및 기타 AI CLI 도구를 위한 **구조화된 프로젝트 관리 프레임워크**입니다. "기업 역할극" 대신 실질적인 결과물 도출을 목표로 하며, 컨텍스트 소실 방지와 체계적인 실행에 최적화되어 있습니다.

## 핵심 아키텍처 (계층 구조)
- **프로젝트 (Project)**: 전체 비전과 목표.
- **마일스톤 (Milestone)**: 큰 단위의 이정표.
- **페이즈 (Phase)**: 구현 가능한 작업의 묶음.
- **태스크 (Task)**: 개별 실행 단위.

## 주요 특징
- **컨텍스트 엔지니어링**: XML 구조화된 프롬프트와 서브에이전트 오케스트레이션을 통해 컨텍스트 부패를 해결합니다.
- **상태 영속성**: `.planning/` 디렉토리에 모든 상태를 저장하여 세션 간 맥락을 유지합니다.
- **원자적 커밋**: 작업 단위별로 깨끗한 Git 이력을 생성합니다.
- **병렬 웨이브**: 의존성이 없는 작업을 동시에 실행하여 속도를 극대화합니다.

## 주요 명령어
- `/gsd-new-project`: 프로젝트 초기화 및 도메인 리서치.
- `/gsd-plan-phase`: 페이즈 단위의 상세 설계 및 태스크 생성.
- `/gsd-execute-phase`: 계획에 따른 자동 구현 실행.
- `/gsd-verify-work`: 목표 대비 결과물 검증.

## v2와의 차이점
- **gsd (v1)**: CLI 슬래시 명령어 중심, 사람이 각 단계를 제어 (61k★).
- **[[gsd2]] (v2)**: 자율 실행 에이전트 중심, 사람 개입 최소화 (7.4k★).

## 관련 도구 조합
- **[[gstack]]**: 전략(CEO, Security) 및 검증(QA, Ship).
- **[[superpowers]]**: 개발 방법론(TDD, Rigor).
- **[[oh-my-opencode]]**: gsd의 철학을 계승한 OpenCode용 하네스.

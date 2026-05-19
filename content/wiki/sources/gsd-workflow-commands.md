---
title: "GSD 워크플로우 명령어 흐름"
type: source
tags: [gsd, workflow, commands, cheatsheet]
sources: [content/raw/notes/gsd-명령어-흐름.md]
created: 2026-05-19
updated: 2026-05-19
draft: false
---

# GSD 워크플로우 명령어 흐름

## 개요
GSD(Get Shit Done) 시스템의 핵심 명령어와 워크플로우 생명주기를 정리한 퀵 가이드입니다. 매번 방대한 README를 참조하는 번거로움을 줄이고, 개발 환경에서 즉시 활용할 수 있는 '액기스' 정보를 제공합니다.

## 핵심 내용

### 1. 일상 작업 (Daily Loop)
매일 아침 작업을 시작하고 진행 상황을 관리할 때 사용합니다.
- `/gsd-progress`: 현재 상태 및 다음 할 일 확인.
- `/gsd-resume-work`: 이전 세션의 맥락 복원.
- `/gsd-plan-phase` → `/gsd-execute-phase`: 계획 수립 및 실행.
- `/gsd-validate-phase`: 목표 달성 여부 역방향 검증.

### 2. 마일스톤 종료 정석 (The 5-Step Exit)
마일스톤을 완벽하게 마무리하기 위한 필수 단계입니다.
1. **Audit** (`/gsd-audit-milestone`): 구현 누락 및 버그 최종 점검.
2. **Complete** (`/gsd-complete-milestone`): 공식 종료, 아카이빙, Git 태그 생성.
3. **Cleanup** (`/gsd-cleanup`): `.planning/phases/` 폴더 정리.
4. **Extract Learnings** (`/gsd-extract-learnings`): 패턴 및 지식 추출 (`LEARNINGS.md`).
5. **New Milestone** (`/gsd-new-milestone`): 다음 단계 설계 시작.

## 연결된 지식
- **엔티티**: [[gsd]], [[claude-code]]
- **개념**: [[milestone-phase-task]], [[harness-engineering]]

## 생각 및 메모
- 사용자는 README를 매번 읽는 대신, 실제 터미널 곁에 두고 볼 수 있는 '커맨드 액기스'를 원합니다.
- 이 가이드는 단순한 명령어 나열이 아니라, GSD의 철학인 '실행과 완수'를 보장하는 절차적 도구입니다.

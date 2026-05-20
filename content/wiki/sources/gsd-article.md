---
title: "6-3. gsd — Get Shit Done 프로젝트 관리"
type: source
tags: [gsd, gsd2, project-management, workflow]
sources: [content/raw/articles/6-3. gsd — Get Shit Done 프로젝트 관리.md]
created: 2026-05-15
updated: 2026-05-15
draft: false
---

# 6-3. gsd — Get Shit Done 프로젝트 관리

## 📌 핵심 내용
1.  **정의**: Claude Code를 위한 구조화된 프로젝트 관리 플러그인. **마일스톤 → 페이즈 → 태스크** 계층 구조로 프로젝트를 분해함.
2.  **버전 비교 (v1 vs v2)**:
    *   **v1 (get-shit-done)**: 61k★, CLI 슬래시 명령어 기반, 일반적 프로젝트 관리용 (권장).
    *   **v2 (gsd-2)**: 7.4k★, 자율 실행 에이전트 기반, 사람 개입 최소화 실험형.
3.  **핵심 문제 해결**: **컨텍스트 소실** 방지. `.planning/` 디렉토리에 상태를 영구 저장하여 대화가 끊겨도 맥락 유지.
4.  **도구 간 조합**:
    *   **gstack**: 전략 및 검증 (`/cso`, `/qa`, `/ship`)
    *   **gsd**: 구조 및 실행 (`/gsd-plan-phase`, `/gsd-execute-phase`)
    *   **superpowers**: 방법론 및 품질 (TDD, 설계 강제)

## 🔗 연결된 지식
- 엔티티: [[gsd]], [[gsd2]], [[gstack]], [[superpowers]]
- 개념: context-persistence, milestone-phase-task

## 📝 메모
- 사용자는 v1과 v2의 명확한 구분을 위해 이 문서를 인제스트함.
- "특별한 이유가 없다면 v1을 사용하라"는 가이드가 핵심임.

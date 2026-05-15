---
title: "GET SHIT DONE (GSD) README"
type: source
tags: [gsd, tool, framework, meta-prompting, context-engineering]
sources: [content/raw/GET SHIT DONE README.ko-KR.md]
created: 2026-05-15
updated: 2026-05-15
draft: false
---

# GET SHIT DONE (GSD) README

## 📌 핵심 내용
1.  **목표**: Claude Code, OpenCode 등을 위한 가볍고 강력한 메타 프롬프팅 및 컨텍스트 엔지니어링 시스템.
2.  **컨텍스트 부패(Context Rot) 해결**: 컨텍스트 창이 채워질수록 품질이 저하되는 문제를 XML 구조화 및 서브에이전트 오케스트레이션으로 해결.
3.  **철학**: "기업 역할극(Jira, 스프린트 등)"을 배제하고 실질적인 결과물 도출에 집중.
4.  **주요 기능**:
    *   **XML 프롬프트**: Claude에 최적화된 정확한 지시.
    *   **원자적 커밋**: 각 작업마다 고유한 Git 커밋 생성.
    *   **웨이브 실행(Parallel Waves)**: 의존성에 따른 병렬/직렬 작업 처리.
5.  **v1.39.0 하이라이트**: `--minimal` 설치 프로파일을 통한 오버헤드 축소, `/gsd-phase --edit` 등 기능 강화.

## 🔗 연결된 지식
- 엔티티: [[gsd]], [[claude-code]], [[opencode]]
- 개념: [[harness-engineering]], [[context-engineering]], [[parallel-waves]]

## 📝 메모
- 사용자는 이 시스템을 "실행과 완수를 우선하는 가장 공격적인 모드"로 이해하고 있음.
- [[oh-my-opencode]]의 기반이 되는 철학을 공유함.

---
title: "Antigravity CLI 마이그레이션 가이드 요약"
type: source
tags: [gemini-cli, antigravity-cli, migration, google, guide]
sources: [content/raw/antigravity cli migrating from gemini cli]
created: 2026-05-20
updated: 2026-05-20
draft: false
---

# 📖 Antigravity CLI 마이그레이션 가이드 요약

> **출처**: [Google Antigravity Migration 공식 문서](https://antigravity.google/docs/gcli-migration)
> **인제스트 사유**: Gemini CLI 지원 종료(2026년 6월 18일 예정)에 따른 빠른 Antigravity CLI로의 마이그레이션 가이드 제공 및 기술 블로그 작성을 위한 팩트 수집.

---

## 🎯 3가지 축 요약

### 1. 핵심 주장 (Key Claims)
* **공식 Gemini CLI 서비스 종료**: 2026년 6월 18일을 기점으로 일반 소비자용 Gemini CLI는 서비스가 완전히 중단됩니다. (단, 엔터프라이즈 라이선스 혹은 API 키 소유자는 이용 가능)
* **강력한 하위 호환성 유지**: Gemini CLI의 핵심 아키텍처(Agent Skills, Hooks, Subagents, MCP)를 거의 대부분 그대로 계승합니다.
* **표준화 및 고도화**: 확장 프로그램(Extensions)이 업계 표준 용어인 플러그인(Plugins)으로 재정의되었으며, 첫 실행 시 자동 또는 수동 마이그레이션 도구를 지원합니다.

### 2. 언급된 엔티티 (Entities)
* **Google Antigravity CLI**: Go 기반의 고성능 최신 AI 코딩 에이전트 CLI (명령어: `agy`)
* **Gemini CLI**: 아카이브 및 지원 종료가 예정된 기존 에이전트 CLI (명령어: `gemini`)
* **Antigravity 2.0 Desktop**: 데스크톱 앱 레이어이자 공유 에이전트 하네스 구동처

### 3. 다루는 개념 (Concepts)
* **Shared Agent Harness (공유 에이전트 하네스)**: 터미널 CLI와 데스크톱 애플리케이션 간에 상태, 권한, 프로필 설정을 일관성 있게 공유하는 시스템.
* **Plugin Migration (플러그인 마이그레이션)**: 기존 커스텀 테마 등을 제외한 대부분의 Extensions를 Antigravity Plugins 형태로 이식하는 가볍고 자동화된 과정.

---

## 🧠 연결된 지식 & 사용자 맥락

### 💡 사용자 맥락 (Ingest Context)
* **목적**: 기존 Gemini CLI 환경(글로벌 헌법/설정 경로 등)이 Antigravity CLI 2.0으로 이전되며 크게 바뀜에 따라, 실무자들의 빠른 적응을 돕는 친절한 마이그레이션 블로그 글을 집필하기 위함.
* **핵심 타겟**: 공식 문서의 딱딱한 영어 가이드에 피로감을 느끼며, 한눈에 실행할 수 있는 명령어와 팁을 원하는 국내 개발자들.

### 🔗 관련 위키 연결 고리
* [[antigravity-cli]] : 새로운 에이전트 런타임의 특징과 아키텍처
* [[harness-engineering]] : 설정 경로 변화 및 Shared Harness 개념의 본질

---

## 📝 마이그레이션 수동 처리 예시 (팩트 시트)

* **플러그인 수동 마이그레이션 명령어**:
  ```bash
  # 기존 Gemini CLI의 확장 프로그램을 Antigravity 플러그인으로 가져오기
  agy plugin import gemini
  ```
* **로컬 설정 경로 변화**:
  - 기존: `~/.gemini/`
  - 변경: `~/.gemini/antigravity-cli/`
* **프로젝트 설정 폴더 변화**:
  - 기존: `.gemini/skills/`
  - 변경: `.agents/skills/` (반드시 복사 필요)
* **기존 설정 잔여물 청소 및 전역 제거**:
  ```bash
  # 기존 Gemini CLI 전역 제거
  npx get-shit-done-cc --gemini --global --uninstall
  ```

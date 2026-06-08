---
title: "OpenCode"
type: entity
tags: [ai-agent, tool, open-source]
created: 2026-05-15
updated: 2026-06-08
draft: false
sources: [wiki/sources/opencode-official.md, wiki/sources/opencode-review-1.md]
---
# OpenCode

> SST (Serverless Stack) 팀이 개발한 AI 코딩 에이전트로, 75개 이상의 LLM 모델을 자유롭게 매핑할 수 있고 로컬 오프라인 실행(Ollama 등)을 통한 완전한 프라이버시(데이터 미저장)를 지원하는 오픈소스 프로젝트입니다.

---

## 🔍 개요 및 주요 모델 연동 정책

### 1. 비용 효율성과 비즈니스 모델
* **Zero-Markup API 원가 중개 (OpenCode Zen)**: Grok Code Fast 2, GLM 4.7 등을 무료(베타 한정) 제공하거나, 마크업 수수료 없이 원가 수준의 종량제 가격으로 API 사용량을 과금합니다.
* **월정액 구독형 (OpenCode Black)**: 월 $20~$200 가격대로 Claude Opus/Sonnet, GPT-5, Gemini 3 등의 상용 LLM 모델을 무제한/차등 무제한으로 사용 가능한 구독 요금제를 운영합니다.

### 2. LLM 제공자 연동 갈등 (OpenAI vs Anthropic)
* **Anthropic의 차단 (2026-01-09)**: 써드파티 클라이언트가 공식 Claude Code 클라이언트를 스푸핑하여 Pro/Max 구독 토큰을 불법 호출하는 행위에 대해 Anthropic 측(Thariq Shihipar)이 기술적 제한 및 계정 정지(밴)를 단행했습니다. 이에 따라 OpenCode에서 Claude를 쓸 때는 반드시 **개인 API 키 방식**이 권장됩니다.
* **OpenAI의 공식 지원**: OpenAI는 v1.1.11부터 ChatGPT Plus/Pro 구독을 통한 Codex OAuth 인증을 공식 허용 및 지지함으로써, Anthropic의 제재와 대비되는 수평적 생태계 전략을 취하고 있습니다.

---

## 🛠️ 핵심 기능 및 사용법
* **명령어 및 도구**: TUI(터미널) 및 IDE 확장, 데스크톱 앱을 제공하며 `/connect`로 API 키 및 토큰 인증을 수행합니다.
* **프로젝트 초기화 (`/init`)**: 프로젝트 전체 분석을 통해 컨텍스트를 담은 `AGENTS.md`를 생성하여 AI가 설계 문서를 참고하도록 가이드를 제공합니다.
* **에이전트 권한 분리**: 파일 생성 및 수정을 집행하는 `Build` 에이전트와 계획 수립 및 검증 전용인 `Plan` 에이전트를 `Tab` 키로 스위칭하여 에러 위험을 방지합니다.

---

## 🔗 연결된 지식
* 관련 플러그인: [[oh-my-opencode]] (에이전트 하네스)
* 대안/기반 도구: [[claude-code]]
* 관련 소스: [[opencode-official]] (공식 정보 요약), [[opencode-review-1]] (갓대희 입문 가이드 요약)

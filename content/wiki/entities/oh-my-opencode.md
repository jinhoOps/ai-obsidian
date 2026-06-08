---
title: "oh-my-opencode"
type: entity
tags: [harness, plugin, ai-team, productivity]
created: 2026-05-15
updated: 2026-06-08
draft: false
sources: [wiki/sources/oh-my-opencode-review.md]
---
# oh-my-opencode

> 단일 AI 에이전트를 전문화된 AI 팀으로 변환하여 오토파일럿 병렬 개발 파이프라인을 지원하는 OpenCode 전용 플러그인(하네스)입니다.

---

## 🚀 핵심 아키텍처 및 에이전트 팀

### 1. Sisyphus 오케스트레이터
* **역할**: 메인 지휘자 및 오케스트레이터. 사용자의 복잡한 요구사항을 분석하여 여러 하위 작업으로 분해하고 전문 에이전트에게 전달합니다.
* **기술 사양**: Claude Opus 4.5 기반, 32k Extended Thinking budget을 활용하여 복잡한 아키텍처 결정을 수행합니다.
* **Todo Continuation Enforcer**: AI 에이전트가 작업 중 임의로 멈추고 사용자 입력을 기다리는 고질적 관행을 억제하고, 전체 백로그가 완수될 때까지 반복 루프를 자율 집행합니다.

### 2. 전문 서브 에이전트 분업 (Sync/Async)
* **Oracle** (Sync, GPT-5.2): 아키텍처 설계 및 심층 디버깅 어드바이저 (`@oracle`로 명시적 호출).
* **Librarian** (Async, GLM-4.7): 공식 문서 탐색 및 오픈소스 리서치 전담 (`@librarian` 호출).
* **Explore** (Async, Grok Code): 초고속 코드베이스 탐색 및 검색 전담 (`@explore` 호출).
* **Frontend UI/UX** (Async, Gemini 3 Pro) / **Document-Writer** (Async, Gemini 3 Flash) / **Multimodal-Looker** (Async, Gemini 3 Flash) 등이 비동기적으로 병렬 처리하여 메인 스레드의 속도를 확보합니다.

---

## 💡 주요 컨텍스트 주입 메커니즘
* **Directory AGENTS.md Injector**: 파일을 로드할 때 해당 파일의 디렉토리부터 프로젝트 루트에 존재하는 모든 `AGENTS.md` 및 `README.md` 컨텍스트를 계층적으로 선제 주입합니다.
* **Conditional Rules Injector**: `.claude/rules/` 하위의 YAML 규칙을 파일 확장자 globs 패턴 매칭에 따라 동적으로 바인딩합니다.
* **Context Compaction**: 대화 컨텍스트 윈도우가 가득 차기 전에 선제 압축(Preemptive Compaction)과 동적 정리(Pruning)를 실행하여 토큰 폭탄을 차단합니다.

---

## 🔧 운영 가이드 및 주의사항
* **마법 키워드 `ultrawork` (또는 `ulw`)**: 프롬프트에 포함하는 것만으로 오케스트레이션 및 Todo 강제 집행 루프가 백그라운드에서 가동됩니다.
* **Anthropic OAuth 차단 이슈 (2026-01-09)**: Anthropic이 써드파티 도구의 공식 구독형 OAuth 연동을 차단했으므로, 계정 차단을 막기 위해 반드시 **개인 API 키 방식**이나 원가 중개용 **OpenCode Zen**을 사용해야 합니다.
* **성능 최적화 (google_auth)**: `oh-my-opencode.json`에서 `"google_auth": true`와 Google Application Default Credentials(ADC)를 결합하여 Google Cloud API 직접 호출을 연결함으로써 레이턴시를 크게 개선할 수 있습니다.

---

## 🔗 연결된 지식
* 기반 플랫폼: [[opencode]]
* 관련 소스: [[oh-my-opencode-review]]
* 핵심 설계 철학: [[aggressive-delegation]] (공격적 위임), [[harness-engineering]] (하네스 엔지니어링)

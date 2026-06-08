---
title: "OpenCode 리뷰(1) : 설치 및 기본 설정"
type: source
tags: [ai-agent, opencode, local-llm, multiprovider]
sources: [content/raw/articles/Open Code 리뷰(1)  OpenCode 설치(oh-my-opencode 사전 학습) 및 설정, 기본 명령어 살펴보기.md]
created: 2026-06-08
updated: 2026-06-08
draft: false
---

# OpenCode 리뷰(1) : 설치 및 기본 설정

> 갓대희의 블로그 포스트를 요약한 것으로, 오픈소스 AI 코딩 에이전트 OpenCode의 특징, 설치 방법, LLM 제공자 연동 방식 및 핵심 기능을 다룹니다.

---

## 📌 핵심 내용

### 1. OpenCode의 정의와 강점
* **오픈소스 AI 코딩 에이전트**: 터미널(TUI), 데스크톱 앱, IDE 확장 프로그램 형태로 동작하는 AI 에이전트입니다.
* **비용 효율성과 프라이버시**: 도구 자체는 무료이며 사용하는 모델의 API 원가 수준(Zero-Markup) 또는 로컬 LLM을 통한 무료 운영이 가능합니다. 코드 및 컨텍스트를 외부 서버에 저장하지 않아 보안성이 뛰어납니다.
* **다중 모델 전환 전략**: 기획 및 설계 단계에서는 Gemini와 같은 저렴한 모델을 사용하고, 정밀 코딩 구현 시에는 Claude를 사용하여 비용을 최적화할 수 있습니다.

### 2. 설치 및 LLM 연동 방식
* macOS/Linux는 `curl` 스크립트나 `Homebrew`를 이용해 설치하며, Windows는 `Chocolatey`, `Scoop`, `npm` 전역 설치를 지원합니다.
* `/connect` 대화형 명령어를 통해 75개 이상의 LLM 제공자(Anthropic, OpenAI, Google, Groq, Ollama 로컬 실행 등)와 연결하여 API 키를 관리합니다.

### 3. OpenCode Zen과 요금제 모델
* **OpenCode Zen**: 선별된 코딩 특화 모델 게이트웨이로, Grok Code Fast 2, GLM 4.7, MiniMax M2.1 등을 베타 기간 한정 무료로 제공하거나 원가 가격 정책으로 중개합니다.
* **OpenCode Black**: 월 $20~$200 요금제로 Claude Opus/Sonnet, GPT-5, Gemini 3 등을 월정액 형태로 자유롭게 사용하는 구독 모델입니다.

### 4. 2026년 1월 9일 자 중요 차단 이슈
* **Anthropic의 써드파티 OAuth 차단**: Anthropic은 Claude Code 전용으로 설계된 Pro/Max 구독 OAuth 토큰을 OpenCode와 같은 제3자 에이전트 하네스에서 스푸핑하여 사용하는 것을 ToS 위반으로 공식 규정하고 기술적 제한을 적용하였습니다.
* **OpenAI의 공식 지원과 대조**: OpenAI는 ChatGPT Plus/Pro 구독을 통한 Codex OAuth 연동을 공식적으로 허용(v1.1.11 이후)하여 오픈소스 에이전트 생태계를 지지하는 상반된 태도를 보입니다.
* **권장 조치**: OpenCode에서 Claude를 연동할 때는 반드시 개인 **API 키 방식**을 사용해야 계정 차단(밴) 위험을 피할 수 있습니다.

### 5. 기본 구성 요소 및 TUI 키바인딩
* `Build` 에이전트(편집/실행 권한 보유)와 `Plan` 에이전트(분석 전용, 확인 요구)를 제공하며 `Tab` 키로 전환합니다.
* `@General` 및 `@Explore` 서브 에이전트를 내장하고 있으며, `@` 문법으로 질문 범위에 파일을 간편하게 추가할 수 있습니다.

---

## 🔗 연결된 지식
* 엔티티: [[opencode]] (OpenCode), [[anthropic]] (Anthropic), [[openai]] (OpenAI)
* 개념: [[harness-engineering]] (하네스 엔지니어링), [[complexity-management]] (복잡성 관리)

---

## 📝 생각 및 메모
* **비용과 규제의 줄다리기**: 상용 LLM 제공업체(Anthropic)가 자사 에이전트 전용 구독을 보호하기 위해 써드파티 생태계를 차단하는 현상은 향후 AI 에이전트 생태계의 비즈니스 모델 규제 트렌드를 보여줍니다.
* **다중 모델 활용의 당위성**: 비용 효율을 극대화하기 위해 설계는 Gemini/로컬 LLM, 구현은 핵심 상용 LLM으로 계층화하는 멀티 에이전트 설계가 필요합니다.

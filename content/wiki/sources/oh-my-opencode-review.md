---
title: "OpenCode 리뷰(2) : oh-my-opencode와 Sisyphus"
type: source
tags: [ai-agent, opencode, oh-my-opencode, multi-agent, sisyphus]
sources: [content/raw/articles/Open Code 리뷰(2)  oh-my-opencode 설치 및 설정 방법(기본 명령어, 슬래시 명령어, 연동 방법 등) with Claude,OpenAI,Gemini.md]
created: 2026-06-08
updated: 2026-06-08
draft: false
---

# OpenCode 리뷰(2) : oh-my-opencode와 Sisyphus

> 갓대희의 블로그 포스트를 요약한 것으로, OpenCode의 플러그인 에이전트 하네스인 `oh-my-opencode`의 아키텍처, Sisyphus 오케스트레이터, 그리고 멀티 에이전트 파이프라인 설정을 설명합니다.

---

## 📌 핵심 내용

### 1. oh-my-opencode의 정체성 (에이전트 하네스)
* **AI 개발팀으로의 진화**: 단일 AI 에이전트 환경인 OpenCode를 오케스트레이터를 필두로 한 전문 AI 개발팀으로 변환해주는 "Battery Included" 플러그인 프레임워크입니다.
* **Sisyphus 오케스트레이터**: Claude Opus 4.5 기반의 메인 지휘자로, 작업이 완료되거나 한계에 다다를 때까지 절대 멈추지 않는 **Todo Continuation Enforcer** 메커니즘을 내장하고 있습니다.
* **Aggressive Delegation (공격적 위임)**: 메인 지휘자는 계획 수립과 통제만 담당하고, 복잡한 하위 컨텍스트를 서브 에이전트들에게 적극 위임하여 토큰 낭비와 컨텍스트 오염을 최소화합니다.

### 2. 전문 에이전트 구성과 모델 매핑
* **역할별 최적 모델 배정**: 
  * `Sisyphus` (오케스트레이터): Claude Opus 4.5
  * `Oracle` (아키텍처, 디버깅 어드바이저): GPT-5.2 (수동 호출: `@oracle`)
  * `Librarian` (공식 문서 리서처): GLM-4.7 Free (수동 호출: `@librarian`)
  * `Explore` (코드베이스 탐색기): Grok Code (수동 호출: `@explore`)
  * `Frontend UI/UX` (UI 전담): Gemini 3 Pro (자동 호출)
  * `Document-Writer` (문서화 전담): Gemini 3 Flash (자동 호출)
* **Sync/Async 실행 구분**: `Librarian`, `Explore`, `Frontend` 에이전트 등은 백그라운드 비동기(Async)로 실행되어 여러 서브 작업을 병렬로 처리합니다. Sisyphus는 이들의 출력을 받아 최종 통합합니다.

### 3. 컨텍스트 인텔리전스 및 주입 기능
* **컨텍스트 자동 압축**: Preemptive Compaction(선제 압축), Dynamic Pruning(동적 가지치기) 등으로 컨텍스트가 가득 차는 현상을 예방합니다.
* **Directory AGENTS.md Injector**: 특정 하위 파일을 조회할 때 상위 디렉토리 트리의 모든 `AGENTS.md` 및 `README.md`를 순차적으로 자동 주입하여 설계 맥락을 이해시킵니다.
* **Conditional Rules Injector**: globs 패턴 매칭 규칙에 따라 대상 언어 및 특정 파일 유형에 해당하는 코딩 룰 파일(`.claude/rules/...`)을 자동 바인딩합니다.

### 4. 핵심 명령어 및 작동 방식
* **`ultrawork` (또는 `ulw`)**: 프롬프트에 이 키워드를 넣으면 Sisyphus가 자동으로 작업을 분해하여 서브 에이전트를 가동하고 완료될 때까지 오토파일럿으로 질주합니다.
* **IDE 수준 도구 추가**: AST 기반의 구조적 검색/치환을 제공하는 `AstGrep`과 `LSP(Language Server Protocol)` 정보(정의로 이동, 레퍼런스 찾기 등 11개 도구)를 에이전트에게 공급합니다.

### 5. 트러블슈팅과 Google ADC
* **Antigravity 404 에러**: `opencode-antigravity-auth` 플러그인의 프로젝트 권한 만료/오류 시에는 해당 플러그인을 제거하고 표준 Google OAuth를 활용해 해결합니다.
* **google_auth**: `oh-my-opencode.json`에서 `"google_auth": true` 옵션과 gcloud ADC(`gcloud auth application-default login`)를 연결하여 OpenRouter를 거치지 않고 Google Cloud API로 직접 고속 호출해 레이턴시를 절감합니다.

---

## 🔗 연결된 지식
* 엔티티: [[oh-my-opencode]] (Oh-My-OpenCode), [[gsd2]] (GSD v2), [[gbrain]] (GBrain)
* 개념: [[aggressive-delegation]] (공격적 위임), [[complexity-management]] (복잡성 관리), [[wiki-architecture]] (위키 아키텍처)

---

## 📝 생각 및 메모
* **에이전트 조직화의 모범 사례**: Sisyphus의 '공격적 위임'과 'Todo Enforcer'는 LLM이 지닌 기억 한계와 중간 멈춤이라는 하드웨어적 제약을 극복하기 위한 대표적인 소프트웨어 엔지니어링적 접근법(하네스)입니다.
* **통치체제로서의 하네스**: 개별 모델의 성능 한계를 극복하기 위해 LSP 정보 주입, 에이전트 권한 분리, 다중 계정 로드밸런싱 등 시스템적 가드레일(Harness)을 촘촘히 엮어낸 점이 인상적입니다.

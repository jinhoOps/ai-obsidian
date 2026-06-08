---
title: "gstack: Garry Tan's AI Engineering Stack"
type: source
tags: [ai-strategy, harness-engineering, gstack, product-operations]
sources: [content/raw/articles/garrytangstack Use Garry Tan's exact Claude Code setup 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA.md]
created: 2026-06-08
updated: 2026-06-08
draft: false
---

# gstack: Garry Tan's AI Engineering Stack

> Y Combinator의 CEO Garry Tan이 공개한 AI 에이전트 기반의 고속 제품 배포 스택(gstack)과 운영 철학을 정리한 소스 요약입니다.

---

## 📌 핵심 내용

### 1. AI 기반의 초고속 배포 실적 (Karpathy의 4단계 실패 극복)
* **생산성의 혁신**: Garry Tan은 2026년 기준 2013년(Bookface 개발 당시) 대비 **약 810배의 논리적 코드 변경 속도(run rate)**를 기록하고 있다고 주장합니다.
* **1인 제조 공장(Software Factory)**: AI가 대부분의 코드를 작성하며, 개발자는 코딩을 손수 하기보다는 AI가 만들어내는 결과물을 배포하고 관리하는 관리자 역할을 수행합니다.

### 2. gstack의 23가지 전문 역할 및 워크플로우
* **Think ➡️ Plan ➡️ Build ➡️ Review ➡️ Test ➡️ Ship ➡️ Reflect**의 유기적 파이프라인 구조를 따릅니다.
* **주요 슬래시 명령어(Specialists)**:
  * `/office-hours`: 6가지 강제 질문을 통해 제품 방향성을 논의하고 디자인 문서를 생성하는 제품 기획 전문가.
  * `/plan-ceo-review` & `/plan-eng-review`: 범위 조율 및 아키텍처 설계를 검증하는 아키텍트/리더십 전문가.
  * `/design-shotgun` & `/design-html`: AI 이미지 시안으로부터 UI 테이스트를 피드백 받고, Pretext를 이용한 의존성 없는 고품질 HTML을 빌드하는 프론트엔드 파이프라인.
  * `/review` & `/investigate`: CI가 잡지 못하는 프로덕션 레벨 버그를 검출하고 자동 수정하는 스태프 엔지니어.
  * `/qa` & `/qa-only`: headless Chromium을 이용해 실제 웹 애플리케이션을 브라우저 수준에서 QA 테스트하고 회귀 테스트를 자동 작성하는 QA Lead.
  * `/cso`: OWASP Top 10 및 STRIDE 위협 모델을 바탕으로 가짜 양성을 제외한 실제 보안 취약점과 익스플로잇 시나리오를 검출하는 보안 책임자.
  * `/ship` & `/land-and-deploy`: 테스트를 돌리고 PR 생성 및 자동 머지 후 프로덕션 건강성 검증까지 담당하는 릴리즈 엔지니어.
  * `/learn`: 세션별 학습 및 피드백, 테이스트 프로필을 Compound(축적)하여 에이전트를 점진적으로 고도화하는 메모리 기능.

### 3. 지속적 체크포인트와 안전 가드레일
* **Continuous Checkpoint Mode**: 세션 중 작업 내역을 로컬 Git에 `WIP:` 커밋으로 자동 저장하여 크래시 발생 시 `/context-restore`로 세션을 복구합니다. 최종 배포 시 스쿼시(squash) 머지를 통해 히스토리를 정비합니다.
* **안전 장치**: `/careful`(파괴적 명령어 실행 전 경고), `/freeze`(작업 디렉토리 제한), `/guard`(둘 모두 적용)를 통한 예기치 못한 프로덕션 피해 방지.
* **다중 에이전트 브라우저 제어**: `/pair-agent`를 이용해 OpenClaw, Hermes 등 서로 다른 벤더의 에이전트들이 하나의 GStack Browser 탭을 공유하며 웹 서핑을 수행하도록 연결 및 조율합니다.

---

## 🔗 연결된 지식
* 엔티티: [[garry-tan]] (Garry Tan), [[gstack]] (GStack), [[claude-code]] (Claude Code), [[gbrain]] (GBrain)
* 개념: [[harness-engineering]] (하네스 엔지니어링), [[agentic-workflow]] (에이전트 워크플로우), [[knowledge-compounding]] (지식 복리 효과)

---

## 📝 생각 및 메모
* **개념 탐색 맥락**: Garry Tan의 gstack은 AI를 단순한 코드 보조 도구(Copilot)로 보지 않고, 소프트웨어 생산의 전 과정을 자동 조율하는 오케스트레이션 공장(Harness)으로 정의합니다.
* **관점의 전환**: 개발자의 역할이 코딩 생산자에서 AI 파이프라인의 **지휘자 및 의사결정권자(Editor)**로 변화하고 있음을 보여주는 실증적 사례입니다.

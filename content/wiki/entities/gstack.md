---
title: "gstack"
type: entity
tags: [tool, ai-agent, framework]
sources: [wiki/sources/garry-tan-gstack.md]
created: 2026-05-14
updated: 2026-06-08
draft: false
---
# gstack

> [[garry-tan|Garry Tan]]이 개발한 [[claude-code|Claude Code]] 기반의 에이전틱 스킬 프레임워크이자, 소프트웨어 개발 라이프사이클 전체를 조율하는 AI 소프트웨어 공장(Software Factory) 하네스입니다.

---

## 🚀 핵심 아키텍처 및 스프린트 프로세스
gstack은 단순 코딩 보조 도구를 넘어 **"Think ➡️ Plan ➡️ Build ➡️ Review ➡️ Test ➡️ Ship ➡️ Reflect"**로 이어지는 스프린트 단계를 시스템화하였습니다.

### 1. 전문가 페르소나 및 슬래시 명령어
AI 에이전트에 구조화된 역할을 부여하여 Blank Prompt의 혼란을 방지합니다.
* **CEO / Founder (`/plan-ceo-review`)**: 10-star 제품 관점에서 범위를 조율하고 확장/reduction 판단을 수행합니다.
* **Eng Manager (`/plan-eng-review`)**: 아키텍처 다이어그램 및 테스트 매트릭스를 확정합니다.
* **QA Lead (`/qa`, `/qa-only`)**: headless Chromium을 띄워 실시간 페이지 흐름을 테스트하고 회귀 테스트를 자동 생성합니다.
* **SRE (`/canary`) / Performance (`/benchmark`)**: 배포 후 모니터링 및 성능 비교 메트릭을 도출합니다.
* **CSO (`/cso`)**: OWASP Top 10 및 STRIDE 취약점 모델을 검사하며, 가짜 양성(false positive)을 예외처리하여 높은 신뢰도를 갖춘 익스플로잇 시나리오를 제공합니다.

### 2. Continuous Checkpoint Mode (연속 체크포인트)
* 작업 내역을 로컬 Git에 `WIP:` 커밋 단위로 상시 저장합니다.
* 에이전트 세션 크래시나 맥락 전환 발생 시, `/context-restore`를 호출하여 이전 상태를 완벽하게 재구성합니다.
* 최종 머지 시에는 WIP 커밋을 깔끔하게 스쿼시(squash) 처리하여 메인 브랜치의 Git 히스토리를 정돈합니다.

### 3. /pair-agent (다중 에이전트 브라우저 제어)
* GStack Browser를 매개로 하여 Claude Code, OpenClaw, Hermes, OpenAI Codex 등 다양한 상용 에이전트들이 브라우저 탭을 분할 공유하며 동일한 웹 앱을 탐색 및 조율하도록 연동합니다.
* ngrok 터널링과 보안 토큰, 샌드박싱 격리를 통해 타 기기 에이전트와의 안전한 협업을 지원합니다.

---

## 🔗 연결된 지식
* 기반 플랫폼: [[claude-code|Claude Code]]
* 관련 메모리 허브: [[gbrain|GBrain]]
* 관련 소스 요약: [[garry-tan-gstack]] (gstack 요약)
* 핵심 방법론: [[harness-engineering]] (하네스 엔지니어링), [[aggressive-delegation]] (공격적 위임)

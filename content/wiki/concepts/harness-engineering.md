---
title: "하네스 엔지니어링 (Harness Engineering)"
type: concept
tags: [ai, harness-engineering, engineering-standards, safety, loop-design]
sources: [content/raw/notes/Harness_Engineering.md, content/raw/notes/conversation-harness-insights.md]
created: 2026-05-15
updated: 2026-05-18
draft: false
---

# 하네스 엔지니어링 (Harness Engineering)

> 모델의 실수를 방지하고 목적 달성을 보장하기 위해, AI 주위에 구축하는 시스템적 루프(Loop) 및 거버넌스 설계 방식

## 🧩 비유로 이해하기 (Mental Models)
- **운영체제(OS)**: 모델이 **CPU**라면, 하네스는 그 위에서 안전하게 앱을 구동하는 **OS**입니다.
- **운동장**: 하네스는 에이전트가 실력을 발휘할 수 있는 **울타리(경계)**이자 **경기 규칙(Rule)**입니다.
- **주방**: 하네스는 **위생 규정 및 주방 운영 수칙**입니다. 요리사(모델)가 요리에만 집중해 일관된 품질을 낼 수 있게 뒷받침합니다.

## 📋 정의 및 본질
하네스(Harness)는 LLM의 원시 능력을 제어하고, 결과물을 검증하는 **추상화 환경**입니다. 

### 목적 달성을 위한 '루프(Loop)' 설계
하네스 엔지니어링의 본질은 **'문제 정의(출발지)에서 해결(도착지)까지 AI가 길을 잃지 않고 도달하게 만드는 시스템적 루프'**를 설계하는 것입니다.
- **상태 관리**: 현재 작업의 진행 상황을 추적하고 지도를 제공.
- **복원 루프**: 실패 시 오류를 감지하고 스스로 수정하게 만드는 피드백 루프(Feedback Loop).
- **검증 루프**: 생성자(Generator)와 독립된 검증자(Evaluator)를 통해 결과물 품질 보장.

## 🏛️ 하네스의 핵심 구성 (거버넌스 레이어)
단순한 기술적 인프라를 넘어, 시스템 전체의 **'통치 규범(Constitution)'** 역할을 수행합니다.
- **GEMINI.md / CLAUDE.md**: 시스템의 정체성과 협업 규칙을 정의하는 최상위 헌법.
- **AGENTS.md / SKILL.md (Rules 영역)**: 각 페르소나와 스킬이 지켜야 할 행동 강령.
- **인프라 가드레일**: 출력을 검증하는 린터, 타입 체크, 안전성 필터.

## ⚖️ 하네스 vs 워크플로우
하네스와 [[agentic-workflow|에이전트 워크플로우]]는 서로 보완적인 관계입니다.
- **하네스**: 고정적이고 규범적인 **'운동장(규칙과 울타리)'**. 거버넌스 레이어.
- **워크플로우**: 유동적이고 실행적인 **'경기 방식(전술과 순서)'**. 오퍼레이션 레이어.

## 🚀 설계 7원칙
1. **지도를 줄 것**: 백과사전 대신 목차와 탐색 가이드를 제공 (Progressive Disclosure).
2. **불변량 강제**: 아키텍처 규칙과 컨벤션을 린터와 CI로 엄격히 관리.
3. **생성과 평가의 분리**: Generator와 독립된 Evaluator 인스턴스 운용.
4. **시각적 검증**: Playwright 등을 통해 결과물을 직접 확인하게 함.
5. **모델 맞춤형 튜닝**: 모델의 성능 향상에 따라 하네스 설계를 유연하게 변경.
6. **가비지 컬렉션**: 드리프트되는 코드를 주기적으로 스캔하고 정리.
7. **Boring Tech**: 훈련 데이터가 풍부하고 검증된 기술 스택 우선 선택.

## 🔗 연결된 지식
- [[executable-ssot]] (실행 가능한 SSOT)
- [[mitchell-hashimoto]] (Mitchell Hashimoto - 하네스 개념 제안자)
- [[openai]] vs [[anthropic]] (기업별 하네스 접근법)

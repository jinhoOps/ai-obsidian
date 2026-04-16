---
type: node
created: 2026-04-13
updated: 2026-04-14
status: evergreen
tags: [ai, harness-engineering, agents, engineering-standards, openai, anthropic]
---

# 🛠️ 하네스 엔지니어링 (Harness Engineering)

하네스(Harness)는 LLM의 원시 능력(Raw Capability)을 제어하고, 특정 작업에 맞게 방향을 잡아주며, 결과물을 검증하는 **추상화 및 환경 설계의 총체**입니다. 모델이 CPU라면, 하네스는 유용한 앱을 돌리기 위한 운영체제(OS)와 같습니다.

## 🏗️ 개념적 비유
- **모델 = CPU**: 연산 엔진.
- **컨텍스트 윈도우 = RAM**: 작업 중인 휘발성 메모리.
- **에이전트 하네스 = OS**: 자원 관리, 도구 연결, 프로세스 제어.
- **에이전트 = Application**: 실제 작업을 수행하는 단위.

## 🏢 양대 빅테크의 하네스 접근법 비교

| 관점 | OpenAI (엔지니어링 중심) | Anthropic (디자인/평가 중심) |
| :--- | :--- | :--- |
| **핵심 은유** | 에이전트의 세계(Repo) 구축 | 적대적 피드백 루프 (Evaluator) |
| **에이전트 수** | Codex 단일 (+ 리뷰 에이전트) | 3-Agent (Planner/Generator/Evaluator) |
| **품질 보장** | 린터 + CI + 정기 가비지 컬렉션 | 독립 Evaluator + Playwright 시각 QA |
| **컨텍스트** | Progressive Disclosure (지도 제공) | 자동 컴팩션 (요약) 및 리셋 |
| **인간의 역할** | 환경 설계자 (코드 0줄 작성 지향) | 하네스 튜너 (기준 및 프롬프트 조정) |

### 1. OpenAI: 불변량 강제와 엔트로피 관리
- **Repository 중심**: "에이전트가 접근할 수 없는 것은 존재하지 않는 것과 같다." 모든 지식은 버전 관리되는 리포지토리에 있어야 함.
- **아키텍처 불변량(Invariant)**: 레이어(Types → Config → Repo → Service → Runtime → UI) 간 의존성 방향을 린터로 엄격히 강제.
- **가비지 컬렉션**: 백그라운드 에이전트가 정기적으로 미사용 코드나 위반 사항을 스캔하여 리팩토링 PR을 자동 생성.

### 2. Anthropic: 시각적 검증과 자기평가 편향 보정
- **컨텍스트 불안(Context Anxiety) 대응**: 모델이 작업을 조기 종료하거나 일관성을 잃는 현상을 하네스 레벨에서 관리.
- **독립 Evaluator**: 에이전트는 자신의 작업을 과대평가하므로, "문제점만 찾아라"는 회의적 프롬프트를 가진 별도 인스턴스로 검증.
- **실제 관측성**: Playwright MCP를 통해 에이전트가 실제 앱을 구동하고 스크린샷을 찍으며 인터랙션 품질을 평가.

## 📜 하네스 설계 7원칙 & 실무 액션

1.  **백과사전을 주지 말고, 지도를 줄 것**
    - `AGENTS.md`는 100줄 이내의 목차로 유지.
    - 상세 내용은 `docs/` 하위로 분리하여 에이전트가 필요할 때 탐색하게 유도(Progressive Disclosure).
2.  **불변량은 코드로 강제하라**
    - 아키텍처 경계와 네이밍 규칙은 린터와 CI로 강제.
    - **Action**: 린터 에러 메시지에 에이전트가 참고할 '수정 방법'을 포함시킬 것.
3.  **생성과 평가를 분리하라**
    - 독립된 Evaluator를 두고 "좋은 점은 생략하고 문제점만 찾아라"고 지시.
4.  **에이전트에게 앱을 보여줘라**
    - Playwright 등을 연결하여 에이전트가 시각적 결과와 사용성을 직접 확인하게 함.
5.  **모델이 바뀌면 하네스를 재검증하라**
    - 하네스는 모델의 약점에 대한 가정이므로, 모델 성능 향상 시 불필요한 가이드는 과감히 제거.
6.  **엔트로피를 가비지 컬렉션하라**
    - 에이전트 생성 코드는 시간이 지나면 드리프트함. 정기적으로 죽은 코드와 미사용 의존성을 정리하는 프로세스 가동.
7.  **지루한 기술(Boring Tech)을 선택하라**
    - 훈련 데이터가 풍부한 기술(React, PostgreSQL, FastAPI 등)이 에이전트 작업 성공률을 높임.

## 🏗️ 하네스의 3가지 계층 (The 3 Layers of Harness)

하네스는 용도에 따라 세 가지 층으로 구분하여 설계할 때 가장 효율적입니다.

1.  **제품 실행 하네스 (Product Runtime Harness)**: 실제 앱이나 기능이 안전하게 실행되도록 만드는 구조 (Validator -> Planner -> Executor -> Verifier).
2.  **개발 안전 하네스 (Dev Safety Harness)**: 개발 중 구조가 무너지지 않도록 검사하는 장치 (Tests, CI, Cleanup Scripts).
3.  **에이전트 작업 하네스 (Agent Task Harness)**: AI 에이전트가 프로젝트에서 일관되게 작업하도록 돕는 가드레일 (AGENTS.md, SKILL.md, 완료 기준).

## ✅ 하네스 구성 핵심 요소 (Harness Components)

하네스를 구성하는 최소 필수 요소와 각 역할은 다음과 같습니다.

| 컴포넌트 | 역할 | 예시 |
| :--- | :--- | :--- |
| **Validator** | 입력값의 정합성 및 위험성 검증 | 필수 값 체크, 타입 검사, 권한 확인 |
| **Planner** | 명시적인 실행 순서(Step) 계획 생성 | 생성 순서 계획, 의존성 순서 결정 |
| **Executor** | Plan에 따른 순차 실행 및 상태 기록 | Step별 성공/실패 기록, 실패 시 중단 |
| **Verifier** | 실행 결과가 목표와 일치하는지 확인 | 파일 생성 확인, API 응답 값 검증 |
| **완료 기준 (DoD)** | 작업의 성공 여부를 판단하는 정량적 지표 | "성공 시 Verifier 통과 및 리포트 생성" |

## 📜 하네스 설계 7원칙 & 실무 액션
**관련 노트:**
- [[wiki/ai/AI_Development_Timeline|AI 발전 타임라인]]
- [[wiki/ai/Obsidian_RAG_Methodology|Obsidian-RAG 방법론]]
- [[wiki/ai/_index|AI 지식 인덱스]]
- [[wiki/_agent_workflows|에이전트 워크플로우]]

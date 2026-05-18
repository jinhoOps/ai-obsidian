---
title: "에이전트 워크플로우 (Agentic Workflow)"
type: concept
tags: [ai, workflow, operations, process]
sources: [content/raw/notes/하네스-에이전트워크플로우.md]
created: 2026-05-18
updated: 2026-05-18
draft: false
---

# 에이전트 워크플로우 (Agentic Workflow)

> 하네스(Harness)라는 시스템적 제약 안에서 특정 목표를 달성하기 위해 에이전트가 수행하는 구체적이고 단계적인 행동 절차.

## 🧩 비유로 이해하기
- **축구 비유**: 하네스가 경기장 라인과 규칙이라면, 워크플로우는 **'팀의 전술과 패스 플레이'**입니다.
- **음식점 비유**: 하네스가 주방 설비와 위생 규정이라면, 워크플로우는 **'주문부터 서빙까지의 레시피'**입니다. (재료 손질 -> 조리 -> 플레이팅 -> 서빙) 순서대로 움직여 손님에게 요리를 전달하는 과정입니다.

## 📋 정의
에이전트 워크플로우는 AI 에이전트가 복잡한 태스크를 해결하기 위해 밟는 **'실행 및 운영 레이어'**의 프로세스입니다. 이는 정적인 규칙(하네스)과 달리, 작업의 성격에 따라 유동적으로 최적화될 수 있는 SOP(Standard Operating Procedure)를 의미합니다.

## 🏗️ 주요 구성 요소 (LLM Wiki 예시)
1. **Discover**: 새로운 정보나 문제를 식별.
2. **Research**: 기존 지식(Wiki)과 소스(Raw)를 탐색.
3. **Strategy**: 해결을 위한 계획 수립.
4. **Execution**: 실제 코드 수정, 문서 생성 등 작업 수행.
5. **Validation**: 결과가 규칙(Harness)에 부합하는지 검증.

## ⚖️ 하네스와의 차이점
| 구분 | [[harness-engineering|하네스]] | 에이전트 워크플로우 |
|---|---|---|
| **핵심 질문** | "우리는 어떤 규칙을 따르는가?" | "이 일을 어떻게 처리할 것인가?" |
| **수준(Level)** | 추상적, 규범적, 고정적 (Governance) | 구체적, 실행적, 유동적 (Operations) |
| **비유** | 헌법, 운동장, OS 커널, **음식점 주방/규정** | 업무 매뉴얼, 경기 전술, 앱 로직, **요리 레시피** |
| **핵심 파일** | `GEMINI.md`, `CLAUDE.md` | `/ingest`, `/query`, `SKILL.md` (Process) |

## 🔗 연결된 지식
- [[harness-engineering]] (하네스 엔지니어링)
- [[wiki-architecture]] (위키 아키텍처)
- [[skill-ingest]] (인제스트 스킬)
- [[skill-query]] (쿼리 스킬)

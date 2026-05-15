---
title: "하네스 엔지니어링 (Harness Engineering)"
type: concept
tags: [ai, harness-engineering, engineering-standards, safety]
sources: [content/raw/notes/Harness_Engineering.md, content/raw/notes/AI_Development_Timeline.md]
created: 2026-05-15
updated: 2026-05-15
draft: false
---

# 하네스 엔지니어링 (Harness Engineering)

> 모델의 실수를 방지하고 품질을 보장하기 위해, AI 모델 주위에 구축하는 검증 하네스 및 인프라 중심의 운용 방식

## 🧩 비유로 이해하기
모델이 **CPU**라면, 하네스는 그 CPU 위에서 유용한 애플리케이션을 구동하기 위한 **운영체제(OS)**와 같습니다. CPU가 아무리 강력해도 메모리 관리, 입출력 제어, 에러 핸들링을 담당하는 OS가 없다면 아무것도 할 수 없듯이, AI 모델 역시 하네스 없이는 안정적인 작업을 수행하기 어렵습니다.

## 📋 정의
하네스(Harness)는 LLM의 원시 능력(Raw Capability)을 제어하고, 특정 작업에 맞게 방향을 잡아주며, 결과물을 검증하는 **추상화 및 환경 설계의 총체**입니다. 이는 단순한 프롬프트 엔지니어링을 넘어, 시스템적인 가드레일과 평가 루프를 구축하는 것을 의미합니다.

## 🏗️ 하네스의 3계층
1. **제품 실행 하네스 (Product Runtime Harness)**: 실제 앱이나 기능이 안전하게 실행되도록 만드는 구조 (Validator -> Planner -> Executor -> Verifier).
2. **개발 안전 하네스 (Dev Safety Harness)**: 개발 중 구조가 무너지지 않도록 검사하는 장치 (Tests, CI, Cleanup Scripts).
3. **에이전트 작업 하네스 (Agent Task Harness)**: AI 에이전트가 프로젝트에서 일관되게 작업하도록 돕는 가드레일 (GEMINI.md, SKILL.md, 완료 기준).

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

---
title: "데브옵스 (DevOps)"
type: concept
tags: [devops, cloud-engineering, infrastructure, sre, cicd]
sources: [content/raw/notes/데브옵스 로드맵.md]
created: 2026-05-18
updated: 2026-05-20
draft: false
---

# 데브옵스 (DevOps)

소프트웨어 개발(Development)과 IT 운영(Operations)을 통합하여, 시스템 개발 수명 주기(SDLC)를 단축하고 고품질의 서비스를 안정적으로 지속 배포(Continuous Delivery)하기 위한 문화, 프로세스, 기술적 실천법의 결합입니다.

## 🛠️ 핵심 도메인 (Core Domains)

1. **클라우드 엔지니어링 (Cloud Engineering)**: AWS, GCP, Azure 등 가상화된 클라우드 자원을 코드로 정의하고 설계하는 인프라 관리 방식 (IaC - Infrastructure as Code).
2. **인프라 및 서버 관리 (Infra & Server)**: 고가용성(High Availability) 및 장애 대응력을 갖춘 베어메탈, 가상 서버, 컨테이너(Docker, Kubernetes) 기반 환경 구축.
3. **사이트 신뢰성 공학 (SRE - Site Reliability Engineering)**: 시스템 다운타임을 최소화하고 복구력(Resiliency)을 확보하며, SLA/SLO 준수를 극대화하기 위한 소프트웨어적 측정 및 모니터링 활동.
4. **지속적 통합/배포 (CI/CD)**: 빌드, 테스트, 릴리스, 배포 프로세스를 파이프라인으로 자동화하여 배포 리스크와 주기를 최소화하는 엔지니어링 체계.

## 📌 핵심 원칙 (CAMS)

1. **Culture (문화)**: 개발과 운영 간의 고립(Silo)을 허물고 공동의 책임을 지는 조직 구조와 신뢰 문화 구축.
2. **Automation (자동화)**: 휴먼 에러를 제거하고 속도를 극대화하기 위해 코드를 통한 인프라 프로비저닝 및 릴리스 자동화.
3. **Measurement (측정)**: 메트릭, 로그, 분산 추적(Observability)을 기반으로 시스템 건강성과 처리량을 정량적으로 수집·모니터링.
4. **Sharing (공유)**: 장애 발생 시 비난 없는 회고(Blameless Post-mortem)와 모범 사례를 전사적으로 나누며 동반 성장.

## ⚖️ 데브옵스(DevOps) vs 하네스 엔지니어링(Harness Engineering)

전통적인 시스템 신뢰성과 배포 인프라를 지탱하는 **데브옵스**와 AI 에이전트의 제어 루프를 보장하는 **하네스 엔지니어링**은 서로 명확히 구분되는 독립적인 전문 도메인입니다.

| 구분 | 데브옵스 (DevOps) | 하네스 엔지니어링 (Harness Engineering) |
|---|---|---|
| **대상 (Target)** | 인간이 작성한 애플리케이션 및 하드웨어/가상화 시스템 | 자율적으로 작동하는 AI 에이전트 및 LLM 추론 루프 |
| **핵심 영역** | Cloud Engineering, Infrastructure, SRE, CI/CD | State Management, Feedback Loop, Verification (Generator/Evaluator) |
| **통제 방식** | 규칙 기반 결정적 자동화 (Linter, Unit Test, CD Script) | 거버넌스 가이드 및 동적 맥락 규범 (GEMINI.md, AGENTS.md) |
| **주된 목적** | 시스템 고가용성, 가동 시간 극대화 및 빠른 릴리스 주기 | AI의 할루시네이션(환각) 방지 및 안전한 자율적 목적 달성 |

## 🔗 연결된 지식
- [[devops-roadmap]] (데브옵스 엔지니어 학습 경로)
- [[harness-engineering]] (AI 중심의 거버넌스 및 제어 루프 설계)


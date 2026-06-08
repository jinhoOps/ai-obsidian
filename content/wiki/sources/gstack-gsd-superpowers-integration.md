---
title: "gstack, gsd, superpowers 통합 가이드"
type: source
tags: [gstack, gsd, superpowers, integration, methodology, planning]
sources: ["content/raw/notes/gstack + gsd + superpowers 함께 사용하기.md"]
created: 2026-06-08
updated: 2026-06-08
draft: false
---

# 🔗 gstack, gsd, superpowers 통합 가이드

세 가지 에이전트 도구를 역할별로 연계하여 강력한 자율형 프로젝트 관리 파이프라인을 구축하는 설계 가이드입니다.

## 핵심 내용

1. **역할 정의 및 매핑**:
   - **`gstack`** ➔ **"무엇을 왜 만드나" (전략·검증)**: `/cso`, `/qa`, `/ship`, `/review` 등의 상위 의사결정 및 검증을 담당.
   - **`gsd`** ➔ **"어떤 순서로 만드나" (구조·실행)**: `/gsd-plan-phase`, `/gsd-execute-phase`, `/gsd-validate-phase` 등 순차적인 진행 상태 및 마일스톤 관리를 수행.
   - **`superpowers`** ➔ **"어떻게 잘 만드나" (방법론·품질)**: TDD(Test-Driven Development), 체계적 디버깅, 코드 리뷰 프로토콜 등 개발의 실행 품질을 담보.
2. **실전 협업 파이프라인**:
   - **비전 수립**: `/cso` (gstack)
   - **계획 수립**: `/gsd-plan-phase` (gsd)
   - **구현**: `/gsd-execute-phase` + `superpowers:test-driven-development`
   - **검증**: `/gsd-verify-work` + `/qa` (gstack)
   - **완료**: `/gsd-complete-milestone` + `/ship` (gstack)
3. **상태 보존 및 버전 관리**:
   - `gsd`는 프로젝트 루트의 `.planning/` 디렉토리에 마일스톤, 로드맵, 계획서(`PLAN.md`), 검증 결과(`VERIFICATION.md`)를 모두 저장하며, 이를 통해 계획 자체도 Git으로 관리 가능하게 합니다.

## 연결된 지식
- [[gstack]] : 전략/검증 스택
- [[gsd]] : 실행/구조 관리 스택
- [[superpowers]] : 개발 방법론 프레임워크
- [[agentic-workflow]] : 에이전트 워크플로우 전반

## 생각 및 메모
- 단순한 AI 대화 수준을 넘어, 실제 소프트웨어 개발팀이 사용하는 형태의 체계적인 마일스톤 관리와 품질 관리를 에이전트 파이프라인에 주입하는 실전적 사례입니다.
- 이 세 가지의 융합을 통해 "바이브 코딩"의 한계를 극복하고, 지속적이고 예측 가능한 에이전트 개발이 가능해집니다.

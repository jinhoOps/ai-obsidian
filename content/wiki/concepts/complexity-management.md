---
title: "복잡성 관리 (Complexity Management)"
type: concept
tags: [engineering-principles, senior-dev, stability]
sources: [wiki/sources/senior-dev-complexity.md]
created: 2026-05-14
updated: 2026-05-14
draft: false
---
# 복잡성 관리 (Complexity Management)

## 개념 정의
시스템이 성장함에 따라 필연적으로 증가하는 엔트로피를 억제하고, 코드가 계속해서 이해 가능하고(Understandable), 수정 가능하며(Modifiable), 디버깅 가능하도록(Debuggable) 유지하는 시니어 개발자의 핵심 역량입니다.

## 핵심 원칙
1.  **최소한의 구현**: "안 하면 어떻게 되는가?"를 먼저 묻고, 가능하면 코드를 쓰지 않거나 기존 것을 재사용합니다.
2.  **의존성 경계**: 새로운 기술이나 도구를 도입할 때 그것이 시스템 전체의 복잡성에 미치는 영향을 평가합니다.
3.  **이해 가능성 우선**: AI가 코드를 빠르게 생성할 수 있는 시대에는, 생성된 코드가 미래의 인간(또는 AI)이 이해할 수 있는 구조인지 관리하는 것이 더 중요해집니다.

## 비즈니스와의 충돌 및 조율
- 비즈니스는 빠른 실험(Uncertainty Reduction)을 원하고, 개발은 안정성을 원합니다.
- 시니어 개발자는 "복잡해서 안 된다"는 말 대신, "더 빠른 실험을 위해 이런 구조를 먼저 잡아야 한다"는 식으로 설득해야 합니다.

## 관련 개념
- Uncertainty Reduction (불확실성 감소)
- [[senior-as-editor|Senior as Editor]]
- [[speed-vs-scale|Speed vs Scale]]

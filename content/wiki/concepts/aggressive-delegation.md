---
title: "공격적 위임 (Aggressive Delegation)"
type: concept
tags: [agent-strategy, delegation, architecture]
created: 2026-05-15
updated: 2026-05-15
draft: false
sources: [wiki/sources/oh-my-opencode-review.md]
---
# 공격적 위임 (Aggressive Delegation)

메인 오케스트레이터가 모든 일을 직접 처리하지 않고, 가능한 모든 세부 작업을 전문 서브 에이전트에게 즉시 넘기는 에이전트 운영 전략입니다.

## 💡 비유
지휘자가 직접 악기를 연주하지 않고 각 파트장에게 연주를 맡긴 뒤 조율에만 집중하는 오케스트라와 같습니다.

## 💎 장점
1. **컨텍스트 오염 방지**: 메인 에이전트의 대화 창에 불필요한 코드 조각이나 검색 결과가 쌓이지 않음.
2. **병렬성**: 여러 작업을 동시에 백그라운드에서 진행 가능.
3. **최적 모델 활용**: 검색은 빠른 모델로, 복잡한 설계는 고성능 모델로 분리하여 실행.

## 🔗 연결된 지식
- 관련 도구: [[oh-my-opencode]], [[oh-my-opencode|Sisyphus]]
- 관련 개념: [[harness-engineering]]

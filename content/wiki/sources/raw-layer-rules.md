---
title: "Raw Layer — AI 운영 규칙"
type: source
tags: [meta, governance, raw-layer, immutability]
sources: [content/raw/ai-rules.md]
created: 2026-05-18
updated: 2026-05-18
draft: false
---

# Raw Layer — AI 운영 규칙

AI 에이전트가 `content/raw/` 레이어의 파일을 다룰 때 준수해야 할 핵심 원칙과 워크플로우를 정의한 소스입니다.

## 📌 핵심 내용
1. **불변성 (Immutability)**: `content/raw/` 레이어의 파일은 절대 수정되지 않는 "Source of Truth"임.
2. **읽기 전용**: AI는 이 레이어의 파일을 분석 목적으로만 읽을 수 있으며, 수정이나 삭제가 금지됨.
3. **인제스트 체크리스트**: 소스 읽기 → 분석 및 요약 → 위키 소스 페이지 생성 → 인덱스 업데이트의 표준 절차 준수.
4. **Quartz 빌드 제외**: 원본 소스는 내부 참조용이며 외부에 노출되지 않도록 설정됨.

## 🔗 연결된 지식
- 개념: [[wiki-architecture]]
- 규칙: [[ai-rules]] (meta/ai-rules.md 와의 연결성)

## 📝 메모
- 시스템의 무결성을 유지하기 위한 가장 기본적인 "거버넌스" 규칙임.
- 하네스 엔지니어링의 관점에서 볼 때, 이 규칙 자체가 에이전트의 행동 반경을 제약하는 하네스의 일부임.

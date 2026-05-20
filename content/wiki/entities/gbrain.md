---
title: "GBrain (지식 뇌)"
type: entity
tags: [tool, knowledge-base, open-source]
sources: [wiki/sources/gbrain.md]
created: 2026-05-20
updated: 2026-05-20
draft: false
---

# GBrain

> **"마크다운 메모를 AI 에이전트의 실시간 지식 뇌로 전환하는 Postgres 기반 개인 지식 베이스"**

---

## 1. 개념 설명 (비유)
기존의 메모 앱(Obsidian, Notion 등)이 개인이 필요한 정보를 기록해두는 **"디지털 책장"**이라면, **GBrain**은 AI 에이전트가 언제든 손을 뻗어 실시간으로 필요한 지식을 꺼내 쓸 수 있도록 돕는 **"지식의 시냅스(Synapse)"** 혹은 **"인공 뇌"**입니다. 
책장에 꽂힌 책을 사람이 직접 눈으로 찾아서 읽는 대신, AI 에이전트가 뇌 신경망에 직접 전류를 흘려보내듯 질문(Query)을 던지면 GBrain이 즉각적으로 가장 맥락이 닿아 있는 '정제된 기억'을 추출하여 넘겨줍니다.

---

## 2. 주요 기능 및 특징
GBrain은 다음과 같은 핵심 컴포넌트로 구성되어 동작합니다:

| 컴포넌트 / 특징 | 상세 내용 |
|---|---|
| **저장 아키텍처** | 분산 마크다운 파일 $\rightarrow$ Postgres + pgvector + tsvector 데이터베이스로 영구 통합 |
| **하이브리드 검색** | 벡터 유사도(HNSW) + 키워드 검색(tsvector)을 **RRF(Reciprocal Rank Fusion)**로 결합 및 중복 제거 파이프라인 작동 |
| **지식 2중 레이어** | 실시간 갱신되는 실행 가능 단일 진실인 `[[compiled-truth]]`와 증거 수집 순서인 `Timeline`으로 나누어 지식 관리 |
| **MCP 연동** | 20개의 MCP(Model Context Protocol) 도구 제공. Claude Code 및 Cursor 등 현대 에이전트와 완벽히 상호작용 |
| **에이전트 스킬** | `ingest`, `query`, `maintain`, `enrich`, `briefing`, `migrate`, `install` 총 7가지 에이전트 자동화 스킬 내장 |

---

## 3. 핵심 철학
1. **에이전트 네이티브 (Agent-Native)**: 인간의 가독성만을 위한 마크다운이 아니라, LLM이 이해하기 가장 좋은 형태로 데이터를 쪼개고(3단계 청킹), 쿼리 대안 확장(Query Expansion) 및 할루시네이션 방지("없음" 명시) 설계를 내장하여 **AI와의 협업 효율성**을 극대화합니다.
2. **지식의 무결성 (Integrity)**: 에이전트가 실행하는 `maintain` 스킬을 통해 모순이나 깨진 링크, 태그 불일치를 상시 자가 검진하여 지식의 질적 수준을 유지합니다. 이는 **'기억의 부채'**가 누적되지 않도록 막는 예방 주사와 같습니다.

---

## 4. 관련 지식 (Related Links)
- **개발자**: [[garry-tan]] (Garry Tan)
- **비교 개념**: [[gstack]] (Garry Tan의 또 다른 프롬프트/도구 지향 스택)
- **핵심 아키텍처**: [[compiled-truth]], [[hybrid-search]]
- **에이전트 환경**: [[claude-code]], [[antigravity-cli]], [[agentic-workflow]]

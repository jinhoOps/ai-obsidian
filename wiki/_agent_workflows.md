---
type: node
created: 2026-04-13
status: seedling
tags: [workflow, meta]
---

# 🔄 에이전트 워크플로우 (Agent Workflows)

에이전트가 지식을 수집, 정제, 연결, 보관하는 표준 절차입니다.

## 1. Gather (수집)
- 웹 클리퍼나 직접 작성을 통해 `raw/` 폴더에 자료 적치

## 2. Refine (정제)
- `compile` 명령을 통해 `raw/` 자료를 분석하고 `wiki/` 문서를 생성

## 3. Link (연결)
- 관련 문서 간의 상호 위키 링크(`[[...]]`) 삽입 및 인덱스 업데이트

## 4. Archive (보관)
- 처리가 완료된 `raw/` 파일을 `raw/archive/`로 이동

---
[[wiki/_master-index|🏠 마스터 인덱스로 돌아가기]]

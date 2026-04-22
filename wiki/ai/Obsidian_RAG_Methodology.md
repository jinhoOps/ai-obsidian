---
type: node
created: 2026-04-13
status: evergreen
tags: [obsidian, rag, ai, knowledge-management, claude-code]
---

# 🧠 Obsidian-RAG: 벡터DB 없는 개인 지식 베이스 구축

Andrej Karpathy의 지식 관리 방식에서 영감을 받은, 벡터 데이터베이스와 임베딩 없이 마크다운 파일과 LLM(Claude Code)만으로 구축하는 개인 RAG 시스템입니다.

## 🏛️ 핵심 아키텍처 (The Librarian Workflow)

이 시스템은 LLM을 **도서관 사서**로 활용합니다. 사서가 모든 책을 외우지 않고 분류 체계(인덱스)를 통해 지식을 탐색하는 원리입니다.

### 📂 폴더 구조
- **raw/**: 가공되지 않은 외부 정보(스크랩, 뉴스레터 등) 수집
- **wiki/**: LLM이 관리하고 정제한 지식 허브 (`_master-index.md` 포함)
- **output/**: 분석 결과 및 리포트

## 🔄 운영 프로세스 (4개의 동사)

1. **Gather (수집)**: 새로운 정보를 `raw/` 폴더에 적치합니다.
2. **Refine (정제)**: `raw/`의 정보를 분석하여 `wiki/`에 새로운 노트를 생성하거나 업데이트합니다. (`compile` 명령)
3. **Link (연결)**: 위키 노트 간의 상호 링크(`[[링크]]`)를 통해 지식의 망을 구축합니다.
4. **Archive (보관)**: 정제가 끝난 원본 데이터는 `raw/archive/`로 이동시킵니다.

## ⚖️ 장단점 비교

| 특징 | Obsidian RAG | 기존 벡터 RAG |
| :--- | :--- | :--- |
| **인프라** | 없음 (Markdown 중심) | 벡터DB + 임베딩 API |
| **가독성** | 사람이 읽을 수 있는 텍스트 | 머신용 벡터 (블랙박스) |
| **자기 개선** | Audit을 통한 품질 관리 | 재인덱싱 전까지 정적 |
| **한계** | 대량 문서 처리 지연 | 대규모 데이터에 최적화 |

---
**참고 링크:**
- [[wiki/ai/_index|AI 지식 인덱스]]
- [[index|마스터 인덱스]]
- [원본 출처](https://wikidocs.net/289873)

---
type: "raw"
category: "article"
source: "https://news.hada.io/topic?id=28323"
author:
  - "xguru"
clipped_date: 2026-05-20
tags:
  - "article"
  - "ingest-ready"
---
# GBrain — 오픈소스 개인 지식 베이스

> [!ABSTRACT] AI Ingest Instruction
> 이 파일은 `raw/articles`에 저장된 원본 소스입니다. 
> 인제스트 시 핵심 내용을 요약하고, `wiki/sources/`에 페이지를 생성하며 관련 엔티티를 연결하세요.

## 메타데이터
- 원본 URL: https://news.hada.io/topic?id=28323
- 저자: xguru
- 수집일: 2026-05-20T14:44:42+09:00

---

▲

(github.com/garrytan)

53P by [xguru](https://news.hada.io/@xguru) 1달전 | ★ favorite |

- YC CEO Garry Tan이 **Karpathy의 LLMWiki 스타일** 로 만든 **개인 지식 관리(Knowledge Brain)** 도구
- CLI/라이브러리로도 사용 가능하지만, OpenClaw와 연동해 사용하는 것을 추천
- 분산된 마크다운 파일들을 **Postgres 기반 지식 베이스** 로 통합하고, 의미 기반 **하이브리드 검색** 을 제공
- **벡터(pgvector HNSW) + 키워드(tsvector)를 RRF(Reciprocal Rank Fusion)** 으로 결합
- **Claude Haiku** 로 쿼리 2개 대안 표현 자동 생성(multi-query expansion), 벡터/키워드 검색 등 4단계 중복 제거 파이프라인 포함
- 페이지마다 **compiled truth** (현재 최선의 이해, 새 증거 시 전면 재작성)와 **timeline** (추가 전용 증거 추적) 분리하는 독자적 지식 모델
- **MCP 서버 20개 툴** 제공 — Claude Code·Cursor 등 AI 에이전트와 직접 연동
- **7개 AI 에이전트 스킬** 내장:
	- **ingest(문서 인입)**: 회의·문서·기사 인제스트, compiled truth 재작성 + timeline 추가 + 교차 참조 링크 생성
		- **query(하이브리드 검색+인용)**: 하이브리드 검색(키워드+벡터+RRF+expansion) + 합성 + 인용, 정보 없으면 "없음" 명시 (할루시네이션 방지)
		- **maintain(헬스 체크)**: 모순, 오래된 compiled truth, 고아 페이지, 죽은 링크, 태그 불일치, 누락 임베딩 탐지
		- **enrich(외부 API 보강)**: 외부 API에서 페이지 보강, 원시 데이터는 별도 저장
		- **briefing(일일 브리핑)**: 오늘의 미팅 참석자 컨텍스트, 활성 딜 데드라인, 시간 민감 스레드 정리
		- **migrate(데이터 이전)**: Obsidian(wikilink), Notion(UUID 제거), Logseq(block ref), 일반 마크다운, CSV, JSON, Roam 마이그레이션
		- **install(설치)**: GBrain 최초 설치 전 과정 자동화
- **3단계 청킹 전략**: Recursive(빠름·무손실) / Semantic(Savitzky-Golay 경계 감지) / LLM-guided(Claude Haiku, 품질 최고)
- v0.2.0에서 **git 기반 증분 sync**, **Supabase Storage 파일 관리**, **설치 스킬** 추가, sync 테스트 20개 추가(총 39개)
- **ClawHub** 사용 시 `clawhub install gbrain` 한 줄로 패키지 설치~스킬 복사~초기화 완료
- MIT 라이선스 / TypeScript
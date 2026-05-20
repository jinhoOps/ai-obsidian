---
title: "위키 아키텍처 (Wiki Architecture)"
type: concept
tags: [wiki-system, architecture, llm-wiki]
sources: [GEMINI.md]
created: 2026-05-14
updated: 2026-05-14
draft: false
---

# 위키 아키텍처 (Wiki Architecture)

> Karpathy의 "LLM Wiki" 패턴을 기반으로 한 개인 지식 베이스.
> 핵심 원리: RAG처럼 매번 재탐색하지 않고, AI가 **영구적으로 컴파일된 위키**를 점진적으로 구축·유지한다.
> 퍼블리싱: **Quartz 4** 정적 사이트로 빌드하여 GitHub Pages에 배포.

## 3-Layer + Meta 구조

```
AI_Obsidian/                       ← Quartz 프로젝트 루트
├── GEMINI.md                      ← 스키마 — AI의 운영 규칙 (핵심만)
├── .agents/skills/                ← AI 에이전트 스킬 (ingest, query, lint)
├── quartz.config.ts               ← Quartz 빌드 설정
├── quartz/                        ← Quartz 엔진 (수정 금지)
│
└── content/                       ← Quartz 콘텐츠 루트
    ├── index.md                   ← 사이트 랜딩 페이지 (Quartz 홈)
    │
    ├── raw/                       ← Layer 1: 불변 원본 소스
    │   ├── articles/              ← 웹 아티클, 블로그, 뉴스레터
    │   ├── notes/                 ← 메모, 저널, 아이디어
    │   ├── podcasts/              ← 팟캐스트, 영상 트랜스크립트
    │   ├── research/              ← 학술지, 보고서
    │   └── assets/                ← 이미지, PDF, 데이터 파일
    │
    ├── wiki/                      ← Layer 2: AI가 컴파일하는 위키
    │   ├── index.md               ← 전체 카탈로그 (AI 탐색 시작점)
    │   ├── log.md                 ← 시간순 활동 기록
    │   ├── entities/              ← 인물, 서비스, 도구, 조직
    │   ├── concepts/              ← 추상 개념, 이론, 프레임워크
    │   ├── comparisons/           ← 대상 간 비교·분석
    │   ├── sources/               ← 각 raw 소스의 요약 페이지
    │   └── synthesis/             ← 여러 소스를 종합한 통찰
    │
    ├── output/                    ← Layer 3: 최종 결과물
    │   ├── posts/                 ← 블로그 포스트
    │   ├── slides/                ← Marp 발표 자료
    │   └── reports/               ← 분석 보고서
    │
    └── meta/                      ← 메타 레이어: 운영 도구
        └── templates/clipper/     ← Web Clipper JSON 템플릿
```

## Quartz 빌드 규칙

| 레이어 | 빌드 | 이유 |
|---|---|---|
| `wiki/` | ✅ **포함** | 지식 그래프·검색의 핵심 |
| `raw/` | ❌ **제외** | 내부용 원본 |
| `output/` | ❌ **제외** | 별도 채널 배포 |
| `meta/` | ❌ **제외** | 운영 도구 |

> `quartz.config.ts`의 `ignorePatterns`에 `["raw", "output", "meta", "templates", "private"]` 설정.

## 역할 분담

| 역할 | 사람 | AI |
|---|---|---|
| 소스 수집 | ✅ 선별·저장 | — |
| 방향 결정 | ✅ 질문·탐색 | — |
| 요약·정리 | — | ✅ 요약 페이지 작성 |
| 교차 참조 | — | ✅ 링크·태그 유지 |
| 위키 유지보수 | — | ✅ lint·업데이트 |
| 결과물 생성 | 리뷰·승인 | ✅ 초안 생성 |

## 제약 사항

- `content/raw/`는 **불변** — AI는 읽기만
- `content/wiki/`는 **AI 소유** — AI가 생성·수정·삭제
- `content/output/`은 **협업** — AI가 초안, 사람이 리뷰
- `content/meta/`는 **사람 소유** — AI는 제안만
- `quartz/`는 **수정 금지** — Quartz 엔진

## 위키 페이지 작성 규칙

```yaml
---
title: "페이지 제목"
type: entity | concept | comparison | source | synthesis
tags: [태그1, 태그2]
sources: [원본 파일 경로]
created: YYYY-MM-DD
updated: YYYY-MM-DD
draft: false
---
```

- **링크**: Obsidian 위키링크 `페이지명` (Quartz가 자동 변환)
- **언어**: 한국어, 비유 활용
- **시각화**: Mermaid 다이어그램 적극 활용
- **길이**: 한 페이지 = 한 개념/엔티티. 길어지면 분리
- **draft**: `true` 시 Quartz 빌드에서 제외

## 핵심 파일

| 파일 | 역할 | 갱신 시점 |
|---|---|---|
| `content/wiki/index.md` | AI 탐색 시작점 | 매 ingest |
| `content/wiki/log.md` | 활동 기록 | 매 작업 |
| `GEMINI.md` | 운영 스키마 | 필요 시 |

## 워크플로우

| 스킬 | 트리거 | 하는 일 |
|---|---|---|
| `/ingest` | "인제스트해줘" | raw/ → 읽기 → 대화 → wiki/ 반영 |
| `/query` | 위키에 대한 질문 | wiki/ 탐색 → 답변 합성 → 지식 환류 |
| `/lint` | "위키 점검해줘" | wiki/ 전수 검사 → 수정 → 검증 |

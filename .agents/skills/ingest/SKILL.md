---
name: ingest
description: "raw/ 폴더의 새로운 소스를 발견하고, 읽고, 요약하고, 사용자와 대화한 후 wiki/에 체계적으로 반영하는 LLM Wiki 인제스트 워크플로우입니다."
---

# /ingest — LLM Wiki 소스 인제스트 스킬

> `content/raw/`에 새로 저장된 소스를 발견하고, 읽고, 요약하고, 사용자와 대화한 뒤 `content/wiki/`에 체계적으로 반영하는 워크플로우입니다.

---

## 🛡️ 불변 규칙 (Invariants)

1. **`content/raw/`는 절대 수정하지 않는다.** 읽기 전용(Read-Only)이다.
2. **`content/wiki/`는 AI가 소유한다.** 이 스킬이 생성·수정·삭제할 수 있다.
3. **모든 위키 페이지는 GEMINI.md의 frontmatter 규칙을 따른다.**
4. **언어는 한국어(존댓말), 인코딩은 UTF-8이다.**
5. **위키링크는 Obsidian 형식 `[[페이지명]]`을 사용한다.**
6. **운영 규칙은 GEMINI.md와 [[wiki-architecture]] 페이지를 참조한다.**

---

## 📋 워크플로우: DISCOVER → READ → DISCUSS → COMPILE → REPORT

### Phase 1: DISCOVER (발견)

`content/raw/`의 하위 폴더(articles/, notes/, podcasts/, research/)를 스캔하여, `content/wiki/sources/`에 대응하는 요약 페이지가 아직 없는 **새 소스 파일**을 식별합니다.

1. `content/wiki/index.md`를 읽어 이미 인제스트된 소스 목록을 파악합니다.
2. `content/raw/*/` 에서 `.md` 파일을 수집합니다. (`index.md`, `agents.md`는 제외)
3. 새 소스 목록을 카테고리별로 사용자에게 보고합니다.
4. 파일이 없으면 "새로운 소스가 없습니다"라고 알리고 종료합니다.

### Phase 2: READ & SUMMARIZE (읽기 & 요약)

각 새 소스를 읽고 **3가지 축**으로 요약합니다:

| 축 | 내용 |
|---|---|
| **핵심 주장 (Key Claims)** | 글의 중심 논지 3-5개 |
| **언급된 엔티티 (Entities)** | 인물, 도구/서비스, 조직 |
| **다루는 개념 (Concepts)** | 추상 개념, 이론, 프레임워크 |

- frontmatter에서 `type`, `category`, `source`, `clipped_date`를 파싱합니다.
- `wiki/index.md`를 확인하여 기존 페이지와 겹치는 엔티티/개념이 있으면 "업데이트 대상"으로 표시합니다.

### Phase 3: DISCUSS (대화)

사용자에게 **3가지 질문**을 던져 맥락을 수집합니다. **답변을 받기 전에는 Phase 4로 진행하지 않습니다.**

```
1. 이 글을 왜 캡처했나요?
2. 지금 하고 있는 일과 어떻게 연결되나요?
3. 이걸로 뭘 해보고 싶나요?
```

- 소스가 여러 개일 때는 질문을 한 번에 묻고, 통합 답변을 받습니다.

### Phase 4: COMPILE (위키 반영)

Phase 2의 요약 + Phase 3의 맥락을 결합하여 위키에 반영합니다.

#### 4.1 소스 요약 페이지: `content/wiki/sources/{slug}.md`

```yaml
---
title: "{소스 제목}"
type: source
tags: [{태그}]
sources: [content/raw/{category}/{원본파일명}]
created: YYYY-MM-DD
updated: YYYY-MM-DD
draft: false
---
```
→ 개요, 핵심 내용 (번호 매긴 섹션), 연결된 지식, 생각 및 메모

#### 4.2 엔티티 페이지: `content/wiki/entities/{slug}.md`
- 위키에 자체 페이지가 **없는** 핵심 엔티티만 새로 생성합니다.
- 이미 **있는** 엔티티는 새 정보를 추가합니다.

#### 4.3 개념 페이지: `content/wiki/concepts/{slug}.md`
- 사용자의 학습 목표/프로젝트와 직접 관련 있는 것을 우선 생성합니다.
- 비유 먼저, 그 다음 정확한 정의를 제공합니다.

#### 4.4 시스템 파일 업데이트
- **`content/wiki/index.md`**: 새 페이지를 해당 카테고리 섹션에 추가 + 통계 업데이트
- **`content/wiki/log.md`**: 최상단에 `## [{날짜}] ingest | {제목}` 엔트리 추가
- **`content/raw/*/index.md`**: 해당 카테고리 목록에 항목 추가 (목록 업데이트만 허용)

### Phase 5: REPORT (완료 보고)

생성/업데이트된 페이지 목록을 보고하고 후속 제안(비교/종합/프로젝트 적용)을 제시합니다.

---

## 🔧 엣지 케이스

| 상황 | 처리 |
|---|---|
| frontmatter 없음 | 파일명과 내용에서 추론 → 사용자 확인 |
| 800줄 초과 파일 | 분할 읽기 (800줄씩) |
| 이미 인제스트된 소스 재요청 | 기존 페이지 보여주고 업데이트 여부 확인 |

## 📌 완료 전 체크리스트

- [ ] frontmatter가 GEMINI.md 규칙을 따르는가?
- [ ] `[[위키링크]]`가 실제 존재하는 페이지를 가리키는가?
- [ ] `wiki/index.md` 통계가 정확한가?
- [ ] `raw/`의 어떤 파일도 수정되지 않았는가?
- [ ] 모든 페이지에 `draft: false`가 설정되었는가?

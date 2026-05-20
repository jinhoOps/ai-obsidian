---
title: "Wiki Layer — AI 운영 규칙"
type: meta
created: 2026-05-14
updated: 2026-05-14
draft: true
---

# 🧠 Wiki Layer — AI 운영 규칙

> `content/wiki/` 레이어에서 AI가 준수할 규칙입니다.
> `draft: true`로 Quartz 사이트에서 이 페이지는 렌더링되지 않습니다.

## 레이어 정의
**Layer 2: AI 컴파일 위키** — AI가 소유·관리하는 지식의 핵심 허브.

## 핵심 원칙

### ✍️ AI 소유
- AI가 페이지를 **생성·수정·삭제** 가능
- 모든 변경은 `wiki/log.md`에 기록
- `wiki/index.md`를 항상 최신 상태로 유지

### 🔗 연결성
- 모든 페이지는 최소 1개 이상 `[[위키링크]]`로 연결
- 고아 페이지는 Lint 시 발견하여 연결

## 하위 폴더

| 폴더 | 용도 | 파일명 |
|---|---|---|
| `entities/` | 인물, 서비스, 도구, 조직 | kebab-case |
| `concepts/` | 추상 개념, 이론, 프레임워크 | kebab-case |
| `comparisons/` | 비교·분석 | `a-vs-b.md` |
| `sources/` | raw 소스 요약 | kebab-case |
| `synthesis/` | 종합 통찰 | `주제-synthesis.md` |

## Quartz 빌드
- ✅ **빌드 포함** — wiki가 사이트의 핵심 콘텐츠
- `[[위키링크]]`는 Quartz가 자동 변환
- `draft: true` 페이지는 빌드 제외

## 페이지 Frontmatter

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

## 본문 규칙
- **첫 문단**: 한 줄 요약
- **비유 우선**: 어려운 개념 → 비유 먼저, 정확한 정의
- **위키링크**: 관련 개념을 `페이지명`으로 연결
- **시각화**: 관계가 복잡하면 Mermaid 다이어그램
- **길이**: 한 페이지 = 한 개념. 길어지면 분리

## AI 체크리스트

### Ingest 시
1. ✅ `sources/`에 요약 페이지 생성
2. ✅ `entities/`, `concepts/`에 관련 페이지 생성
3. ✅ 기존 페이지와 위키링크 연결
4. ✅ `index.md` 업데이트
5. ✅ `log.md`에 기록

### 업데이트 시
1. ✅ frontmatter `updated` 갱신
2. ✅ `log.md` 기록
3. ✅ `index.md` 확인

### Lint 시
1. ✅ 고아 페이지, 깨진 링크, frontmatter 누락, 낡은 정보 확인
2. ✅ 결과를 사용자에게 보고

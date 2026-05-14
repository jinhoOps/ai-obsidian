---
title: "Meta Layer — AI 운영 규칙"
type: meta
created: 2026-05-14
updated: 2026-05-14
---

# ⚙️ Meta Layer — AI 운영 규칙

> `content/meta/` 레이어에서 AI가 준수할 규칙입니다.

## 레이어 정의
**메타 레이어: 운영 도구** — 위키 시스템 자체를 운영하기 위한 도구와 템플릿.

## 핵심 원칙

### 👤 사람 소유 (Human-Owned)
- 이 레이어는 **사용자가 소유**합니다
- AI는 **제안만** 가능하며, 사용자 승인 후에만 수정합니다
- 템플릿 구조 변경은 반드시 사용자와 논의 후 진행합니다

## 하위 폴더

| 폴더 | 용도 |
|---|---|
| `templates/clipper/` | Obsidian Web Clipper JSON 템플릿 |

## Quartz 빌드
- ❌ **빌드 제외** — 운영 도구는 공개 불필요
- `quartz.config.ts`의 `ignorePatterns`에 `"meta"` 포함

## AI 체크리스트
1. ✅ 템플릿 개선 사항 발견 시 사용자에게 **제안**
2. ✅ 새 템플릿 유형이 필요할 때 초안 제시
3. ❌ 사용자 승인 없이 수정 금지
4. ❌ 파일 삭제 금지

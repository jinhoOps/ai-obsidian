---
title: "GSD 워크플로우 명령어 흐름"
type: source
tags: [gsd, workflow, commands, cheatsheet]
sources: [content/raw/notes/gsd-명령어-흐름.md]
created: 2026-05-19
updated: 2026-05-19
draft: false
---

# 🚀 GSD 워크플로우 치트시트 (Quick Guide)

> **"무엇을 해야 할지 모를 때는 `/gsd-progress --next`만 기억하세요."**
> 이 페이지는 작업 중 터미널 옆에 띄워두고 즉시 참조하기 위한 '명령어 액기스'입니다.

---

## ⚡ 무지성 작업 루프 (Easy Mode)

가장 빠르게 다음 할 일을 진행하고 싶을 때 사용합니다.
- `/gsd-progress --next`: 현재 상태를 분석하고 **자동으로 다음 단계**를 안내/수행합니다.

---

## 🔄 일상 작업 루프 (Daily Cycle)

매일 아침 작업을 재개하고 페이즈를 완료할 때의 표준 절차입니다.

1. **상태 확인**: `/gsd-progress` (현재 위치 파악)
2. **맥락 복원**: `/gsd-resume-work` (어제 작업 내용 불러오기)
3. **계획 수립**: `/gsd-plan-phase` (`PLAN.md` 생성)
4. **구현 실행**: `/gsd-execute-phase` (태스크 순차 실행)
5. **검증**: `/gsd-validate-phase` 또는 `/gsd-verify-work` (목표 달성 확인)

> 💡 **Tip**: 설계 고민이 필요할 땐 `/gsd-discuss-phase`로 AI와 대화하세요.

---

## 🏁 마일스톤 종료 정석 (The 5-Step Exit)

마일스톤을 깔끔하게 마무리하고 다음 단계로 넘어가기 위한 필수 체크리스트입니다.

| 순서 | 명령어 | 역할 |
|---|---|---|
| **1. Audit** | `/gsd-audit-milestone` | 구현 누락 및 버그 최종 점검 (Gap 발견 시 해결 후 재실행) |
| **2. Complete** | `/gsd-complete-milestone` | 공식 종료 처리, 아카이빙, Git 태그 생성 |
| **3. Cleanup** | `/gsd-cleanup` | `.planning/phases/` 폴더 정리 및 최적화 |
| **4. Extract** | `/gsd-extract-learnings` | 패턴 및 지식 추출 (`LEARNINGS.md` 작성) |
| **5. Next** | `/gsd-new-milestone` | 다음 마일스톤 설계 및 시작 |

---

## 🔗 연결된 지식
- **엔티티**: [[gsd]], [[claude-code]]
- **개념**: milestone-phase-task, context-persistence, [[harness-engineering]]

## 📝 메모
- `/gsd-progress --next` 플래그는 사용자의 인지 부하를 줄여주는 '이지 모드' 진입점입니다.
- 마일스톤 종료의 5단계는 '부채 없는 개발'을 위한 하네스 엔지니어링의 핵심 규범입니다.

---
title: "gstack 설치 가이드 (Antigravity CLI 용)"
type: source
tags: [gstack, installation, setup, antigravity-cli, agy, openclaw]
sources: ["content/raw/GSTACK 설치 - agy (Antigravity CLI).md"]
created: 2026-06-08
updated: 2026-06-08
draft: false
---

# 🛠️ gstack 설치 가이드 (Antigravity CLI 용)

gstack을 Antigravity CLI(`agy`) 및 OpenClaw 환경에서 설치하고 동작 방식을 테스트하기 위한 실전 가이드입니다.

## 핵심 내용

1. **설치 프로세스**:
   - `git clone`을 통해 로컬 사용자 설정 폴더(`~/.gemini/antigravity/skills/gstack`)에 gstack을 내려받고 setup 스크립트를 수행합니다.
   - `AGENTS.md` (또는 `GEMINI.md`)에 `gstack` 섹션을 추가하고 사용 가능한 브라우징 도구(`/browse`) 및 스킬을 정의합니다.
2. **팀 모드 설정**:
   - 공유 저장소에서 `./setup --team`을 실행하여 팀원 전체가 프로젝트 세션 시작 시 gstack 자동 업데이트 혜택을 받도록 구성할 수 있습니다.
   - `optional` 또는 `required` 옵션으로 동료들의 gstack 필수 실행 정책을 조율합니다.
3. **OpenClaw (agy 변종) 연동**:
   - ACP를 통해 agy 세션을 생성하는 OpenClaw 환경에서 gstack을 설치하고 `AGENTS.md`를 통해 코딩 태스크 시 gstack 스킬을 로드하도록 위임 지시를 추가합니다.
4. **동작 및 스프린트 워크플로우**:
   - gstack은 단순 도구 모음이 아니라, **생각하기 ➔ 계획 ➔ 구축 ➔ 검토 ➔ 테스트 ➔ 배포 ➔ 반영**의 유기적 흐름입니다.
   - `/office-hours`의 디자인 문서가 `/plan-ceo-review`와 `/plan-eng-review`로 이어지고, `/review`와 `/qa`를 거쳐 `/ship`으로 안전하게 귀결되는 구조입니다.

## 연결된 지식
- [[antigravity-cli]] : Antigravity CLI에 대한 설명
- [[gstack]] : Garry Tan의 AI 엔지니어링 스택
- [[harness-engineering]] : 에이전트 오동작 방지 인프라

## 생각 및 메모
- `gstack`은 AI 협업 도구의 모음이 아닌 하나의 완벽한 소프트웨어 개발 생태계 프로세스에 가깝습니다.
- 개별 도구(예: `/qa` 브라우저 테스팅)를 독립적으로 사용하기보다 전체 스프린트 흐름 속에서 활용할 때 그 효과가 극대화됩니다.

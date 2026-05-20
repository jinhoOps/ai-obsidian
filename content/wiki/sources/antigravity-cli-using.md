---
title: "Antigravity CLI 상세 사용법"
type: source
tags: [antigravity-cli, agy, commands, slash-commands, workflow]
sources: [https://antigravity.google/docs/cli-using]
created: 2026-05-20
updated: 2026-05-20
draft: false
---

# 🛠️ Antigravity CLI 상세 사용법

Antigravity CLI는 프롬프트 박스에 직접 입력하는 **슬래시 명령어(/)**를 통해 에이전트의 행동과 세션을 관리합니다.

## 1. 네이티브 슬래시 명령어
- **/usage**: 터미널 내에서 대화형 인터랙티브 도움말 매뉴얼을 표시합니다.
- **/agents**: 실행 중인 서브에이전트를 모니터링하고, 로그 확인 및 작업을 중단할 수 있는 TUI 패널을 엽니다.
- **/logout**: Google 세션에서 로그아웃하고 캐시된 인증 정보를 삭제합니다.
- **/conversations**: 활성 세션을 전환하거나 이전에 나눈 대화를 불러옵니다.
- **/rollback**: 대화 히스토리를 이전 체크포인트로 되돌립니다.
- **/rename**: 현재 대화 스레드의 이름을 변경합니다.

## 2. 서브에이전트 및 권한 승인
- **Asynchronous Subagents**: 리서치, 빌드 검증 등 무거운 작업은 백그라운드에서 실행됩니다. `/agents` 명령으로 이들을 제어할 수 있습니다.
- **Fast Path Approval (`ctrl+k`)**: 서브에이전트가 권한 승인을 요청할 때 프롬프트 위에 알림이 뜹니다. 현재 대화 흐름을 방해받지 않고 `ctrl+k` 단축키로 즉시 승인할 수 있습니다.

## 3. 에이전트 자율성 설정 (Autonomy)
에이전트가 도구를 사용하거나 코드를 수정할 때의 개입 수준을 설정할 수 있습니다.
- `strict`: 모든 도구 사용에 대해 사용자 승인이 필요합니다.
- `request-review`: 중요한 변경 사항에 대해서만 승인을 요청합니다.
- `always-proceed`: 사용자 승인 없이 자율적으로 작업을 수행합니다. (주의 필요)

## 4. 커스텀 설정 및 파이프라인
`~/.gemini/antigravity-cli/settings.json`을 수정하여 세밀한 명령 권한(예: `git` 허용, `rm -rf` 차단)을 설정하거나, 에이전트의 메타데이터를 로컬 쉘 스크립트로 파이프하여 커스텀 워크플로우를 구축할 수 있습니다.

## 🔗 연결된 지식
- [[antigravity-cli]] : 엔티티 상세 정보
- [[gsd-workflow-commands]] : (심화) GSD 방법론 기반의 워크플로우 명령어

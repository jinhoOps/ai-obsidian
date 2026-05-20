---
title: "Antigravity CLI 시작 가이드"
type: source
tags: [antigravity-cli, agy, getting-started, setup]
sources: [https://antigravity.google/docs/cli-getting-started]
created: 2026-05-20
updated: 2026-05-20
draft: false
---

# 🛸 Antigravity CLI 시작 가이드

Antigravity CLI(`agy`)는 키보드 중심 개발자를 위한 경량 터미널 인터페이스입니다. Antigravity 2.0 데스크톱 앱과 동일한 에이전트 하네스, 설정 및 권한을 공유합니다.

## 1. 설치 및 인증
- **설치**: [antigravity.google](https://antigravity.google)에서 플랫폼을 다운로드하여 설치하면 `agy` 명령어를 사용할 수 있습니다.
- **인증**: Silent Keyring 로그인을 지원하여 원격 SSH 세션 등에서도 별도의 입력 없이 매끄러운 인증이 가능합니다.

## 2. 초기 마이그레이션
- 기존 Gemini CLI 사용자는 첫 실행 시 제공되는 온보딩 프로세스를 통해 기존 확장 프로그램(Extensions), 스킬, 설정을 자동으로 가져올 수 있습니다.
- 수동으로 마이그레이션하려면 다음 명령어를 사용합니다:
  ```bash
  agy plugin import gemini
  ```

## 3. 기본 구성
- **설정 파일**: `~/.gemini/antigravity-cli/settings.json`
- **프로젝트 설정**: 각 프로젝트 루트의 `.agents/` 디렉토리에 상태 및 로컬 설정이 저장됩니다.
- **권한 관리**: 에이전트의 자율성 수준(request-review, always-proceed, strict)을 설정하여 안전한 자동화를 구현할 수 있습니다.

## 🔗 연결된 지식
- [[antigravity-cli]] : 엔티티 상세 정보
- [[antigravity-cli-migration]] : 상세 마이그레이션 절차
- [[antigravity-cli-using]] : 상세 사용법 및 슬래시 명령어

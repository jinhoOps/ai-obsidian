---
title: "OpenCode 리뷰(2) : oh-my-opencode와 Sisyphus"
type: source
tags: [oh-my-opencode, sisyphus, orchestration, harness]
sources: [content/raw/articles/Open Code 리뷰(2)  oh-my-opencode 설치 및 설정 방법(기본 명령어, 슬래시 명령어, 연동 방법 등) with Claude,OpenAI,Gemini.md]
created: 2026-05-15
updated: 2026-05-15
draft: false
---

# OpenCode 리뷰(2) : oh-my-opencode와 Sisyphus

단일 에이전트를 전문 AI 팀으로 진화시키는 `oh-my-opencode` 플러그인과 Sisyphus 오케스트레이터를 다룹니다.

## 📌 핵심 내용
1. **Sisyphus 오케스트레이터**: 작업 완료 시까지 멈추지 않는(Todo Enforcer) 지휘자 에이전트.
2. **공격적 위임 (Aggressive Delegation)**: 전문 에이전트(Oracle, Librarian, Explore 등)에게 작업을 병렬로 분산하여 컨텍스트 오염을 방지하고 속도를 극대화.
3. **IDE급 도구 확장**: LSP 연동, AST-Grep(구조적 치환) 등 강력한 코드 수정 도구 제공.
4. **Ultrawork (ulw)**: 하위 태스크 분해, 실행, 검증을 자동화하는 마법의 키워드.

## 🔗 연결된 지식
- 엔티티: [[oh-my-opencode]], [[oh-my-opencode|Sisyphus]], Oracle, Librarian
- 개념: [[aggressive-delegation]], todo-continuation-enforcer, [[harness-engineering]]

## 📝 메모
- 사용자의 "gsd, gstack 등 방법론 공부" 목표와 직결되는 실전형 하네스 구현체임.

---
title: "2026년 6월 첫째 주 AI 업계 동향 및 플랫폼 전쟁"
type: source
tags: [choi-openai, industry-trend, news, platform-war, agents, local-ai, custom-apps]
sources: ["content/raw/articles/Post by @choi.openai on Threads.md"]
created: 2026-06-08
updated: 2026-06-08
draft: false
---

# 🌐 2026년 6월 첫째 주 AI 업계 동향 및 플랫폼 전쟁

이 문서는 2026년 6월 첫째 주(6월 1일~7일)에 걸쳐 발생한 글로벌 빅테크 및 AI 스타트업의 주요 발표를 모아놓은 스레드 글 요약입니다. AI 시장이 챗봇 성능 경쟁에서 에이전트 컴퓨팅 플랫폼 및 보안/비용 최적화를 다루는 하네스(Harness) 전쟁으로 본격 전환되고 있음을 보여줍니다.

## 핵심 내용 및 발표 요약 (6월 첫째 주)

1. **오픈AI (Codex 플랫폼화 및 메모리 구조 혁신)**:
   - **Codex Sites & Plugins**: 자연어로 설명만 하면 즉석에서 호스팅되는 웹앱/대시보드 제작 도구인 'Sites'와 직무 특화 플러그인(데이터 분석, 영업, 제품 디자인 등)을 발표. 비개발자 사용자의 성장을 주도.
   - **Build iOS Apps 플러그인**: 인앱 가상 아이폰 시뮬레이터 및 SwiftUI 프리뷰와 핫 리로드를 내장하여 컴파일/검증 시간을 55% 단축.
   - **Python SDK**: 파이썬 환경에 에이전트 런타임을 네이티브하게 이식하고 세션 복구 및 권한 제어를 지원하는 SDK 공개.
   - **Dreaming Memory**: 인간이 잠을 자며 기억을 정리하듯, 대화 종료 후 백그라운드에서 기억을 유기적으로 통합하고 맥락을 장기 갱신하는 메모리 아키텍처 출시.
2. **마이크로소프트 (인하우스 추론 모델 & 에이전트 OS)**:
   - **MAI-Thinking-1**: Azure 인프라 파트너십을 넘어 바닥부터 자체 훈련한 MoE 아키텍처 기반 추론 모델 MAI 7종 발표.
   - **Project Solara & Microsoft Scout**: OS 레이어보다 에이전트 계층을 중심에 둔 비전(Solara)과 Teams, Outlook, OneDrive 등 Workspace 전반을 자동화하여 회의 준비/자료 정리를 알아서 대행하는 Scout 에이전트 공개.
3. **구글 (Workspace 데이터 결합 및 멀티모달)**:
   - **AI Studio Workspace 연동**: 별도 미들웨어/OAuth 구축 없이 Gmail, Drive, Sheets 데이터를 AI Studio 런타임에 직접 연결하여 CRUD 앱의 개발 속도를 극한으로 끌어올림.
   - **Gemma 4 12B**: 텍스트, 이미지, 오디오를 별도 인코더 없이 단일 구조로 처리하는 통합 멀티모달 모델(Apache 2.0) 공개. 16GB 노트북에서 구동 가능.
   - **Dreambeans**: 사용자의 구글 서비스 사용 이력을 바탕으로 매일 개인 맞춤형 스토리를 추천/제공하는 앱 실험 중.
4. **로컬 AI 및 하네스/라우팅 트렌드**:
   - **LM Studio 모바일**: 'LM Link' 엔드투엔드 암호화 기술을 통해 스마트폰에서 로컬 데스크톱의 거대 AI 모델을 오프그리드로 호출 가능.
   - **Perplexity Hybrid Agentic Inference**: 프라이버시가 민감한 개인 정보는 온디바이스(로컬)에서, 복잡한 지능은 클라우드에서 처리하도록 자동 라우팅.
   - **Factory Router**: 코딩 에이전트 스타트업 Factory가 작업 유형에 따라 최적의 모델로 작업을 자동 분배하여 비용을 20~25% 감축하는 라우터 출시.
5. **엔비디아 (하드웨어 표준 플랫폼 선점)**:
   - **Isaac GR00T Humanoid Robot**: Unitree H2 Plus 본체, Sharpa 손, Jetson Thor를 묶은 공통 하드웨어 개발 플랫폼을 구축해 로봇 데이터 표준 선점.
   - **Alpamayo 2 Super**: 320억 파라미터 자율주행 VLA(Vision-Language-Action) 추론 모델 오픈소스 공개.

## 연결된 지식
- [[harness-engineering]] : 에이전트 오동작과 라우팅을 통제하는 하네스 개념
- [[agentic-workflow]] : 에이전트 기반의 워크플로우 설계
- [[opencode]] : 오픈소스 AI 코딩 에이전트 생태계

## 생각 및 메모
- 빅테크 간의 주도권 싸움이 "모델 자체의 매개변수나 IQ 대결"에서 **"누가 유저의 사내/개인 데이터를 매끄럽게 가져와서(퍼스트 파티 데이터 결합), 에이전트 런타임에 이식하고(SDK/OS 통합), 안전하고 저렴하게 실행할 것인가(하네스 & 라우터)"**로 고도화되고 있습니다.
- 6월 첫째 주 소식들은 에이전트 컴퓨팅 패러다임이 더 이상 이론이 아닌, OS와 앱 개발 환경 전반의 인프라 전쟁으로 확장되었음을 단적으로 보여줍니다.

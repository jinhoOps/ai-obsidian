---
title: "Zero-Native: Zig 기반 데스크톱 앱 프레임워크"
type: source
tags: [zig, web-ui, native-app, zero-native, vercel]
sources: [raw/articles/zero-native - Zig와 웹 UI로 데스크톱 + 모바일 앱 빌드.md]
created: 2026-05-14
updated: 2026-05-14
---

# Zero-Native: Zig 기반 데스크톱 앱 프레임워크

## 개요
Vercel Labs에서 공개한 [[Zig]] 기반의 경량 데스크톱/모바일 앱 프레임워크인 [[Zero-Native]]에 대한 요약입니다. 기존의 Electron이나 Tauri와 유사하지만, Zig 언어의 특성을 살려 더 가볍고 빠른 성능을 지향합니다.

## 핵심 내용

### 1. 기술적 특징
- **System WebView**: 브라우저를 내장하지 않고 OS의 시스템 웹뷰를 사용하여 바이너리 크기를 줄임.
- **Zig 언어 활용**: 별도의 글루 레이어 없이 플랫폼 SDK나 네이티브 라이브러리에 직접 접근 가능.
- **다양한 프레임워크 지원**: Next.js, React, Svelte, Vue 등을 스타터 템플릿으로 제공.

### 2. 보안 및 성능
- **Zero Trust Security**: 웹뷰의 네이티브 API 접근을 기본적으로 차단하고 명시적인 옵트인 방식으로만 허용.
- **JS-Zig Bridge**: `window.zero.invoke()`를 통해 안전한 통신 계층 제공.

## 연결된 지식
- **경쟁 도구**: [[Tauri]] (Rust), [[Wails]] (Go), [[Electron]]
- **기반 기술**: [[Zig]], [[WebView]]

## 생각 및 메모
- 사용자는 경제 관련 프로젝트(`Stock Snowball`)의 데스크톱 앱 버전 제작을 위해 이 프레임워크의 도입 가능성을 열어두고 있습니다.
- Vercel이 최근 출시하는 AI 기반 도구들(agent-browser, portless 등)과의 연계 가능성도 주목할 만합니다.

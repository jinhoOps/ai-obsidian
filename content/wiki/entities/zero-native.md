---
title: "Zero-Native"
type: entity
tags: [tool, framework, zig, vercel]
sources: [wiki/sources/zero-native-framework.md]
created: 2026-05-14
updated: 2026-05-14
---

# Zero-Native

## 정의
Vercel Labs에서 개발한 [[Zig]] 기반의 데스크톱 앱 프레임워크입니다. 웹 기술(HTML/JS/CSS)을 사용하여 맥, 윈도우, 리눅스용 네이티브 앱을 만들 수 있게 해줍니다.

## 핵심 특징
- **극강의 가벼움**: Electron처럼 브라우저 엔진을 통째로 내장하지 않고 시스템의 [[WebView]]를 사용하여 실행 파일 크기와 메모리 사용량을 획기적으로 줄였습니다.
- **Zig 언어의 직접성**: C와 호환성이 좋은 Zig를 사용하여 네이티브 SDK나 라이브러리에 별도의 중간 계층 없이 접근할 수 있습니다.
- **보안 모델**: 자바스크립트에서 네이티브 기능을 호출할 때 엄격한 권한 체크와 오리진 체크를 적용하는 Zero Trust 모델을 지향합니다.

## 비교
- [[Tauri]]: Rust 기반으로 유사한 목적을 가지나, Zero-Native는 Zig를 사용하여 더 낮은 수준의 제어를 제공합니다.
- [[Electron]]: 사용성은 높으나 리소스 소모가 큽니다.

## 사용자 인사이트
- 경제 프로젝트(`Stock Snowball`)의 서비스 안정성과 성능을 모두 잡기 위한 데스크톱 배포 옵션 중 하나로 검토되고 있습니다.

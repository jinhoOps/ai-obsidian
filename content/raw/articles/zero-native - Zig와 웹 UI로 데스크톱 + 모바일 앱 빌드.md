---
type: "raw"
category: "article"
source: "https://news.hada.io/topic?id=29409"
clipped_date: 2026-05-14
---
# 원본

▲

(github.com/vercel-labs)

23P by [xguru](https://news.hada.io/@xguru) 2일전 | ★ favorite |

- Vercel Labs가 공개한 **Zig 기반 데스크톱 앱 셸** 로, 웹 프론트엔드를 맥/윈/리눅스용 네이티브 앱으로 만드는 프레임워크
- 시스템 **WebView** 사용 시 브라우저 런타임을 번들하지 않아 바이너리가 작고 실행이 빠름
- 렌더링 일관성이 필요하면 **Chromium(CEF)** 번들로 전환 가능, `app.zon` (매니페스트 파일) 에서 웹 엔진 선택
- Zig가 C를 직접 호출하므로 플랫폼 SDK, 네이티브 라이브러리, 코덱 접근에 **별도 글루 레이어 필요 없음**
- WebView를 기본적으로 **신뢰하지 않는 보안 모델** 채택: 네이티브 명령, 권한, 내비게이션, 윈도우 API 모두 옵트인 방식
- `window.zero.invoke()` 로 **JavaScript → Zig 브릿지** 호출 시 사이즈 제한·오리진 체크·권한 체크 적용
- **Next, React, Svelte, Vue** 프론트엔드 스타터 템플릿 제공, `zig build run` 으로 바로 실행
- 현재는 프리릴리즈로 맥/리눅스/윈도우 빌드 경로 지원
- 모바일은 **iOS/Android** 호스트 앱이 `libzero-native.a` 의 C ABI를 링크하는 임베딩 방식(샘플 포함)
- Apache-2.0 라이선스

▲

결국에 웹앱을 네이티브앱으로 만든다는거 아닌가요? 잘 몰라서요. pwa 빌더보다 나은 대안이 되는가..

답변달기

▲

추상화의 편리함에 매몰되어 실행 성능을 포기하던 시대가 저물고 있음을 이 프로젝트가 증명하고 있네요. 가벼운 바이너리와 빠른 응답 속도는 사용자 경험의 본질이자 가장 강력한 기능입니다.

답변달기

▲

동의합니다. 특히나 요즘처럼 메모리가 비싼 시대에는 더더욱 그런 거 같아요

답변달기

▲

너무 좋다 ㅜㅜㅜ 행복행

답변달기

▲

요즘 Vercel 도 AI 기반 개발이 자리를 잡았는지 새로운 것들을 엄청 쏟아내네요.  
기존 것들에 기능 추가도 빠르고요. agent-browser, portless, json-render 등

Zero-native 는 왠지 Tauri의 Zig 버전 같은 느낌

Tauri (Rust) vs Zero-Native (zig) vs Wails (go)

[Tauri 2.0 정식 릴리즈](https://news.hada.io/topic?id=17083)  
[Wails - Go 사용 데스크톱 응용 프로그램 개발 프레임 워크](https://news.hada.io/topic?id=4774)

답변달기

▲

그래도 안정성은 electron 아닌가요

답변달기

▲

electron 은 일단 메모리 부터 너무 부담이어서요. 시스템 웹뷰만으로도 충분한 앱들은 이런 대체제들이 나은거 같습니다.

답변달기
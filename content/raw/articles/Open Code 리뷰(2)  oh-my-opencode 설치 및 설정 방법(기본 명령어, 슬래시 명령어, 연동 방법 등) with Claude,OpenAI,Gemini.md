---
type: "raw"
category: "article"
source: "https://goddaehee.tistory.com/485"
author:
  - "갓대희"
clipped_date: 2026-05-15
tags:
  - "article"
  - "ingest-ready"
---
# Open Code 리뷰(2) : oh-my-opencode 설치 및 설정 방법(기본 명령어, 슬래시 명령어, 연동 방법 등) with Claude,OpenAI,Gemini

> [!ABSTRACT] AI Ingest Instruction
> 이 파일은 `raw/articles`에 저장된 원본 소스입니다. 
> 인제스트 시 핵심 내용을 요약하고, `wiki/sources/`에 페이지를 생성하며 관련 엔티티를 연결하세요.

## 메타데이터
- 원본 URL: https://goddaehee.tistory.com/485
- 저자: 갓대희
- 수집일: 2026-05-15T14:26:50+09:00

---

728x90

안녕하세요! 갓대희 입니다.  
오늘은 OpenCode를 위한 플러그인으로 화제가 된 **"oh-my-opencode"** 에 대해 알아보려고 한다.

![](https://blog.kakaocdn.net/dna/dgNCFo/dJMcagjS6J2/AAAAAAAAAAAAAAAAAAAAAKXf3co1KbOaoQ3hNdenchy2CuApFRoMbTZNK8L2ez0x/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=HqIB2q2RlXo58UBXArvREEcMhTw%3D)

oh my opencode는 1만 2천개 이상의 GitHub 스타를 기록하며 개발자 커뮤니티에서 뜨거운 반응을 얻고 있는 프로젝트이다. (2026년 1월 초 기준)

단일 AI 에이전트를 전문화된 AI 팀으로 변환하는 혁신적인 접근 방식이 특징이다.

이번 세션에서는 이전 OpenCode기초의 내용을 어느정도 보고 왔다는전제하에, 이론적인 내용을 먼저 살펴 보고 실습을 해보는 방향으로 구성해보았다.

이번글에서는 기본 설정 및 설치 방법까지만 다루고, 이를 활용해 간단한 프로젝트를 실제 구현하는 섹션을 이어서 작성하면 좋겠다는 생각이 들었다. 일단 기본적인 설정 방법을 알아보자.

**OpenCode 시리즈**

[← Part 1: OpenCode 기초](https://goddaehee.tistory.com/484) Part 2: oh-my-opencode(현재 글) [Part 3: 오픈소스, 무료 및 저가 LLM 모델 활용](https://goddaehee.tistory.com/488) [Part 4: Z.ai GLM 구독 및 oh-my-opencode 연동해보기](https://goddaehee.tistory.com/492)

**이 글을 읽기 전에**  
이 글은 OpenCode의 기본 사용법을 알고 있다는 전제하에 작성되었다. OpenCode가 처음이라면 먼저 [OpenCode 기초](https://goddaehee.tistory.com/484) 를 읽어보길 권한다.

### 목차

1. 핵심 비교: 순정 OpenCode vs oh-my-opencode
2. 에이전트의 시대: 패러다임 전환
3. Sisyphus: 절대 포기하지 않는 오케스트레이터
	- 이름의 의미
		- 기술 사양
4. 전문화된 에이전트 팀
5. 도구 비교: 순정 OpenCode vs oh-my-opencode
6. 핵심 기능
7. 설치 및 설정 가이드
8. 설정 파일 구조 이해하기
9. 사용법: ultrawork 마법의 키워드
10. 실제 성과 사례
11. 언제 무엇을 선택할까?
12. 주의사항 및 한계점
13. 트러블슈팅 가이드
14. 자주 묻는 질문
15. 참고 자료

**oh-my-opencode: OpenCode를 AI 개발팀으로 진화시키다**  
oh-my-opencode는 OpenCode를 위한 플러그인으로, 단일 AI 에이전트를 전문화된 AI 팀으로 변환한다는 목표를 갖고 있다. Sisyphus 오케스트레이터가 이끄는 7개의 전문 에이전트가 병렬로 작업하며, 12k+ GitHub 스타를 기록한 화제의 프로젝트이다. (2026년 1월 초 기준)

AI 코딩 도구의 패러다임이 변화하고 있다. 단일 LLM이 모든 작업을 처리하던 시대에서, 전문화된 AI 팀이 협업하는 시대로 전환되고 있다. oh-my-opencode는 이 변화를 가장 명확하게 보여주는 프로젝트이다.

[공식 GitHub](https://github.com/code-yeongyu/oh-my-opencode) 에 따르면, oh-my-opencode는 "Battery Included" 에이전트 하네스로, OpenCode 위에서 동작하는 플러그인이다. 개발자 YeonGyu Kim(Q)이 개인적으로 사용하던 설정을 플러그인으로 패키징하여 공개했으며, 출시 2주 만에 3,400개 스타를 달성한 후 현재 9,500개 이상으로 성장했다.

**용어 설명**
- **에이전트 하네스(Agent Harness)**: 여러 AI 에이전트를 감싸서 제어하고 조율하는 "관제탑" 역할의 프레임워크. 마치 말을 제어하는 마구(고삐)처럼 AI들을 통제한다.
- **Battery Included**: "건전지 포함"이라는 뜻으로, 별도 설정 없이 설치만 하면 바로 사용할 수 있다는 의미. 복잡한 설정 과정 없이 즉시 동작한다.

**공식 문서 출처**  
"Certified, Verified, Tested, Actually Useful Harness in Production, after $24,000 worth of tokens spent." - 실제 프로덕션 환경에서 $24,000 상당의 토큰을 소비하며 검증된 에이전트 하네스이다.  
[oh-my-opencode GitHub README](https://github.com/code-yeongyu/oh-my-opencode)

**프로젝트 현황 (2026년 1월 초 기준)**
- **Stars**: 9,500+
- **Forks**: 635+
- **License**: SUL-1.0 (Sustainable Use License)
- **npm**: `oh-my-opencode`

※ SUL-1.0은 개인/비영리 사용은 자유롭고, 상업적 사용 시 라이선스 확인이 필요하다.

## OpenCode vs oh-my-opencode

oh-my-opencode가 순정 OpenCode와 어떻게 다른지 비교해보자.

| 구분 | 순정 OpenCode | oh-my-opencode |
| --- | --- | --- |
| **에이전트 구성** | build/plan + @general (3개) | Sisyphus + 6개 전문 에이전트 (총 7개) |
| **모델 선택** | 단일 모델 사용 | 역할별 최적 모델 자동 배정 |
| **작업 방식** | 순차 실행 | 병렬 백그라운드 실행 |
| **작업 완료 보장** | 수동 확인 필요 | Todo Enforcer 자동 지속 |
| **개발 도구** | 기본 내장 (8개) | LSP/AstGrep 추가 |
| **MCP 서버** | 수동 설정 필요 | 큐레이팅된 MCP 포함 |
| **컨텍스트 관리** | 기본 관리 | 인텔리전스 자동 관리 |
| **Claude Code 호환** | 부분 호환 | 완전 호환 레이어 |

핵심적인 차이는 "혼자 일하는 AI"에서 "팀으로 협업하는 AI"로의 전환이다. 순정 OpenCode는 Build와 Plan 에이전트 2개로 순차적으로 작업하지만, oh-my-opencode는 Sisyphus가 이끄는 에이전트 팀이 병렬로 작업한다.

## 에이전트의 시대: 패러다임 전환

AI 코딩 도구의 발전 단계를 살펴보면, 우리가 어디에 있고 어디로 향하는지 이해할 수 있다.

### AI 코딩 도구의 진화 단계

| **1세대: 코드 완성** | GitHub Copilot 등. 개발자가 타이핑하면 다음 코드를 제안한다. |
| --- | --- |
| **2세대: 대화형 AI** | ChatGPT, Claude 등. 질문하면 코드를 생성해준다. |
| **3세대: 단일 에이전트** | Claude Code, Cursor, OpenCode. 하나의 AI가 파일을 읽고 수정한다. |
| **4세대: 에이전트 팀** | **oh-my-opencode**. 전문화된 여러 AI가 역할을 나눠 협업한다. |

**개발 팁**  
이 패러다임 전환을 이해하는 것이 중요하다. oh-my-opencode를 단순히 "더 똑똑한 AI 도구"로 보면 활용도가 제한된다. "AI 팀을 관리하는 매니저"의 관점에서 접근해야 최대 효과를 얻을 수 있다.

## Sisyphus: 절대 포기하지 않는 오케스트레이터

**용어 설명: 오케스트레이터(Orchestrator)**

오케스트라의 지휘자처럼, 여러 에이전트들에게 작업을 분배하고 조율하는 역할을 한다. 어떤 에이전트가 어떤 작업을 맡을지 결정하고, 전체 작업 흐름을 관리하는 "총괄 책임자"이다.

oh-my-opencode의 핵심은 Sisyphus 에이전트이다. 그리스 신화에서 영원히 바위를 굴려 올리는 시시포스(시지푸스, 시지퍼스 로도 많이 읽는다.)처럼, 이 에이전트는 작업이 완료될 때까지 절대 멈추지 않는다.

### 이름의 의미

[DeepWiki 문서](https://deepwiki.com/code-yeongyu/oh-my-opencode/4.1-sisyphus-orchestrator) 에 따르면, Sisyphus는 "eternally rolling a boulder uphill"(영원히 바위를 언덕 위로 굴리는)이라는 시시포스(시지푸스, 시지퍼스 로도 많이 읽는다.) 신화에서 이름을 따왔다. 이는 작업이 완료될 때까지 지속적으로 실행하는 이 에이전트의 특성을 상징한다.

### 기술 사양

| 항목 | 사양 |
| --- | --- |
| **기본 모델** | Claude Opus 4.5 |
| **Extended Thinking** | 32k 토큰 예산 |
| **역할** | 메인 오케스트레이터 |
| **특징** | Aggressive Delegation (공격적 위임) |

### Aggressive Delegation 전략

Sisyphus의 핵심 전략은 "Aggressive Delegation"(공격적 위임)이다. [DeepWiki](https://deepwiki.com/code-yeongyu/oh-my-opencode) 에 따르면, Sisyphus는 가능한 모든 것을 전문 에이전트에게 위임한다. 이로 인해:

- **컨텍스트 깔끔하게 유지**: 메인 컨텍스트가 불필요한 정보로 오염되지 않음
- **병렬 작업 스트림 활성화**: 여러 작업이 동시에 백그라운드에서 진행됨
- **최적 모델 사용**: 각 작업에 가장 적합한 모델이 자동 선택됨

### Sisyphus 작업 흐름

1. **작업 분석**: 사용자 요청을 분석하여 필요한 하위 작업 식별
2. **에이전트 선택**: 각 하위 작업에 적합한 전문 에이전트 결정
3. **병렬 위임**: 여러 에이전트에게 동시에 작업 할당
4. **결과 통합**: 각 에이전트의 결과를 수집하여 최종 결과 생성
5. **완료 검증**: Todo Enforcer가 모든 작업 완료 여부 확인

## 전문화된 에이전트 팀

oh-my-opencode는 Sisyphus 외에도 각 영역에 특화된 에이전트 팀을 제공한다. 각 에이전트는 해당 작업에 최적화된 모델을 사용한다.

| 에이전트 | 역할 | 모델 | 호출 방법 |
| --- | --- | --- | --- |
| **Sisyphus** | 메인 오케스트레이터 | Claude Opus 4.5 (32k) | 기본 활성화 |
| **Oracle** | 아키텍처 설계, 디버깅 어드바이저 | GPT-5.2 Medium | `@oracle` |
| **Librarian** | 공식 문서 탐색, 코드 리서치 | GLM-4.7 Free | `@librarian` |
| **Explore** | 초고속 코드베이스 탐색 | Grok Code | `@explore` |
| **Frontend UI/UX** | 프론트엔드 개발 전문 | Gemini 3 Pro | 자동 호출 |
| **Document-Writer** | README, API 문서, 가이드 작성 | Gemini 3 Flash | 자동 호출 |
| **Multimodal-Looker** | PDF, 이미지, 다이어그램 분석 | Gemini 3 Flash | 자동 호출 |

### 에이전트 권한과 실행 모드

각 에이전트는 역할에 따라 **파일 권한** 과 **실행 모드** 가 다르게 설정된다. 이를 통해 안전하고 효율적인 병렬 작업이 가능하다.

| 에이전트 | 파일 권한 | 실행 모드 | 특징 |
| --- | --- | --- | --- |
| **Sisyphus** | Read + Write | Sync | 메인 오케스트레이터, 모든 도구 사용 가능 |
| **Oracle** | Read Only | Sync | 분석/설계 전문, 코드 수정 불가 |
| **Librarian** | Read Only | Async | 백그라운드 리서치 가능 |
| **Explore** | Read Only | Async | 빠른 탐색, 병렬 실행 최적화 |
| **Frontend UI/UX** | Read + Write | Async | 프론트엔드 파일 직접 수정 가능 |
| **Document-Writer** | Read + Write | Async | 문서 파일 생성/수정 가능 |
| **Multimodal-Looker** | Read Only | Async | 이미지/PDF 분석 전문 |

**Sync vs Async**: Sync 에이전트는 응답을 기다리며, Async 에이전트는 백그라운드에서 병렬 실행된다. 이를 통해 Sisyphus가 다른 작업을 진행하는 동안 여러 에이전트가 동시에 작업할 수 있다.

### Oracle: 설계와 디버깅 전문가

Oracle은 GPT-5.2 모델을 사용하며, 아키텍처 설계와 디버깅에 특화되어 있다. 복잡한 시스템 설계 결정이나 난해한 버그 분석이 필요할 때 자동 또는 수동으로 호출된다.

#### Oracle 호출 예시

```
@oracle 이 마이크로서비스 아키텍처에서 이벤트 소싱을 도입하려면 어떻게 설계해야 할까?

@oracle 이 스택 트레이스를 분석해줘. 왜 메모리 누수가 발생하는지 모르겠어.
```

### Librarian: 문서와 지식 전문가

Librarian은 공식 문서 탐색과 오픈소스 코드 리서치에 특화되어 있다. 새로운 라이브러리를 도입하거나 API 사용법을 확인할 때 유용하다.

#### Librarian 호출 예시

```
@librarian React 19의 새로운 훅 API 문서를 찾아줘

@librarian FastAPI에서 WebSocket 연결을 처리하는 공식 예제 코드 찾아줘
```

### Explore: 초고속 코드베이스 탐색기

Explore는 대규모 코드베이스를 빠르게 탐색하는 데 최적화되어 있다. 가벼운 모델을 사용하여 빠른 응답 속도를 보장한다.

**개발 팁**  
에이전트 선택에서 가장 중요한 것은 비용 대비 효율이다. 단순 검색에는 가벼운 Explore를, 복잡한 설계에는 Oracle을, 문서 리서치에는 Librarian을 사용하면 비용을 절감하면서 품질을 유지할 수 있다.

## 도구 비교: 순정 OpenCode vs oh-my-opencode

oh-my-opencode는 순정 OpenCode의 기본 도구 외에 IDE급 도구를 추가로 제공한다.

### 순정 OpenCode 기본 도구

bash edit write read grep glob list webfetch

### oh-my-opencode 추가 도구

LSP Integration AstGrep Session History Dynamic Codebase

| 도구 | 기능 | 세부 사항 | 장점 |
| --- | --- | --- | --- |
| **LSP Integration** | lsp\_hover, lsp\_goto\_definition, lsp\_find\_references, lsp\_rename, lsp\_diagnostics 등 | **11개 도구** | IDE 수준의 코드 네비게이션 |
| **AST-Grep** | AST 기반 코드 검색(search), 구조적 치환(replace) | **2개 작업, 25개 언어** | 정확하고 안전한 리팩토링 |
| **Session History** | session\_list, session\_read, session\_search, session\_info | **4개 도구** | 이전 작업 내용 빠른 참조 |
| **Dynamic Codebase** | 동적 코드베이스 탐색, 파일 변경 모니터링 | 실시간 | 실시간 코드 변경 추적 |

### 큐레이팅된 MCP 서버

oh-my-opencode는 미리 설정된 MCP(Model Context Protocol) 서버를 포함한다. 순정 OpenCode에서는 수동으로 설정해야 하지만, oh-my-opencode에서는 기본 포함되어 있다.

| MCP 서버 | 용도 |
| --- | --- |
| **Exa** | AI 최적화 웹 검색 |
| **Context7** | 공식 문서 검색 및 제공 |
| **Grep.app** | GitHub 전체 코드 검색 |

### 인증 플러그인 의존성

oh-my-opencode는 다양한 LLM 제공업체를 지원하기 위해 별도의 인증 플러그인에 의존한다. 이 플러그인들은 설치 시 자동으로 구성된다.

| 플러그인 | 버전 | 지원 서비스 | 비고 |
| --- | --- | --- | --- |
| `opencode-antigravity-auth` | @1.1.2 | Google Gemini | Antigravity 프로젝트 경유 |
| `opencode-openai-codex-auth` | latest | ChatGPT (OpenAI Codex) | ChatGPT Plus/Pro 필요 |

**주의**  
`opencode-antigravity-auth` 는 Antigravity 프로젝트를 통해 API를 호출한다. 프로젝트 접근 권한 문제로 404 에러가 발생할 수 있으며, 이 경우 표준 Google OAuth를 사용해야 한다. 자세한 내용은 [트러블슈팅](#troubleshooting) 섹션 참조.

### Multi-Account Load Balancing

Antigravity를 통해 Gemini API를 사용할 때, 단일 계정의 rate limit 문제를 해결하기 위해 최대 **10개의 Google 계정** 을 등록할 수 있다.

#### 자동 계정 전환 메커니즘

- 현재 계정이 rate limit에 도달하면 자동으로 다음 계정으로 전환
- 모든 계정을 라운드 로빈 방식으로 순환하여 부하 분산
- Gemini 무료 티어의 분당 요청 제한을 우회하는 데 효과적
```dockerfile
# 추가 계정 인증 (최대 10개)
antigravity auth           # 첫 번째 계정
antigravity auth --add     # 두 번째 계정 추가
antigravity auth --add     # 세 번째 계정 추가...
```

**Tip: 무료로 rate limit 극복하기**  
Google 계정은 무료로 생성할 수 있으므로, 여러 계정을 등록하면 Gemini API를 사비 부담 없이 더 많이 활용할 수 있다. 단, Google의 서비스 약관을 준수해야 한다.

## 핵심 기능

### Todo Continuation Enforcer: 완료까지 멈추지 않는다

LLM 에이전트의 가장 흔한 문제는 작업 중간에 멈추는 것이다. "여기까지 진행했습니다. 계속할까요?"라고 물어보며 사용자 입력을 기다리는 경우가 많다. Todo Continuation Enforcer는 이 문제를 해결한다.

**해결된 문제**  
[공식 문서](https://github.com/code-yeongyu/oh-my-opencode) 에 따르면, Todo Continuation Enforcer는 "chronic LLM habit of stopping mid-task"(작업 중간에 멈추는 LLM의 고질적 습관)를 방지한다. 세션은 완료되거나, 그렇지 않으면 멈추지 않는다.

### 컨텍스트 인텔리전스

**용어 설명: 컨텍스트 윈도우(Context Window)**

AI가 한 번에 "기억"할 수 있는 대화 내용의 최대 크기. 마치 책상 위에 펼쳐놓을 수 있는 종이의 양과 같다. 대화가 길어지면 오래된 내용은 "책상에서 떨어져" AI가 잊어버리게 된다.

LLM의 컨텍스트 윈도우는 제한되어 있다. oh-my-opencode는 여러 전략으로 이 문제를 관리한다.

- **선제적 압축(Preemptive Compaction)**: 책상이 가득 차기 전에 미리 내용을 요약 정리. 중요한 정보만 남기고 축약한다.
- **동적 정리(Dynamic Pruning)**: 더 이상 필요 없는 정보를 자동으로 정리. 오래된 대화나 중복 내용을 삭제한다.
- **도구 출력 축소(Tool Output Truncation)**: 도구 실행 결과에서 핵심만 남기고 나머지는 요약. 1000줄 로그에서 핵심 10줄만 유지하는 방식.

### 자동 컨텍스트 주입

oh-my-opencode는 파일을 읽을 때 관련 컨텍스트를 자동으로 주입한다.

#### Directory AGENTS.md Injector

파일을 읽으면 해당 디렉토리부터 프로젝트 루트까지의 모든 `AGENTS.md` 와 `README.md` 를 자동 주입한다.

```perl
project/
├── AGENTS.md              # 프로젝트 전체 컨텍스트
├── src/
│   ├── AGENTS.md          # src 디렉토리 컨텍스트
│   └── components/
│       ├── AGENTS.md      # 컴포넌트 컨텍스트
│       └── Button.tsx     # 이 파일 읽으면 3개 AGENTS.md 모두 주입
```

주입 순서: project/AGENTS.md → src/AGENTS.md → components/AGENTS.md. 각 디렉토리의 컨텍스트는 세션당 한 번만 주입된다.

#### Conditional Rules Injector

`.claude/rules/` 디렉토리의 규칙 파일을 조건에 따라 주입한다. globs 패턴으로 특정 파일에만 규칙을 적용할 수 있다.

```yaml
---
globs: ["*.ts", "src/**/*.js"]
description: "TypeScript/JavaScript 코딩 규칙"
---
- 인터페이스명은 PascalCase 사용
- 함수명은 camelCase 사용
```

`alwaysApply: true` 옵션으로 항상 적용되는 규칙도 설정 가능. 파일 경로부터 프로젝트 루트, `~/.claude/rules/` 까지 탐색한다.

### 백그라운드 병렬 작업

순정 OpenCode는 순차적으로 작업을 처리한다. oh-my-opencode는 여러 에이전트가 백그라운드에서 동시에 작업할 수 있다.

### 병렬 작업 예시

사용자가 "새 기능을 구현하고, 테스트를 작성하고, 문서를 업데이트해줘"라고 요청하면:

- **Sisyphus**: 전체 작업 계획 수립
- **메인 에이전트**: 기능 구현 (포그라운드)
- **테스트 에이전트**: 테스트 작성 (백그라운드)
- **문서 에이전트**: 문서 업데이트 (백그라운드)

#### call\_omo\_agent: 백그라운드 에이전트 실행

`call_omo_agent` 도구는 `run_in_background` 파라미터로 에이전트를 비동기 실행할 수 있다.

```csharp
// 백그라운드에서 테스트 작성 에이전트 실행
call_omo_agent({
  agent: "sisyphus",
  prompt: "모든 새 함수에 대해 단위 테스트 작성",
  run_in_background: true  // 비동기 실행
})

// 메인 스레드는 계속 진행
// 결과는 나중에 확인 가능
```

`run_in_background: true` 로 실행하면 결과를 기다리지 않고 즉시 다음 작업을 진행한다. 여러 에이전트를 동시에 실행하여 작업 시간을 단축할 수 있다.

### Claude Code 호환성 레이어

[공식 문서](https://github.com/code-yeongyu/oh-my-opencode) 에 따르면, oh-my-opencode는 Claude Code와 완전 호환되는 레이어를 제공한다. 다음 기능들이 호환된다:

### Hook 시스템 상세

oh-my-opencode의 Hook 시스템은 Claude Code와 완전 호환되며, **20개 이상의 이벤트 인터셉터** 를 제공한다. Hook을 통해 도구 실행 전후에 커스텀 로직을 삽입할 수 있다.

| Hook 유형 | 트리거 시점 | 용도 |
| --- | --- | --- |
| **PreToolExecution** | 도구 실행 전 | 입력 검증, 로깅, 권한 체크 |
| **PostToolExecution** | 도구 실행 후 | 결과 후처리, 메트릭 수집 |
| **Notification** | 특정 이벤트 발생 시 | Slack/Discord 알림, 외부 연동 |
| **Stop** | 세션 종료 시 | 정리 작업, 리소스 해제 |

**Hook 설정 예시**  
`.opencode/settings.json` 의 `hooks` 섹션에서 설정할 수 있다. Claude Code의 Hook 설정과 동일한 형식을 사용한다.

## 설치 및 설정 가이드

### 사전 요구사항

- **OpenCode**: 버전 1.0.150 이상
- **LLM 구독**: Claude Pro/Max, ChatGPT Plus/Pro, Google Gemini 중 하나 이상
- **Node.js**: bun 또는 npm 실행 가능 환경

### 기본 설치

// bun 사용 (권장)

```javascript
bunx oh-my-opencode install
```

ex) bunx oh-my-opencode install

\- 클로드 코드 구독 여부

![](https://blog.kakaocdn.net/dna/czIXZ1/dJMb99SBKel/AAAAAAAAAAAAAAAAAAAAANn6PI1jQut_54t1FqyUCge31UqOnd25xjK8JwFlWbA3/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=xkGgS8sBkyeJQNb0Tgy27wR0U%2BE%3D)

\- openAI 구독 여부

![](https://blog.kakaocdn.net/dna/bmQnDR/dJMcabplf2n/AAAAAAAAAAAAAAAAAAAAACMZfZ1neQwRRQu8Yo8JC6hUzLcJaoIBl6m4NYDyazSv/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=AraWUuYp20Nn9s7MwOQKODksK5w%3D)

\- gemini 구독 여부

![](https://blog.kakaocdn.net/dna/l4qyZ/dJMcaiosLVT/AAAAAAAAAAAAAAAAAAAAAFJvstC20XGpu_ug0BNSRdkVdgB_YVaA7OhF9eYlHM3g/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=6Wkrarn8UqxCTOo2a1ZT%2FcNH650%3D)

\- 위 3가지 단계를 선택하면 설치가 완료되며, 이후 작업해야 하는 step 에 대해서 안내해준다.

(인증부터 진행하면 되는데 하기에 별도로 작성해 두었다.)

![](https://blog.kakaocdn.net/dna/nm95L/dJMcachugKV/AAAAAAAAAAAAAAAAAAAAAIkoOsPA2cYVpiOHbpN3dr0TB9UHr9U_952cMVMk1tO6/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=x%2BEd2nTJQfEtBUKF9jGwSkSPOpU%3D)

// npm 사용 (Ubuntu/Debian Snap 환경)

```applescript
npx oh-my-opencode install
```

**주의사항**  
Ubuntu/Debian에서 Snap으로 Node.js를 설치한 경우, `bunx` 가 실패할 수 있다. 이 경우 `npx` 를 사용하면 된다.

### 구독 옵션별 설치 (CLI)

자동화 환경이나 LLM 에이전트가 설치를 수행하는 경우, 플래그를 사용하여 구독 정보를 전달할 수 있다.

// 모든 구독 + Claude max20 지원

```perl
bunx oh-my-opencode install --no-tui --claude=max20 --chatgpt=yes --gemini=yes
```

```perl
bunx oh-my-opencode install --no-tui --claude=yes --chatgpt=no --gemini=no
```

| 옵션 | 값 | 설명 |
| --- | --- | --- |
| `--claude` | yes / no / max20 | Claude Pro/Max 구독 여부 (max20은 Claude Max 요금제) |
| `--chatgpt` | yes / no | ChatGPT Plus/Pro 구독 여부 |
| `--gemini` | yes / no | Google Gemini 구독 여부 |

### 인증 설정

설치 후 각 LLM 제공자에 대한 인증을 설정해야 한다.

#### \[2026-01-09 업데이트\] Anthropic OAuth 인증 제한 (Anthropic 직원 공식 확인)

**Anthropic이 Claude Code OAuth 토큰을 공식 Claude Code에서만 사용 가능하도록 기술적 제한을 적용했습니다.**  
**공식 확인:** Thariq Shihipar (Anthropic 기술 스태프, Claude Code 담당)가 2026-01-10 X에서 확인: *"We tightened our safeguards against spoofing the Claude Code harness"*

**Anthropic 공식 입장:**

- 에러 메시지: `"This credential is only authorized for use with Claude Code and cannot be used for other API requests"`
- 제3자 도구(OpenCode, oh-my-opencode 등)에서 OAuth 방식 사용 시 **ToS(서비스 약관) 위반** 으로 간주
- 일부 사용자 계정 밴 사례 발생 ([GitHub Issue #6930](https://github.com/anomalyco/opencode/issues/6930))

**ToS 위반 근거** ([Anthropic Consumer Terms](https://www.anthropic.com/terms)):

- "You may not share your Account login information, Anthropic API key or Account credentials with anyone else."
- "to access the Services through automated or non-human means... except when you are accessing our Services via an Anthropic API Key or where we otherwise explicitly permit it"

**권장 대안:** Anthropic API 키 사용 (별도 [API 비용](https://console.anthropic.com/) 발생)

참고: Google Gemini, OpenAI(ChatGPT) OAuth는 현재까지 제한 없이 사용 가능합니다.

#### Anthropic (Claude) 인증

**주의:** 아래 OAuth 방식은 2026년 1월 기준 **ToS 위반** 으로 간주되어 **권장하지 않습니다**. API 키 방식을 사용하세요.

```shell
opencode auth login
# 제공자 목록에서 "Anthropic" 선택
# OAuth 흐름 완료
```

**권장 방식: API 키 사용**

```makefile
# 환경 변수로 API 키 설정
export ANTHROPIC_API_KEY="your-api-key-here"

# 또는 opencode.json에서 설정
# ~/.config/opencode/opencode.json
```

API 키는 [Anthropic Console](https://console.anthropic.com/settings/keys) 에서 발급받을 수 있습니다.

#### Google Gemini 인증

```shell
opencode auth login
# 제공자 목록에서 "Google" 선택
# OAuth 흐름 완료
# 최대 10개 계정 지원 (자동 로드밸런싱)
```

#### GPT 인증

```javascript
opencode auth login
# 제공자 목록에서 "OPEN AI" 선택
# OAuth 흐름 완료
```

~~ex) Anthropic 인증 (OAuth 방식 - 현재 ToS 위반)~~ ~~\- opencode auth login~~![](https://blog.kakaocdn.net/dna/bd51bL/dJMcab3W6Ms/AAAAAAAAAAAAAAAAAAAAAIfz1-IWLPDFM8RnnWoeKll1d37DG0vN_3AXMI4rEKvb/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=5MpceE0%2FtYOfLJYp2GC%2B%2BHAhYCo%3D)

~~\- 구독형 또는 API key 선택이 가능하다.~~![](https://blog.kakaocdn.net/dna/bK0btN/dJMcab3W6MF/AAAAAAAAAAAAAAAAAAAAAEBtIF5S3W1ukaAaREZnon-FTV5qNJvwB3oXAFTkGUYS/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=pXI2XqVINuC3Uc%2BAqArxzKJP0rE%3D)

**\[2026-01-09 업데이트\]**

~~( 구독형을 사용해서 많이 사용하다보면, anthropic에서 자동 차단을 하는 경우가 있다고 한다. 이런 경우 차단 해제 요청을 하면 된다고 하는데 아직 초기 단계이니 주의하여 사용하자. 주의 사항은 이전 세션에 작성해 두었다. )~~![](https://blog.kakaocdn.net/dna/AQJVk/dJMcagYuMSU/AAAAAAAAAAAAAAAAAAAAAEtBmTLy-9pqpcHTUu5694a4igGGpuTN5a0lzB5rNajw/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=2TM9Al1YLunyoJbELS6%2BE0%2BQUj4%3D)

**현재 상황:** Anthropic이 **구독형(OAuth) 인증을 제3자 도구에서 사용하는 것을 ToS 위반으로 규정** 했습니다. 단순 차단이 아닌 **계정 밴** 사례가 발생하고 있으므로, **반드시 API 키 방식을 사용** 하세요.

\- 링크 클릭 하여 인증하고, code를 복사하여 붙여 넣어 주자.

![](https://blog.kakaocdn.net/dna/CQ72D/dJMcadAEsW9/AAAAAAAAAAAAAAAAAAAAAK9zZfKv_pW-leLj3NdAPGjZauwpzke5BN2-qw0lF6hP/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=u9pi81UZ0iF0H5l1kXK3cwXHlpw%3D)

![](https://blog.kakaocdn.net/dna/bWkxAI/dJMcabbOsMs/AAAAAAAAAAAAAAAAAAAAAJQjo5GTphIAuP-XatC8TK32qUunew5Y7PPXS6OzoGDs/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=U636JUuBFO79uB0bKzb6aMYUhjQ%3D)

\- 인증 완료

![](https://blog.kakaocdn.net/dna/dmvbB1/dJMcab3W6Np/AAAAAAAAAAAAAAAAAAAAAIutP9chumjZ7OzrkfQtel9Hg8oI96lyWuJbw2uU_E2O/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=D5ODvjOUaiiQ0oWmL9zj8iLoBEI%3D)

ex) Open AI 인증

\- opencode auth login > 로그인 방법 선택 > 나의 경우는 Codex Subscription

![](https://blog.kakaocdn.net/dna/bFHwvg/dJMcag5g8GO/AAAAAAAAAAAAAAAAAAAAADvcHlQuWSXBjfziHTojbeSKA4JZek64Gocj--sSABjB/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=7l5310dVqZBgb%2Fxo9Com0U63pVA%3D)

\- 웹을 통한 Codex 로그인 처리

![](https://blog.kakaocdn.net/dna/bUoXnx/dJMcagqEsjB/AAAAAAAAAAAAAAAAAAAAAN-TJGtYSHUT1IjyaubFiTOa9AFdrfAvfmsMUfxkyuZ9/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=fXgxhmS9O%2Bax7oPMVvRhEpiIkI4%3D)

\- 최종 인증 완료

![](https://blog.kakaocdn.net/dna/cquBcy/dJMcagxpUQ7/AAAAAAAAAAAAAAAAAAAAAEMyzlPIVnLE9JP9VSGnOjhRPZVMEFKd-vdfpdzYmrCj/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=cC8ydUTIhye7a%2B9nMGrP6m8j9XU%3D)

ex) Google Gemini 인증

\- opencode auth login

![](https://blog.kakaocdn.net/dna/boIo6d/dJMcaiIJOLr/AAAAAAAAAAAAAAAAAAAAAMnuZ3KUet-XUH7O-6yBHCzK5c6p95Abd17K1Xa7UI_K/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=B%2B%2BmKsePAD0KlSnVdzgCcXxh1Dc%3D)

\- antigravity를 통한 인증방법을 선택 하는게 편하다.

( 안티그래비티, 반중력 설치 방법은 다음 글 참고: [Google Antigravity(안티그래비티, 반중력) 리뷰](https://goddaehee.tistory.com/424) )

![](https://blog.kakaocdn.net/dna/pLV6J/dJMcaaxc57n/AAAAAAAAAAAAAAAAAAAAAMJSt7cl8HF5suGRBNxrBIir7YvYgvyYigok-ZcD5LCz/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=wverVxHfrMskRJNJ7RadK6wB3s0%3D)

\- enter 입력

![](https://blog.kakaocdn.net/dna/z72cn/dJMcaaKKbv6/AAAAAAAAAAAAAAAAAAAAAAtBziWJL5nvD0Ho__2txM7tMVlN_pYC3-x0jXv8AZc_/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=qVvh%2BTqUrgIUOgVHVHpWubaAB2k%3D)

\- 여러 계정등록이 가능한데 나의 경우 포스팅용으로 일단 1개만 진행하도록 한다.

![](https://blog.kakaocdn.net/dna/b1OZ8F/dJMcabplgdX/AAAAAAAAAAAAAAAAAAAAABCsK8shwnaOvIVK9LP74HgFHB3QuxgyQSl5Hkpi6nrD/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=XibnK8gMfX6eO%2BBT7uF1OaU%2FDac%3D)

\- 다음과 같이 뜨면 정상 연동된 것이다.

![](https://blog.kakaocdn.net/dna/sjIz2/dJMcahb1NGY/AAAAAAAAAAAAAAAAAAAAAEIjqvNEDWQrHsPp5wBK9QV77arShtOf7uRnK-x0eJUw/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=Fu3xTlp1eFlMq18XEv%2BZxGu8bqU%3D)

\------- 혹시 위와 같은 페이지가 노출 안되고 오류 페이지가 뜬자면, 다음과 같이 설치해야할수도 있다. ----------

\- 브라우저의 주소를 복사해 주자.

![](https://blog.kakaocdn.net/dna/bNaJWO/dJMcachuhaa/AAAAAAAAAAAAAAAAAAAAADOKza203cuTxzoYx50-6V19Oe-2Z2PvDfdqCO5Z4Kv-/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=Cw%2F6HlZHKArzEW3758L6CJtzEx0%3D)

\- 다시 콘솔창으로 돌아와 입력하고 엔터 > 연동이 되었는데 또다른 계정 연동 여부를 물어본다.

![](https://blog.kakaocdn.net/dna/tzNVz/dJMcaf6lXkH/AAAAAAAAAAAAAAAAAAAAACFhMGghwF7Tx7SnD7-NHqkTZAoxE6eo4ob-R89gkVX_/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=gXxAEIYvRGlhuVnBy0bMY8uA25o%3D)

\- 원하는 갯수만큼 계정을 연동하여 완료 하자.

![](https://blog.kakaocdn.net/dna/ssRhU/dJMcagxpUXq/AAAAAAAAAAAAAAAAAAAAAOMJ2q1ez8oBpN0QEs0BfNLvtM1wMwA2eL-CHKHVDsfQ/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=gTaqQ5v6LT0epx9FFsXr%2F069Tc4%3D)

### 설치 확인

// OpenCode 버전 확인 (1.0.150 이상 필요)

```javascript
opencode --version
```

ex) opencode --version  
1.1.3

// 설정 파일에서 oh-my-opencode 플러그인 확인

```javascript
cat ~/.config/opencode/opencode.json
```

ex)

![](https://blog.kakaocdn.net/dna/6f820/dJMcaiIJOTy/AAAAAAAAAAAAAAAAAAAAAMhqSMuQHRjHvXFGdnJ91CN7syfmoMo8JJ3770p76gb6/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=GJcAKnIPA%2FfNRbzBvBVejzEXhd8%3D)

## 설정 파일 구조 이해하기

oh-my-opencode를 제대로 활용하려면 설정 파일의 위치와 역할을 이해해야 한다. 설치 후 문제가 발생하면 대부분 이 파일들의 설정 오류가 원인이다.

### 설정 파일 위치

```applescript
# 글로벌 설정 디렉토리 (모든 프로젝트에 적용)
~/.config/opencode/
├── opencode.json           # 플러그인 및 provider 설정
├── oh-my-opencode.json     # 에이전트별 모델 매핑
└── antigravity-accounts.json

# 인증 정보 디렉토리
~/.local/share/opencode/
└── auth.json               # API 키 및 인증 정보

# 프로젝트별 설정 (글로벌 설정을 override)
프로젝트루트/.opencode/
└── oh-my-opencode.json     # 해당 프로젝트에만 적용
```

**프로젝트별 설정 팁**  
프로젝트마다 다른 모델이나 에이전트 설정이 필요하다면, 프로젝트 루트에 `.opencode/oh-my-opencode.json` 을 생성한다. 이 파일은 글로벌 설정보다 우선 적용되므로, 프로젝트 특성에 맞는 맞춤 설정이 가능하다.  
  
**예시 활용:**  
• 프론트엔드 프로젝트: `frontend-ui-ux-engineer` 에 Gemini 3 Pro 지정  
• 백엔드 프로젝트: `oracle` 에 GPT-5.2 지정으로 아키텍처 리뷰 강화  
• 문서 작업: `document-writer` 에 빠른 Flash 모델 지정

| 파일 | 역할 | 수정 시점 |
| --- | --- | --- |
| `opencode.json` | 플러그인 활성화, 커스텀 provider 정의 | 새 provider 추가 시 |
| `oh-my-opencode.json` | 에이전트별 모델 지정 | 에이전트 모델 변경 시 |
| `auth.json` | API 키 저장 | 새 provider 인증 시 |

### oh-my-opencode.json 설정 예시

에이전트별로 사용할 모델을 직접 지정할 수 있다. 기본 설정을 그대로 사용해도 되지만, 특정 모델로 변경하고 싶다면 이 파일을 수정한다.

```json
// ~/.config/opencode/oh-my-opencode.json
{
  "$schema": "https://raw.githubusercontent.com/code-yeongyu/oh-my-opencode/master/assets/oh-my-opencode.schema.json",
  "google_auth": true,
  "agents": {
    "Sisyphus": {
      "model": "anthropic/claude-opus-4-5"
    },
    "oracle": {
      "model": "openai/gpt-5.2",
      "description": "아키텍처 설계, 코드 리뷰, 전략적 판단"
    },
    "librarian": {
      "model": "google/gemini-3-flash-preview"
    },
    "explore": {
      "model": "google/gemini-3-flash-preview"
    },
    "frontend-ui-ux-engineer": {
      "model": "google/gemini-3-pro-preview"
    },
    "document-writer": {
      "model": "google/gemini-3-flash-preview"
    }
  }
}
```

**권장 설정: google\_auth**  
위 예시에서 `"google_auth": true` 는 Google의 Application Default Credentials(ADC)를 사용하는 설정이다. OpenRouter API 대신 Google Cloud 직접 인증을 사용하면 **API 응답 속도가 개선** 되고, **비용도 절감** 될 수 있다.  
  
Google Cloud에 직접 인증하려면:  
1\. `gcloud auth application-default login` 실행  
2\. oh-my-opencode.json에서 `"google_auth": true` 설정  
  
※ 설정하지 않으면 모든 요청이 OpenRouter를 통해 라우팅됩니다.

**업데이트: Gemini 3 정식 출시**  
Gemini 3 모델들이 정식 출시(GA)되어 더 이상 `-preview` 접미사가 필요하지 않다고 한다. 만약 아직도 preview가 접미사로 붙는 경우 업데이트를 확인해보자.  
  
`google/gemini-3-flash` (권장)  
`google/gemini-3-pro`

### 사용 가능한 모델 확인하기

설정 전에 실제로 사용 가능한 모델을 확인하는 것이 좋다. 다음 명령어로 각 provider의 모델 목록을 조회할 수 있다.

```javascript
# Google 모델 중 Gemini 3 확인
opencode models google | grep gemini-3

# 특정 provider의 전체 모델 목록
opencode models anthropic
opencode models openai
opencode models google

# 인증 상태 확인
opencode auth list
```

ex) opencode models google | grep gemini-3

![](https://blog.kakaocdn.net/dna/EaPNT/dJMcacaIZVr/AAAAAAAAAAAAAAAAAAAAAAQRhD4DsqDjnJOjao_FS0Tek1wcd3k5ylLyWP0z-T_O/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=YvJVn4b4trcgsOjeKe%2BRwG5GnoE%3D)

ex) opencode models anthropic

![](https://blog.kakaocdn.net/dna/ONh91/dJMcafkY1Dk/AAAAAAAAAAAAAAAAAAAAAB5cOeFYqdbpzOiJJmEBF2T4imtBYNNOzjpJDplKzGzo/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=kcRgj9fvTzqHrGT8NOIIuNXCY0I%3D)

ex) opencode auth list

![](https://blog.kakaocdn.net/dna/YqxsW/dJMb99LPf6o/AAAAAAAAAAAAAAAAAAAAAFgmAWnk6viFWgzU6aRbnlG66KA8kvNtKQr37ocPsWsZ/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=mnW3AHLml%2Bo2MjT48Qvt379GiTA%3D)

## 사용법: ultrawork 키워드

oh-my-opencode의 모든 기능을 활성화하는 가장 간단한 방법은 `ultrawork` 또는 줄여서 `ulw` 를 프롬프트에 포함하는 것이다.

**핵심 포인트**  
`ultrawork` 한 단어만 포함하면 다음이 자동 활성화된다:  
• 병렬 에이전트 실행  
• 백그라운드 작업 활성화  
• Todo Continuation Enforcer 작동  
• 전문 에이전트 자동 위임  
• 완료까지 지속 실행

### ultrawork 사용 예시

#### 기본 사용

```javascript
이 프로젝트를 분석하고 리팩토링 계획을 세워줘 ultrawork

로그인 기능을 구현해줘 ulw

8000개의 ESLint 경고를 모두 수정해줘 ultrawork
```

`ultrawork` 를 입력하면 Sisyphus가 작업을 분석하고, 필요한 에이전트에게 위임하며, 모든 작업이 완료될 때까지 자동으로 진행한다.

ex) 이 프로젝트를 분석하고 리팩토링 계획을 세워줘 ultrawork

![](https://blog.kakaocdn.net/dna/bq2kda/dJMcagKYa6Y/AAAAAAAAAAAAAAAAAAAAAIfy7qNbFnDni7VhHYNUKfqfDZ9sahFaUaV97DXqRN0_/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=YzzLmi9fk%2BtUbvVfJZO%2FcOb2XBw%3D)

\- 한참동안 일을 이어 가는 모습.

![](https://blog.kakaocdn.net/dna/bh9ZKT/dJMcaaRvY55/AAAAAAAAAAAAAAAAAAAAACD_qoaG5Czx-XwBOW8gtHOK-kjj2LELpfQCzgbFsc7E/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=2Z0CzjwpQLndp%2FJuaHQ4zUPXMso%3D)

\- 내용을 보여드리고 싶은데.... 현재 내 MacBook M2 Max에서도 open code는 CLI 환경임에도 다른 CLI 환경보다 버벅이는 느낌이 많다. ㅠㅠ 나만 그런진 모르겠다. 아마 출력 내용이 길어지면 이를 모두 표현하려고 하다보니 스크롤이 길어지면 이런 현상이 좀 있는 것 같다.

\- 최종 요약된 내용만 참고차 작성 하려한다.

```javascript
이제 종합적인 분석과 전략적 리팩토링 계획이 완성되었습니다.
⚙ background_cancel [all=true]
---
# 🔍 프로젝트 분석 및 리팩토링 계획
## 📊 현재 상태 요약
### 기술 스택
| 항목 | 버전/상태 |
|------|----------|
| Next.js | 16.0.10 (App Router) |
| React | 19.2.1 |
| TypeScript | strict mode ✅ |
| Styling | Tailwind CSS v4 |
| Auth | Firebase |
| API Client | Axios (일부 fetch 혼용) |
| State Management | Context API만 사용 (별도 라이브러리 없음) |
### 프로젝트 규모
- **19개 라우트** (\`src/app/\`)
- **82개 'use client' 파일** (거의 모든 컴포넌트가 클라이언트)
- **36개 feature 컴포넌트** (\`src/components/features/\`)
- **5개 API 서비스** (\`src/services/\`)
- **2개 테스트 파일** (테스트 커버리지 매우 낮음)
---
🚨 발견된 주요 문제점
1. 메가 컴포넌트 문제 (Critical)
BlogInteractive.tsx가 1,500줄 이상으로, 10개+ 인터랙티브 타입(button, badge, accordion, tooltip, flipcard, toggle, cardgallery, particle, text3d, timeline)을 하나의 파일에서 관리
2. Server Component 미활용 (High)
- 모든 컴포넌트가 'use client' (82개 파일)
- App Router의 장점을 전혀 활용하지 못함
- Server Actions 미사용
3. API 레이어 비일관성 (Medium)
- Axios와 fetch 혼용 (nanobanaService.ts는 fetch 사용)
- 에러 처리 패턴 불일치 (일부는 {success: false} 반환, 일부는 throw)
- 토큰 주입 방식 불일치
4. 데이터 페칭 보일러플레이트 (Medium)
- TanStack Query/SWR 미사용
- 모든 곳에서 useEffect + useState 수동 패턴
- 로딩/에러 상태 반복 코드
5. 코드 조직 비일관성 (Low)
- 폴더 네이밍 혼재: email-template vs emailTemplate vs githubTrend
- 고아 CSS 모듈: Login.module.css
- 일부 feature만 로컬 hooks/components 보유

6. 테스트 부재 (Medium)
- 단 2개의 유닛 테스트 파일
- E2E 테스트는 5개 존재하나 커버리지 불충분
---
✅ 강점 (유지할 부분)
- 깔끔한 path alias 설정 (@/, @components/, @hooks/ 등)
- API DTO에 대한 우수한 TypeScript 타이핑
- AI 에러 핸들러의 재시도 로직 (aiErrorHandler.ts)
- Feature-based 조직 구조가 형성되고 있음
- Atomic UI 컴포넌트 (Button, Typography, Grid)
---
📋 6단계 리팩토링 계획
Phase 0: 가드레일 & 베이스라인 (Quick Win)
| 항목 | 내용 |
|------|------|
| 목표 | 리팩토링을 안전하고 측정 가능하게 만들기 |
| 작업 | • 변경 불가 계약 정의 (public API 시그니처 유지)<br>• 베이스라인 메트릭 스냅샷 (번들 크기, use client 수)<br>• 라우트별 스모크 체크리스트 작성 |
| 공수 | S (몇 시간) |
| 위험도 | 🟢 Low |
Phase 1: API 레이어 정규화 (최고 ROI)
| 항목 | 내용 |
|------|------|
| 목표 | Axios/fetch 혼용, 토큰 주입 변형, 에러 스타일 불일치 제거 |
| 작업 | • nanobanaService.ts를 Axios로 마이그레이션<br>• 에러 처리 표준화 (throw + boundary에서 UI 매핑)<br>• 토큰 주입을 Axios interceptor로 일원화 |
| 공수 | S-M (반나절~하루) |
| 위험도 | 🟡 Medium |
Phase 2: 데이터 페칭 전략 (보일러플레이트 제거)
| 항목 | 내용 |
|------|------|
| 목표 | useEffect 패턴을 TanStack Query로 점진적 대체 |
| 작업 | • TanStack Query provider 추가<br>• useXxxQuery / useXxxMutation 컨벤션 수립<br>• 읽기 위주 페이지(posts)와 mutation 플로우(upload) 먼저 마이그레이션 |
| 공수 | M (1-2일) |
| 위험도 | 🟡 Medium |
| 의존성 | Phase 1 권장 |
Phase 3: 구조 정리
| 항목 | 내용 |
|------|------|
| 목표 | 네비게이션 깊이 감소, 네이밍 일관성 확보 |
| 작업 | • 폴더 네이밍 표준화 (kebab-case 또는 camelCase 선택)<br>• 고아 스타일링 제거/이동 (Login.module.css)<br>• Page 컴포넌트 플래트닝 |
| 공수 | S-M (반나절~하루) |
| 위험도 | 🟢 Low-Medium |
Phase 4: 메가 컴포넌트 분해 (핵심)
| 항목 | 내용 |
|------|------|
| 목표 | BlogInteractive.tsx를 유지보수/테스트 가능하게 분해 |
| 작업 | • 인터랙티브 타입별 서브컴포넌트 분리 (ButtonGenerator, BadgeGenerator 등)<br>• 각 타입별 상태를 개별 hook으로 추출<br>• 메인 컴포넌트는 오케스트레이션/라우팅만 담당 |
| 공수 | L (3일+) |
| 위험도 | 🔴 High |
| 의존성 | Phase 0 (가드레일) |
Phase 5: Server Component 전환
| 항목 | 내용 |
|------|------|
| 목표 | 클라이언트 경계 축소, JS 페이로드 감소 |
| 작업 | • src/app/*/page.tsx를 Server Component로 전환<br>• Header를 서버 래퍼 + 클라이언트 아일랜드로 분리<br>• server-only 경계 도입 |
| 공수 | M-L (2-3일) |
| 위험도 | 🟡 Medium-High |
| 의존성 | Phase 3 권장 |
Phase 6: Server Actions 도입
| 항목 | 내용 |
|------|------|
| 목표 | 폼 핸들러 보일러플레이트 감소 |
| 작업 | • 내부 mutation에 Server Actions 적용<br>• Zod 유효성 검사 + 일관된 에러 매핑<br>• Firebase auth는 클라이언트 유지 |
| 공수 | M (1-2일) |
| 위험도 | 🟡 Medium |
| 의존성 | Phase 5 |
---
📈 성공 지표
| 메트릭 | 현재 | 목표 |
|--------|------|------|
| 'use client' 파일 수 | 82개 | 50개 이하 |
| BlogInteractive.tsx LOC | 1,500+ | 200 이하 (오케스트레이션만) |
| 유닛 테스트 파일 수 | 2개 | 주요 hook/service 커버리지 |
| useEffect 데이터 페칭 블록 | 다수 | TanStack Query로 대체 |
| API 에러 처리 패턴 | 2가지 혼재 | 1가지 표준 |
---
⚠️ 리팩토링 시 주의사항
1. Hydration 불일치 - 서버 사이드 전환 시 timestamp/random ID 주의
2. Double Retry Storm - TanStack Query retry + AI retry + Axios retry 중복 방지
3. 토큰 누출 위험 - 'use client' 파일에 auth 토큰 로직 import 주의
4. 장기 브랜치 금지 - 좁고 머지 가능한 슬라이스로 진행
---
🚫 리팩토링하지 않을 부분
- Path aliases 및 DTO 타이핑 - 이미 우수함
- Atomic UI 컴포넌트 (Button, Typography) - 접근성/테마 이슈 없으면 유지
- AI 에러 핸들러 - 대체하지 말고 통합
- 게임 feature (2048, bunny) - 클라이언트 중심 유지, hook 추출만
---
다음 단계: 어떤 phase부터 시작할지 또는 특정 비즈니스 크리티컬 라우트가 있다면 알려주세요. 해당 부분을 우선 마이그레이션하는 상세 계획을 수립하겠습니다
```

### 에이전트 직접 호출

특정 에이전트를 직접 호출하고 싶다면 `@` 멘션을 사용한다.

#### 에이전트 직접 호출 예시

```javascript
@oracle 이 시스템의 아키텍처를 어떻게 개선하면 좋을까?

@librarian React Query v5의 새로운 API 문서 찾아줘

@explore 이 프로젝트에서 인증 관련 코드가 어디에 있는지 찾아줘
```

\- 위에 작성해두었지만 기억 나지 않을 것 같아 다시 한번 얘기하자면.

오라클이 우리가 생각하는 그 Database Oracle이 아니다.

내 글일부 캡쳐 >>

![](https://blog.kakaocdn.net/dna/lbiBN/dJMcai21zhD/AAAAAAAAAAAAAAAAAAAAAGoAcIyCJjXB5HQU5RgzYMlgi955vNlwz4Dqz9LCrq58/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=zTmue22OKfomlvo6INXmxepHPvc%3D)

ex) @oracle 이 시스템의 아키텍처를 어떻게 개선하면 좋을까?

![](https://blog.kakaocdn.net/dna/bRhXUY/dJMcagEdmZc/AAAAAAAAAAAAAAAAAAAAAKcPacVD-0IMDSS9Jj_Dr8muz1wRmBZucSZnNzcPmdMw/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=wfHX4Gd5TnXuPdwlDB4FC47IBhA%3D)

\- 위에서 병렬 처리에대해 작성학도 하였지만, 실제 open code와 일을 하다보면 다음과 같이 병렬작업에 대한 내용도 확인 가능 할 것이다. 1~2 explore agents, 1-2 librarian agents... 컨텍스트를 수집할때 이때문에 클로드 코드보다 빠른것 처럼 느껴지긴 한다.

![](https://blog.kakaocdn.net/dna/SN6aW/dJMcafSPuVA/AAAAAAAAAAAAAAAAAAAAACqWlvyKer-94tWPQlL92yKJszBstSpRUcQXeJErUDW6/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=a5gPM7MiyfokSx%2FYBYVhR2SIAUY%3D)

\- 작업 사이 해당 서브 에이전트(oracle)이 작업하는 것도 실시간으로 확인 가능하다.

![](https://blog.kakaocdn.net/dna/wiENE/dJMcai21zCk/AAAAAAAAAAAAAAAAAAAAAOguzWhCqtmrvLbswZ1TRr2W22hP9MwvsQ-onoA3Z6_H/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=pS1Hf9j10exYqmVZS%2FAKRWzFLHs%3D)

\- 한참을 걸려 완성된 결과 예시

![](https://blog.kakaocdn.net/dna/kMsvm/dJMcagjS6N4/AAAAAAAAAAAAAAAAAAAAAOjaRx7WlYFxzVSM8Eg5E77OJGNMNabN0_YKrLhrA3xj/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1780239599&allow_ip=&allow_referer=&signature=eAvrxlDdPnSIo4i3r2gB3SfyEAU%3D)

### ultrawork vs 직접 호출

| 방식 | 언제 사용 | 특징 |
| --- | --- | --- |
| `ultrawork` | 복잡한 멀티스텝 작업 | Sisyphus가 자동으로 최적 에이전트 선택 |
| `@oracle` | 설계/디버깅 질문 | GPT-5.2로 직접 응답 |
| `@librarian` | 문서/코드 검색 | 빠른 리서치 결과 |
| `@explore` | 코드베이스 탐색 | 가장 빠른 응답 |

## 실제 성과 사례

oh-my-opencode는 $24,000 상당의 토큰을 소비하며 실제 프로덕션 환경에서 검증되었다. 커뮤니티에서 보고된 실제 성과 사례를 살펴보자.

#### 커뮤니티 후기

"Claude Code가 7일 할 일을 Sisyphus는 1시간에 완료했습니다."

"Knocked out 8000 eslint warnings with Oh My Opencode, just in a day"

— Jacob Ferrari

"45k 라인 Tauri 앱을 SaaS로 하룻밤에 전환했습니다."

"이건 정말, 정말, 정말 좋습니다."

— Henning Kilset

**공식 문서 출처**  
이 후기들은 [공식 GitHub README](https://github.com/code-yeongyu/oh-my-opencode) 에 인용된 실제 사용자 피드백이다.

### 성과 비교 (추정치)

| 작업 | 순정 OpenCode | oh-my-opencode | 개선율 |
| --- | --- | --- | --- |
| 대규모 리팩토링 | 수동 반복 필요 | 자동 완료 | \- |
| ESLint 경고 수정 (8000개) | 여러 세션 | 하루 | 큰 개선 |
| 복잡한 기능 구현 | 7일 (추정) | 1시간 | 168x |

※ 이 수치는 커뮤니티 후기를 기반으로 한 예시이며, 실제 성능은 작업 복잡도와 환경에 따라 다를 수 있다.

## 언제 무엇을 선택할까?

순정 OpenCode와 oh-my-opencode는 각각 적합한 사용 시나리오가 다르다. 상황에 맞는 도구를 선택하는 것이 중요하다.

#### 순정 OpenCode가 적합한 경우

- **단순 작업**: 간단한 코드 수정, 빠른 질문-응답
- **빠른 프로토타이핑**: 아이디어를 빠르게 구현해보고 싶을 때
- **리소스 제한 환경**: 단일 모델로 충분한 경우
- **비용 민감**: API 비용을 최소화하고 싶을 때
- **단일 LLM 사용**: 특정 모델만 사용하고 싶을 때

#### oh-my-opencode가 적합한 경우

- **대규모 리팩토링**: 수천 개의 경고/에러 수정, 전체 코드베이스 개선
- **복잡한 멀티스텝 작업**: 기능 구현 + 테스트 + 문서화를 한 번에
- **AI 팀 협업**: 여러 전문가가 필요한 작업
- **완료 보장 필요**: 작업이 중간에 멈추면 안 되는 경우
- **다양한 모델 활용**: 각 작업에 최적 모델을 사용하고 싶을 때
- **IDE급 도구 필요**: LSP, AstGrep 등 고급 도구가 필요할 때

**개발 팁**  
처음에는 순정 OpenCode로 시작하고, 작업이 복잡해지거나 에이전트가 자주 멈추는 문제를 경험하면 oh-my-opencode로 전환하는 것이 좋은 접근법이다.

## 주의사항 및 한계점

### 최소 요구사항

- **OpenCode 버전**: 1.0.150 이상 필수
- **LLM 구독**: Claude Pro/Max, ChatGPT Plus/Pro, Google Gemini 중 하나 이상 필요
- **Node.js 환경**: bun 또는 npm 실행 가능해야 함

### 알려진 이슈

**\[2026-01-09 업데이트\] Anthropic OAuth 기술적 제한 (Anthropic 직원 공식 확인)**

**Claude OAuth 인증 - 제3자 도구에서 사용 시 기술적으로 제한됨**  
  
**(Anthropic 공식 확인, 2026-01-10):**  
Anthropic이 Claude Code OAuth 토큰을 **공식 Claude Code에서만 사용 가능** 하도록 기술적 제한을 적용했습니다.  
**공식 확인:** Thariq Shihipar (Anthropic 기술 스태프)가 X에서 "Claude Code harness 스푸핑에 대한 보안 조치를 강화했다"고 공식 확인. 이 이슈로 차단된 계정은 모두 해제 완료.  
  
• **에러 메시지:** `"This credential is only authorized for use with Claude Code and cannot be used for other API requests"`  
• **ToS 위반 근거:** 자격증명 공유 금지 조항 + 비허가 자동화 접근 금지 조항  
**권장 대안:**  
• **Anthropic API 키 사용**: [Anthropic Console](https://console.anthropic.com/settings/keys) 에서 발급 (별도 API 비용 발생)  
• **다른 LLM 사용**: Google Gemini, OpenAI OAuth는 현재까지 제한 없음  
  
출처: [VentureBeat (2026-01-10)](https://venturebeat.com/technology/anthropic-cracks-down-on-unauthorized-claude-usage-by-third-party-harnesses)

**사용자 영향 및 커뮤니티 반응**  
  
**영향도:**  
이번 제한은 **Claude Max/Pro 구독자에게 상당한 타격** 이 예상됩니다. 대부분의 개발자들이 구독형으로 Claude Code를 사용하고 있기 때문입니다.  
  
• **구독형 사용 불가**: OpenCode에서 Claude Max/Pro 구독을 활용한 OAuth 로그인 방식 사용 불가  
• **API 전환 시 비용 부담**: API 키 방식은 구독과 별개로 사용량 기반 과금 발생 (토큰당 비용)  
• **구독료 + API 비용 이중 부담**: 기존 Claude Max $100~200/월 구독 외에 추가 API 비용 발생 가능  
  
**커뮤니티 동향:**  
• **Claude Code로 복귀**: 일부 개발자들은 OpenCode/oh-my-opencode를 포기하고 공식 Claude Code로 돌아가는 움직임  
• **다른 모델로 전환**: MiniMax M2.1, GPT-5 등 다른 LLM 기반으로 에이전트 재구성 시도  
• **OpenCode 유료화 대응**: OpenCode 측에서 $200 요금제 출시 예정 (별도 공식 제휴 추진 중으로 추정)  
  

**현실적 선택지:**  

| 선택지 | 장점 | 단점 |
| --- | --- | --- |
| **Claude Code로 복귀** | 구독료만으로 사용 가능, ToS 안전 | 멀티 모델/에이전트 기능 상실 |
| **API 키 전환** | OpenCode 기능 유지 | 추가 비용 부담, 사용량 관리 필요 |
| **다른 LLM 중심 구성** | Gemini/GPT OAuth 사용 가능 | Claude 품질 대비 성능 차이 가능 |

**\[참고\] OpenAI, 써드파티 도구에서 Codex 사용 공식 지원 (2026년 1월)**

Anthropic이 써드파티 도구 접근을 차단한 것과 **대조적으로**, OpenAI는 써드파티 도구에서 ChatGPT Plus/Pro 구독을 통한 Codex 사용을 **공식 지원** 하고 있다.

**OpenCode v1.1.11 Codex 인증 공식 지원**
- **지원 시작**: OpenCode v1.1.11부터 Codex OAuth 인증 공식 지원
- **사용 방법**: `/connect` 명령으로 OpenAI 로그인 후 OAuth 인증 완료
- **지원 플랜**: ChatGPT Plus, Pro, Business, Edu, Enterprise 플랜 모두 지원
- **OpenAI 입장**: 써드파티 도구 생태계 지원을 공개적으로 지지

(출처: [OpenAI Help Center](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan))

**Anthropic vs OpenAI 비교**

| 항목 | Anthropic (Claude) | OpenAI (Codex) |
| --- | --- | --- |
| 써드파티 도구 지원 | **차단** (ToS 위반) | **공식 지원** |
| 구독 플랜 사용 | API 키만 허용 | Plus/Pro OAuth 허용 |
| OpenCode 연동 | 별도 API 비용 발생 | 구독료만으로 사용 가능 |

**시사점:** Claude 구독자가 OpenCode/oh-my-opencode에서 Claude를 사용하려면 별도 API 비용이 발생하지만, ChatGPT Plus/Pro 구독자는 추가 비용 없이 Codex를 사용할 수 있다. 이는 중요한 대안이 될 수 있다.

**개인적으로는 Claude Code는 기존처럼 독립적으로 활용하고, 한편으로는 OpenCode + oh-my-opencode 조합을 기반으로 다시 한 번 커스터마이징해 사용하는 방향을 고민 중이다. ([Part 3: 오픈소스, 무료 및 저가 LLM 모델 활용](https://goddaehee.tistory.com/488) 참고)  
  
이 과정에서 기존에 Claude가 담당하던 역할을 Gemini나 Codex로 분산하거나, 혹은 Part 3: 오픈소스·무료·저가 LLM 모델 활용에서 언급한 것처럼 GLM 계열 모델로 대체하는 방식도 함께 검토하고 있다. 결국 목표는 단일 모델 의존에서 벗어나, 비용·성능·역할을 기준으로 LLM을 조합하는 구조를 직접 설계하고 커스터마이징 해봐야 할 것 같다.**

**\[2026-01-09\] Codex + Gemini 조합 최적화 구성 예시**

각 모델의 강점을 살린 oh-my-opencode.json 구성 예시:

```json
{
  "$schema": "https://raw.githubusercontent.com/code-yeongyu/oh-my-opencode/master/assets/oh-my-opencode.schema.json",
  "google_auth": false,
  "agents": {
    "librarian": { "model": "openai/gpt-5.2-codex:medium" },
    "explore": { "model": "google/antigravity-gemini-3-flash" },
    "plan": { "model": "openai/gpt-5.1-codex-max:high" },
    "frontend-ui-ux-engineer": { "model": "google/antigravity-gemini-3-pro-high" },
    "document-writer": { "model": "google/antigravity-gemini-3-flash" },
    "multimodal-looker": { "model": "google/antigravity-gemini-3-pro-high" }
  }
}
```

**구성 근거:**

| 에이전트 | 모델 | 선택 이유 |
| --- | --- | --- |
| **librarian** | Codex:medium | 코드베이스 탐색에 적당한 추론력 |
| **explore** | Gemini Flash | 빠른 탐색, 비용 효율 |
| **plan** | Codex-Max:high | 계획 수립에 깊은 사고 필요 |
| **frontend-ui-ux-engineer** | Gemini Pro High | 이미지/디자인 분석 강점 (멀티모달) |
| **document-writer** | Gemini Flash | 문서 작성에 빠른 응답 |
| **multimodal-looker** | Gemini Pro High | 이미지/PDF 분석 강점 |

\* Codex variant: low < medium < high < xhigh (추론 깊이/속도 트레이드오프)  
\* Gemini antigravity-: opencode-antigravity-auth 플러그인을 통한 Google OAuth 인증 모델  
\* opencode.json에 해당 모델들이 정의되어 있어야 위 구성이 동작함

**Claude 안전 사용 체크리스트 \[2026-01-09 업데이트\]**
- **API 키 사용 (필수)**: OAuth 대신 [Anthropic API 키](https://console.anthropic.com/settings/keys) 사용
- ~~**VPN Off**: Claude 접속 시 VPN 끄기~~ (API 키 사용 시 관련성 낮음)
- **Pre-paid**: 충전식 크레딧 사용으로 과금 폭탄 방지
- **Backup Model**: Sisyphus의 메인 모델을 Gemini 3 Pro나 GPT-5로 설정하여 Claude 의존도 분산
- **Usage Limit 설정**: API Console에서 월간 사용량 제한 설정 권장

**밴 후 대안 모델 (커뮤니티 추천)**  
Claude Max 계정이 정지된 경우 다음 대안을 고려할 수 있다:  
  

| **GPT-5.2** | 높은 품질, 가장 많이 추천됨 |
| --- | --- |
| **Sonnet 4.5 with thinking** | 좋은 결과 보고됨 |
| **Google AI Ultra** | 여러 사용자가 전환 |
| **GitHub Copilot → Claude Opus** | 우회 방법으로 제안됨 |

**메모리 누수 이슈 (해결됨)**  
초기 버전에 존재했던 메모리 누수(#361) 이슈는 v2.1 업데이트에서 **완전히 해결** 되었다. 이제 24시간 이상의 장기 세션도 안정적으로 유지된다.

### 비용 고려

oh-my-opencode는 여러 모델을 동시에 사용하므로, 순정 OpenCode보다 비용이 증가할 수 있다. 특히:

- **병렬 에이전트**: 여러 에이전트가 동시에 작동하면 토큰 소비 증가
- **Opus 4.5 사용**: Sisyphus가 사용하는 Opus 4.5는 비용이 높은 모델
- **Todo Enforcer**: 완료까지 자동 진행하므로 예상보다 많은 토큰 소비 가능

**비용 관리 팁**  
• 단순 작업에는 순정 OpenCode 사용  
• 복잡한 작업에만 `ultrawork` 활성화  
• 에이전트 직접 호출(@oracle 등)로 필요한 기능만 사용

## 트러블슈팅 가이드

1\. Authorization Failure / ProviderInitError

**증상:**
```makefile
ProviderInitError: ProviderInitError
Authorization Failure
```

**원인:** Z.AI 관련 provider를 잘못 선택한 경우 발생한다. Z.AI Coding Plan 구독자는 일반 `zai` 가 아닌 `zai-coding-plan` provider를 사용해야 한다.

```javascript
// 잘못된 설정
"oracle": { "model": "z.ai/glm-4.7" }
"oracle": { "model": "zai/glm-4.7" }

// 올바른 설정 (Z.AI Coding Plan 구독자)
"oracle": { "model": "zai-coding-plan/glm-4.7" }
```

### 2\. Insufficient Balance 오류

**증상:**
```perl
Insufficient balance or no resource package. Please recharge.
```

**원인:** Z.AI Coding Plan API 키를 일반 Zhipu AI endpoint(`open.bigmodel.cn`)에서 사용하려고 시도한 경우이다.

| Provider | API Endpoint | 용도 |
| --- | --- | --- |
| `zai` | open.bigmodel.cn | 일반 Zhipu AI API |
| `zhipuai` | open.bigmodel.cn | 일반 Zhipu AI API |
| `zai-coding-plan` | api.z.ai | **Z.AI Coding Plan 구독자용** |

**해결:** Z.AI Coding Plan 구독자는 반드시 `zai-coding-plan` provider를 사용해야 한다.

### 3\. Antigravity 404 에러

**증상:**
```groovy
Requested entity was not found.
Status: 404
Project: pure-card-t3lbr
Endpoint: https://cloudcode-pa.googleapis.com/...
```

**원인:** `opencode-antigravity-auth` 플러그인이 Google 요청을 가로채서 Antigravity 프로젝트를 통해 API를 호출하는데, 해당 프로젝트 접근 권한에 문제가 있다.

**해결:** `opencode.json` 에서 `opencode-antigravity-auth` 플러그인을 제거하고 표준 Google OAuth를 사용한다.

```json
// ~/.config/opencode/opencode.json
{
  "plugin": [
    "opencode-openai-codex-auth",
    "oh-my-opencode"
    // "opencode-antigravity-auth" 제거
  ]
}
```

### 4\. 모델이 Claude로 응답하는 문제

**증상:**

Oracle 에이전트에게 질문했는데 "저는 Claude AI입니다"라고 응답한다.

**원인:** `opencode/glm-4.7-free` 는 OpenCode에서 제공하는 무료 모델로, 실제로는 Claude 기반이다.

**해결:** GLM-4.7을 직접 사용하려면 Z.AI Coding Plan API 키로 `zai-coding-plan/glm-4.7` 을 설정해야 한다.

### 5\. 모델 404 에러 (Model Not Found)

**증상:**

특정 에이전트(frontend-ui-ux-engineer 등) 선택 시 모델을 찾을 수 없다는 404 에러 발생

**원인:** Gemini 3 모델명에 `-preview` 접미사를 붙이지 않았다.

```json
// ❌ 잘못된 설정 (404 발생)
"model": "google/gemini-3-flash"
"model": "google/gemini-3-pro"

// ✅ 올바른 설정
"model": "google/gemini-3-flash-preview"
"model": "google/gemini-3-pro-preview"
```

**확인 방법:**

```perl
opencode models google | grep gemini-3
```

### 6\. Hook이 비활성화해도 실행되는 문제

**증상:**

Hook을 비활성화(`enabled: false`)했는데도 계속 트리거된다.

**상태:** 해결됨 (v1.5+). 이제 `enabled: false` 설정이 정상적으로 동작한다.

### 7\. 종료 후 에이전트가 계속 실행되는 문제

**증상:**

`/exit` 또는 `Ctrl+C` 로 종료해도 백그라운드 에이전트가 계속 실행되거나, 비정상적인 동작이 발생한다.

**상태:** GitHub Issue [#541](https://github.com/opencode-ai/opencode/issues/541) 에서 보고됨.

**임시 해결:** 터미널을 완전히 종료하거나, `ps aux | grep opencode` 로 잔존 프로세스를 확인 후 수동 종료한다.

### 8\. 백그라운드 에이전트 출력 확인 불가

**증상:**

병렬로 실행 중인 백그라운드 에이전트의 출력을 실시간으로 확인할 수 없다.

**상태:** GitHub Issue [#523](https://github.com/opencode-ai/opencode/issues/523) 에서 기능 요청 중.

**현재 방법:** `/tasks` 명령어로 실행 중인 태스크 목록을 확인하고, 완료될 때까지 대기해야 한다.

### 트러블슈팅 체크리스트

오류 발생 시 아래 체크리스트를 순서대로 확인한다.

| 문제 | 확인 사항 |
| --- | --- |
| **Authorization Failure** | `zai-coding-plan` provider 사용 여부 확인 |
| **Insufficient Balance** | Z.AI Coding Plan 구독 상태, 올바른 provider 확인 |
| **Antigravity 404** | `opencode-antigravity-auth` 플러그인 제거 |
| **모델 404** | `gemini-3-flash-preview`, `gemini-3-pro-preview` 사용 |
| **GLM-4.7이 Claude로 응답** | `opencode/glm-4.7-free` 대신 `zai-coding-plan/glm-4.7` 사용 |
| **인증 실패 전반** | `opencode auth list` 로 인증 상태 확인 |

**참고 자료**  
이 트러블슈팅 가이드는 [vibelabs.kr의 실제 사용 경험](https://vibelabs.kr/columns/19) 을 바탕으로 작성되었다.

## 자주 묻는 질문

Q: oh-my-opencode는 무료인가?

A: oh-my-opencode 플러그인 자체는 무료 오픈소스이다. 그러나 사용하는 LLM 제공자(Claude, ChatGPT, Gemini)에 대한 구독이 필요하며, API 사용량에 따라 비용이 발생한다.

Q: Claude Code가 이미 있는데 왜 oh-my-opencode를 사용해야 하나?

A: Claude Code는 Claude 모델만 사용할 수 있지만, oh-my-opencode는 Claude, ChatGPT, Gemini를 역할별로 최적화하여 사용한다. 또한 멀티 에이전트 협업, 병렬 실행, Todo Enforcer 등 Claude Code에 없는 기능을 제공한다.

Q: 기존 OpenCode 설정과 호환되는가?

A: [공식 문서](https://github.com/code-yeongyu/oh-my-opencode) 에 따르면, oh-my-opencode는 Claude Code 호환성 레이어를 제공하므로 기존 설정과 대부분 호환된다. 다만 일부 고급 설정은 확인이 필요하다.

Q: 어떤 구독이 필수인가?

A: Claude Pro/Max, ChatGPT Plus/Pro, Google Gemini 중 하나 이상이 필요하다. 모든 구독이 있으면 최적의 성능을 얻을 수 있지만, 하나만 있어도 사용 가능하다.

Q: Sisyphus가 멈추지 않으면 비용 폭탄이 아닌가?

A: Todo Enforcer는 "작업 완료"까지 지속하지, "무한 반복"하지 않는다. 작업이 완료되면 자연스럽게 종료된다. 다만 복잡한 작업에서는 예상보다 많은 토큰을 소비할 수 있으므로 모니터링이 권장된다.

Q: 로컬 모델(Ollama)과 함께 사용할 수 있는가?

A: oh-my-opencode는 기본적으로 Claude, ChatGPT, Gemini 구독을 전제로 설계되었다. 로컬 모델과의 호환성은 공식 문서에서 명확히 언급되지 않으며, 실제 테스트가 필요하다.

## 참고 자료

### 공식 자료

- [oh-my-opencode GitHub 저장소](https://github.com/code-yeongyu/oh-my-opencode) - 공식 소스 코드와 문서
- [DeepWiki 문서](https://deepwiki.com/code-yeongyu/oh-my-opencode) - 상세 아키텍처 설명과 에이전트 분석
- [npm 패키지](https://www.npmjs.com/package/oh-my-opencode) - 공식 npm 배포

### GitHub Issues (알려진 이슈)

oh-my-opencode

- [Issue #158: Claude Max 계정 밴 사례](https://github.com/code-yeongyu/oh-my-opencode/issues/158) - OAuth 사용 시 주의사항
- [Issue #115: Safety 논의](https://github.com/code-yeongyu/oh-my-opencode/issues/115) - Claude 구독 사용 안전성 토론
- [Issue #361: 메모리 누수](https://github.com/code-yeongyu/oh-my-opencode/issues/361) - 장시간 사용 시 메모리 증가 현상

OpenCode (기반 플랫폼)

- **\[2026-01-09 추가\]** [Issue #6930: Anthropic OAuth ToS 위반 및 계정 밴](https://github.com/anomalyco/opencode/issues/6930) - **Claude OAuth 사용 시 계정 밴 사례 보고**
- [Anthropic Consumer Terms of Service](https://www.anthropic.com/terms) - ToS 위반 근거 (자격증명 공유 금지 조항)

OpenCode 기타 이슈

- [Issue #530: Hook 비활성화 무시](https://github.com/opencode-ai/opencode/issues/530) - enabled: false가 작동하지 않는 문제
- [Issue #541: 종료 후 비정상 동작](https://github.com/opencode-ai/opencode/issues/541) - exit 후 에이전트 계속 실행
- [Issue #523: 백그라운드 에이전트 출력](https://github.com/opencode-ai/opencode/issues/523) - 병렬 실행 중 출력 확인 불가

### 관련 프로젝트

- [OpenCode 공식 웹사이트](https://opencode.ai/) - 기반 플랫폼
- [OpenCode GitHub](https://github.com/sst/opencode) - OpenCode 소스 코드

이 글은 2026년 1월 기준 공식 문서와 커뮤니티 자료를 바탕으로 작성되었다. oh-my-opencode는 활발히 개발되고 있는 프로젝트이므로, 최신 정보는 [공식 GitHub](https://github.com/code-yeongyu/oh-my-opencode) 에서 확인하는 것이 좋다.

300x250

[저작자표시 비영리 변경금지 (새창열림)](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.ko)

#### 'AI > OhMyOpencode' 카테고리의 다른 글

| [Open Code 리뷰(4): OpenCode(oh-my-opencode)에 Z.ai GLM 연동하기(with claude code Z.aiGLM연동)](https://goddaehee.tistory.com/492) (8) | 2026.01.15 |
| --- | --- |
| [Open Code 리뷰(3): 오픈소스, 무료 및 저가 LLM 모델 활용 해보기 with Ollama, Qwen3, glm4.7, MiniMax M2.1 등](https://goddaehee.tistory.com/488) (17) | 2026.01.08 |
| [Open Code 리뷰(1): OpenCode 설치(oh-my-opencode 사전 학습) 및 설정, 기본 명령어 살펴보기](https://goddaehee.tistory.com/484) (3) | 2026.01.06 |

Contents

- 목차
- OpenCode vs oh-my-opencode
- 에이전트의시대:패러다임전환
- AI코딩도구의진화단계
- Sisyphus:절대포기하지않는오케스트레이터
- 이름의의미
- 기술사양
- AggressiveDelegation전략
- Sisyphus작업흐름
- 전문화된에이전트팀
- 에이전트권한과실행모드
- Oracle:설계와디버깅전문가
- Oracle호출예시
- Librarian:문서와지식전문가
- Librarian호출예시
- Explore:초고속코드베이스탐색기
- 도구비교:순정OpenCodevsoh-my-opencode
- 순정OpenCode기본도구
- oh-my-opencode추가도구
- 큐레이팅된MCP서버
- 인증플러그인의존성
- Multi-AccountLoadBalancing
- 자동계정전환메커니즘
- 핵심기능
- TodoContinuationEnforcer:완료까지멈추지않는다
- 컨텍스트인텔리전스
- 자동컨텍스트주입
- DirectoryAGENTS.mdInjector
- ConditionalRulesInjector
- 백그라운드병렬작업
- 병렬작업예시
- call\_omo\_agent:백그라운드에이전트실행
- ClaudeCode호환성레이어
- Hook시스템상세
- 설치및설정가이드
- 사전요구사항
- 기본설치
- 구독옵션별설치(CLI)
- 인증설정
- \[2026-01-09업데이트\]AnthropicOAuth인증제한(Anthropic직원공식확인)
- Anthropic(Claude)인증
- GoogleGemini인증
- GPT 인증
- 설치확인
- 설정파일구조이해하기
- 설정파일위치
- oh-my-opencode.json설정예시
- 사용가능한모델확인하기
- 사용법:ultrawork키워드
- ultrawork사용예시
- 기본사용
- 에이전트직접호출
- 에이전트직접호출예시
- ultraworkvs직접호출
- 실제성과사례
- 커뮤니티후기
- 성과비교(추정치)
- 언제무엇을선택할까?
- 순정OpenCode가적합한경우
- oh-my-opencode가적합한경우
- 주의사항및한계점
- 최소요구사항
- 알려진이슈
- 비용고려
- 트러블슈팅가이드
- 2.InsufficientBalance오류
- 3.Antigravity404에러
- 4.모델이Claude로응답하는문제
- 5.모델404에러(ModelNotFound)
- 6.Hook이비활성화해도실행되는문제
- 7.종료후에이전트가계속실행되는문제
- 8.백그라운드에이전트출력확인불가
- 트러블슈팅체크리스트
- 자주묻는질문
- 참고자료
- 공식자료
- GitHubIssues(알려진이슈)
- 관련프로젝트

### TAG

,,,,,,,,,

PREV

### [Open Code 리뷰(3): 오픈소스, 무료 및 저가 LLM 모델 활용 해보기 with Ollama, Qwen3, glm4.7, MiniMax M2.1 등](https://goddaehee.tistory.com/488)

[댓글 18](#0)

- ![프로필사진](https://i1.daumcdn.net/thumb/C100x100/?fname=https://t1.daumcdn.net/tistory_admin/static/manage/images/r3/default_S.png)
	익명
	비밀댓글입니다.
	[수정/삭제](#) I [답글](#)
	- ㄴ
		![프로필사진](https://i1.daumcdn.net/thumb/C100x100/?fname=https://t1.daumcdn.net/tistory_admin/static/manage/images/r3/default_S.png)
		[익명](https://goddaehee.tistory.com/485#comment15648035)
		비밀댓글입니다.
		[수정/삭제](#)
- ![프로필사진](https://i1.daumcdn.net/thumb/C100x100/?fname=https://t1.daumcdn.net/tistory_admin/static/manage/images/r3/default_S.png)
	익명
	비밀댓글입니다.
	[수정/삭제](#) I [답글](#)
	- ㄴ
		![프로필사진](https://i1.daumcdn.net/thumb/C100x100/?fname=https://t1.daumcdn.net/tistory_admin/static/manage/images/r3/default_S.png)
		[익명](https://goddaehee.tistory.com/485#comment15649071)
		비밀댓글입니다.
		[수정/삭제](#)
- ![프로필사진](https://i1.daumcdn.net/thumb/C100x100/?fname=https://t1.daumcdn.net/tistory_admin/static/manage/images/r3/default_S.png)
	익명
	비밀댓글입니다.
	[수정/삭제](#) I [답글](#)
	- ㄴ
		![프로필사진](https://i1.daumcdn.net/thumb/C100x100/?fname=https://t1.daumcdn.net/tistory_admin/static/manage/images/r3/default_S.png)
		[익명](https://goddaehee.tistory.com/485#comment15656019)
		비밀댓글입니다.
		[수정/삭제](#)
- [홍도리 재테크 성장일기](https://mobom.co.kr/)
	잘 보고 갑니다!
	[수정/삭제](#) I [답글](#)
- [도깨비영](https://dreams2025.com/)
	잘보구갑니다~  
	맛점하세요 (\*^ー^)ノ♪
	[수정/삭제](#) I [답글](#)
- [rntlife](https://betterlifecamp.tistory.com/)
	잘 보고 갑니다
	[수정/삭제](#) I [답글](#)
- [Finders log](https://sunnyonul.tistory.com/)
	잘 보았습니다
	[수정/삭제](#) I [답글](#)
- [금융보험정보창고](https://note2122.tistory.com/)
	포스팅 잘 보고 갑니다ㅎ
	[수정/삭제](#) I [답글](#)
- [이짚](https://2-zip.tistory.com/)
	좋은 글 잘 보고 갑니다 ㅎㅎ 제 블로그에도 놀러오세요 ◠‿◠
	[수정/삭제](#) I [답글](#)
- [Yulmuule](https://yulmuule.tistory.com/)
	잘 보고 갑니다.🧐 좋은하루☀️보내세요😆
	[수정/삭제](#) I [답글](#)
- [뚜벅 뚜벅](https://kangsan01.tistory.com/)
	잘보고 갑니다
	[수정/삭제](#) I [답글](#)
- [BLS(beautiful life story)](https://msong1.tistory.com/)
	좋은 포스팅 잘보고 갑니다. 겨울에 따뜻하고 건강하게 보내십시오.
	[수정/삭제](#) I [답글](#)
- ![프로필사진](https://i1.daumcdn.net/thumb/C100x100/?fname=https://t1.daumcdn.net/tistory_admin/static/manage/images/r3/default_S.png)
	익명
	비밀댓글입니다.
	[수정/삭제](#) I [답글](#)
	- ㄴ
		![프로필사진](https://i1.daumcdn.net/thumb/C100x100/?fname=https://t1.daumcdn.net/tistory_admin/static/manage/images/r3/default_S.png)
		[익명](https://goddaehee.tistory.com/485#comment15666722)
		비밀댓글입니다.
		[수정/삭제](#)
- [diary7555](https://diary7555.tistory.com/)
	안녕하세요 글 너무 유용하게 읽었습니다. ChatGPT PRO 모델 구독중이라 gpt를 등록하고싶은데요  
	gpt-5.2 pro 모델을 사용할 방법은 없는건가요? 현재 gpt-5.2만 지원 되는 것 같아서요!  
	  
	variant값을 넣으면 되는 것인지. Variant를 넣는다면 어떤 값을 넣어야하는건지 궁금합니다! 혹은 다른 방법은 없는 것일까요
	[수정/삭제](#) I [답글](#)

**소중한 공감 감사합니다**
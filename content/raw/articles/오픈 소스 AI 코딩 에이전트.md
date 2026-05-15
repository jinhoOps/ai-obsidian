---
type: "raw"
category: "article"
source: "https://opencode.ai/"
author:
clipped_date: 2026-05-15
tags:
  - "article"
  - "ingest-ready"
---
# 오픈 소스 AI 코딩 에이전트

> [!ABSTRACT] AI Ingest Instruction
> 이 파일은 `raw/articles`에 저장된 원본 소스입니다. 
> 인제스트 시 핵심 내용을 요약하고, `wiki/sources/`에 페이지를 생성하며 관련 엔티티를 연결하세요.

## 메타데이터
- 원본 URL: https://opencode.ai/
- 저자: 
- 수집일: 2026-05-15T14:24:40+09:00

---

[![OpenCode](data:image/svg+xml,%3csvg%20width='234'%20height='42'%20viewBox='0%200%20234%2042'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M18%2030H6V18H18V30Z'%20fill='%23CFCECD'/%3e%3cpath%20d='M18%2012H6V30H18V12ZM24%2036H0V6H24V36Z'%20fill='%23656363'/%3e%3cpath%20d='M48%2030H36V18H48V30Z'%20fill='%23CFCECD'/%3e%3cpath%20d='M36%2030H48V12H36V30ZM54%2036H36V42H30V6H54V36Z'%20fill='%23656363'/%3e%3cpath%20d='M84%2024V30H66V24H84Z'%20fill='%23CFCECD'/%3e%3cpath%20d='M84%2024H66V30H84V36H60V6H84V24ZM66%2018H78V12H66V18Z'%20fill='%23656363'/%3e%3cpath%20d='M108%2036H96V18H108V36Z'%20fill='%23CFCECD'/%3e%3cpath%20d='M108%2012H96V36H90V6H108V12ZM114%2036H108V12H114V36Z'%20fill='%23656363'/%3e%3cpath%20d='M144%2030H126V18H144V30Z'%20fill='%23CFCECD'/%3e%3cpath%20d='M144%2012H126V30H144V36H120V6H144V12Z'%20fill='%23211E1E'/%3e%3cpath%20d='M168%2030H156V18H168V30Z'%20fill='%23CFCECD'/%3e%3cpath%20d='M168%2012H156V30H168V12ZM174%2036H150V6H174V36Z'%20fill='%23211E1E'/%3e%3cpath%20d='M198%2030H186V18H198V30Z'%20fill='%23CFCECD'/%3e%3cpath%20d='M198%2012H186V30H198V12ZM204%2036H180V6H198V0H204V36Z'%20fill='%23211E1E'/%3e%3cpath%20d='M234%2024V30H216V24H234Z'%20fill='%23CFCECD'/%3e%3cpath%20d='M216%2012V18H228V12H216ZM234%2024H216V30H234V36H210V6H234V24Z'%20fill='%23211E1E'/%3e%3c/svg%3e) ![OpenCode](data:image/svg+xml,%3csvg%20width='234'%20height='42'%20viewBox='0%200%20234%2042'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M18%2030H6V18H18V30Z'%20fill='%234B4646'/%3e%3cpath%20d='M18%2012H6V30H18V12ZM24%2036H0V6H24V36Z'%20fill='%23B7B1B1'/%3e%3cpath%20d='M48%2030H36V18H48V30Z'%20fill='%234B4646'/%3e%3cpath%20d='M36%2030H48V12H36V30ZM54%2036H36V42H30V6H54V36Z'%20fill='%23B7B1B1'/%3e%3cpath%20d='M84%2024V30H66V24H84Z'%20fill='%234B4646'/%3e%3cpath%20d='M84%2024H66V30H84V36H60V6H84V24ZM66%2018H78V12H66V18Z'%20fill='%23B7B1B1'/%3e%3cpath%20d='M108%2036H96V18H108V36Z'%20fill='%234B4646'/%3e%3cpath%20d='M108%2012H96V36H90V6H108V12ZM114%2036H108V12H114V36Z'%20fill='%23B7B1B1'/%3e%3cpath%20d='M144%2030H126V18H144V30Z'%20fill='%234B4646'/%3e%3cpath%20d='M144%2012H126V30H144V36H120V6H144V12Z'%20fill='%23F1ECEC'/%3e%3cpath%20d='M168%2030H156V18H168V30Z'%20fill='%234B4646'/%3e%3cpath%20d='M168%2012H156V30H168V12ZM174%2036H150V6H174V36Z'%20fill='%23F1ECEC'/%3e%3cpath%20d='M198%2030H186V18H198V30Z'%20fill='%234B4646'/%3e%3cpath%20d='M198%2012H186V30H198V12ZM204%2036H180V6H198V0H204V36Z'%20fill='%23F1ECEC'/%3e%3cpath%20d='M234%2024V30H216V24H234Z'%20fill='%234B4646'/%3e%3cpath%20d='M216%2012V18H228V12H216ZM234%2024H216V30H234V36H210V6H234V24Z'%20fill='%23F1ECEC'/%3e%3c/svg%3e)](https://opencode.ai/ko)

신규

데스크톱 앱 베타 버전 출시 macOS, Windows, Linux 지원.[지금 다운로드](https://opencode.ai/ko/download) [데스크톱 베타 다운로드](https://opencode.ai/ko/download)

무료 모델이 포함되어 있으며, 어떤 제공자의 모델이든 연결 가능합니다. Claude, GPT, Gemini 등을 포함합니다.

<video src="https://opencode.ai/_build/assets/opencode-min-CiEsORKQ.mp4" controls="">브라우저가 비디오 태그를 지원하지 않습니다.</video>

### OpenCode란 무엇인가요?

OpenCode는 터미널, IDE, 또는 데스크톱에서 코드를 작성할 수 있도록 도와주는 오픈 소스 에이전트입니다.

- \[\*\]
	**LSP 지원** LLM에 적합한 LSP를 자동으로 로드합니다
- \[\*\]
	**멀티 세션** 동일한 프로젝트에서 여러 에이전트를 병렬로 실행하세요
- \[\*\]
	**링크 공유** 참조나 디버깅을 위해 세션 링크를 공유하세요
- \[\*\]
	**GitHub Copilot** GitHub로 로그인하여 Copilot 계정을 사용하세요
- \[\*\]
	**ChatGPT Plus/Pro** OpenAI로 로그인하여 ChatGPT Plus 또는 Pro 계정을 사용하세요
- \[\*\]
	**모든 모델** Models.dev를 통해 로컬 모델 포함 75개 이상의 LLM 제공자 지원
- \[\*\]
	**모든 에디터** 터미널 인터페이스, 데스크톱 앱, IDE 확장 프로그램으로 사용 가능
[문서 읽기](https://opencode.ai/docs/ko)

### 오픈 소스 AI 코딩 에이전트

\[\*\]

**150,000** 개 이상의 GitHub 스타, **850** 명의 기여자, **11,000** 개 이상의 커밋과 함께, OpenCode는 매달 **6.5M** 명 이상의 개발자가 사용하고 신뢰합니다.

그림 1.**150K** GitHub 스타

그림 2.**850** 기여자

그림 3.**6.5M** 월간 사용자

### 프라이버시를 최우선으로 설계

\[\*\]

OpenCode는 코드나 컨텍스트 데이터를 저장하지 않으므로, 프라이버시에 민감한 환경에서도 안전하게 작동합니다. 더 알아보기: [프라이버시](https://opencode.ai/docs/ko/enterprise/).

### FAQ

- OpenCode는 어떤 AI 모델로든 코드를 작성하고 실행할 수 있도록 도와주는 오픈 소스 에이전트입니다. 터미널 기반 인터페이스, 데스크톱 앱, 또는 IDE 확장 프로그램으로 사용할 수 있습니다.
- 가장 쉬운 시작 방법은 [소개](https://opencode.ai/docs/ko).
- 꼭 그렇지는 않습니다. OpenCode에는 계정 없이도 사용할 수 있는 무료 모델 세트가 포함되어 있습니다. 이 외에도, [Zen](https://opencode.ai/ko/zen) 계정을 생성하여 인기 있는 코딩 모델들을 사용할 수 있습니다. Zen 사용을 권장하지만, OpenCode는 OpenAI, Anthropic, xAI 등 모든 인기 제공자와도 작동합니다. 또한 [로컬 모델](https://opencode.ai/docs/ko/providers/#lm-studio).
- 네, OpenCode는 모든 주요 제공자의 구독 플랜을 지원합니다. Claude Pro/Max, ChatGPT Plus/Pro, 또는 GitHub Copilot 구독을 사용할 수 있습니다. [더 알아보기](https://opencode.ai/docs/ko/providers/#directory).
- 이제 아닙니다! OpenCode는 이제 [데스크톱](https://opencode.ai/ko/download) 및 [웹](https://opencode.ai/docs/ko/web)!
- OpenCode는 100% 무료로 사용할 수 있습니다. 무료 모델 세트도 포함되어 있습니다. 다른 제공자를 연결할 경우 추가 비용이 발생할 수 있습니다.
- 데이터와 정보는 무료 모델을 사용하거나 공유 링크를 생성할 때만 저장됩니다. 더 알아보기: [모델](https://opencode.ai/docs/ko/zen/#privacy) 및 [공유 페이지](https://opencode.ai/docs/ko/share/#privacy).
- 네, OpenCode는 완전히 오픈 소스입니다. 소스 코드는 [GitHub](https://github.com/anomalyco/opencode) 에 공개되어 있으며, [MIT 라이선스](https://github.com/anomalyco/opencode?tab=MIT-1-ov-file#readme) 를 따릅니다. 즉, 누구나 사용, 수정 또는 개발에 기여할 수 있습니다. 커뮤니티의 누구든지 이슈를 등록하고, 풀 리퀘스트를 제출하고, 기능을 확장할 수 있습니다.

### 새로운 제품 출시 소식을 가장 먼저 받아보세요

대기 명단에 등록하여 조기 이용 권한을 받으세요.
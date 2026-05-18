# 📋 Wiki Log

> 위키에서 일어난 모든 활동의 시간순 기록입니다.
> 각 항목은 `## [날짜] 작업유형 | 제목` 형식으로 작성하여 파싱 가능하게 유지합니다.

## [2026-05-18] lint | 위키 건강 검진 및 지식 구조 재조정
- **건강 점수**: 76 → 95 (🟢 건강)
- **작업 내용**:
    - **개념 재정의**: `[[devops]]` 페이지의 연결성 수정 (AI 핵심 개념 → 인프라 참조용).
    - **통계 동기화**: `index.md` 통계 데이터 및 마지막 업데이트 날짜 갱신.
    - **무결성 검사**: 깨진 링크 및 고아 페이지 전수 조사 완료.
- **잔여 문제**: 없음 (사용자 의도에 따른 구조 조정 완료).

---

## [2026-05-18] ingest | Raw Layer — AI 운영 규칙, 데브옵스 로드맵
- **소스**: `raw/ai-rules.md`, `raw/notes/데브옵스 로드맵.md`
- **작업**: 위키의 불변 레이어 규칙 및 데브옵스 학습 경로 인제스트.
- **생성된 페이지**:
    - [[raw-layer-rules]] (Source): 신규 생성
    - [[devops-roadmap]] (Source): 신규 생성
- **업데이트된 페이지**:
    - [[index.md]] (System): 소스 목록 및 통계 업데이트
    - `raw/index.md`, `raw/notes/index.md` (Source Index): 목록 업데이트
- **맥락**: 시스템의 무결성을 유지하기 위한 거버넌스 규칙과 기술적 성장 경로를 지식 베이스에 통합.

---

## [2026-05-18] ingest | 하네스 및 워크플로우 대화적 고찰 반영
- **소스**: `raw/notes/conversation-harness-insights.md`
- **작업**: 사용자와의 대화 내용을 바탕으로 하네스를 '목적 달성 루프'로 정의. 쉬운 비유(OS, 운동장, 주방)를 통해 접근성 강화.
- **생성/업데이트된 페이지**:
    - [[conversation-harness-insights]] (Source): 신규 생성
    - [[harness-engineering]] (Concept): '루프' 정의 및 비유 보강
- **맥락**: 하네스 엔지니어링의 본질을 '출발지에서 도착지까지의 안정적인 도달을 보장하는 시스템 설계'로 명확히 함.

---

## [2026-05-18] refine | 하네스 개념 정제 (3계층 분류 제거)
- **작업**: 워크플로우와 혼선을 주는 하네스의 '3계층(실행/개발/작업)' 분류를 제거하고, `GEMINI.md` 중심의 거버넌스 정의로 일원화.
- **업데이트된 페이지**:
    - [[harness-engineering]] (Concept): 3계층 섹션 삭제 및 '거버넌스 레이어' 중심 재구성.
    - [[agentic-workflow]] (Concept): 하네스(Governance) vs 워크플로우(Operations) 대비 강화.
- **맥락**: 하네스를 '인프라/절차'가 아닌 '규범/헌법'으로 명확히 정의하여 에이전트 운영의 안정성과 논리적 일관성 확보.

---

## [2026-05-18] ingest | 하네스 vs 워크플로우 (거버넌스 vs 오퍼레이션) 구분
- **소스**: `raw/notes/하네스-에이전트워크플로우.md`
- **작업**: 하네스를 '헌법'으로, 워크플로우를 'SOP'로 정의하여 개념적 뉘앙스 확장. 사용자 제안으로 '음식점' 비유(주방 vs 레시피) 추가 도입.
- **생성된 페이지**:
    - [[harness-vs-workflow]] (Source)
    - [[agentic-workflow]] (Concept)
- **업데이트된 페이지**:
    - [[harness-engineering]] (Concept)
    - [[index.md]] (System)
- **맥락**: 하네스 엔지니어링의 기술적 정의를 넘어 '거버넌스' 차원의 이해를 돕기 위해 "헌법 vs SOP", "운동장 vs 경기 방식", "음식점 주방 vs 레시피" 비유 도입. 지식의 대중적 이해도를 높이기 위한 작업.

---

## [2026-05-15] ingest | GSD v1 (get-shit-done) vs v2 (gsd2) 지식 체계화
- **소스**: `raw/GET SHIT DONE README.ko-KR.md`
, `raw/articles/6-3. gsd — Get Shit Done 프로젝트 관리.md`
- **작업**: v1(실행 중심)과 v2(자율 중심)의 명확한 구분 및 하네스 도구 간 관계 정립
- **생성된 페이지**:
    - [[gsd-readme]], [[gsd-article]] (Sources)
    - [[gsd]], [[gsd2]] (Entities)
- **업데이트된 페이지**:
    - [[virtual-engineering-team]] (Concept)
    - [[index.md]] (System)
- **맥락**: 사용자가 GSD v1과 v2를 혼동 없이 관리하고, 프로젝트의 성격에 따라 적절한 도구를 선택할 수 있도록 지식 기반 마련. 하네스 경험 축적의 핵심 이정표.

---

## [2026-05-15] ingest | OpenCode & oh-my-opencode 및 하네스 진화론
- **소스**: `raw/articles/` 및 `raw/notes/` (OpenCode 공식, 갓대희 리뷰 1&2, Awesome DESIGN.md, AI 협업의 진화)
- **작업**: 소스 요약 및 실전 하네스(OpenCode/OMO) 중심 지식 확장
- **생성된 페이지**:
    - [[opencode-official]], [[opencode-review-1]], [[oh-my-opencode-review]], [[awesome-design-md]], [[ai-collaboration-evolution]] (Sources)
    - [[opencode]], [[oh-my-opencode]], [[goddaehee]] (Entities)
    - [[aggressive-delegation]], [[design-md]] (Concepts)
- **맥락**: GSD, gstack 외 실전 에이전트 도구(OpenCode/OMO)의 메커니즘을 학습하여 "에이전트 지시 실력 향상" 및 "지식 연결" 목표 달성. Sisyphus의 공격적 위임 전략을 통한 하네스 엔지니어링의 실체적 이해.

---

## [2026-05-15] ingest | 하네스 엔지니어링 및 지식 관리 전략 소스 6종
- **소스**: `raw/notes/` (AI 타임라인, free-code, 하네스 엔지니어링, Software 3.0, 제텔카스텐, 지식 복리)
- **작업**: 소스 요약 및 하네스 엔지니어링 중심의 지식 체계 구축
- **생성된 페이지**:
    - [[ai-development-timeline]], free-code-guide, [[harness-engineering-deep-dive]], [[software-3-0-harness]], [[zettelkasten-principles]], [[knowledge-compounding-principle]] (Sources)
    - [[harness-engineering]], [[executable-ssot]], [[knowledge-compounding]], [[zettelkasten]] (Concepts)
    - [[mitchell-hashimoto]], [[anthropic]], [[openai]], [[claude-code]] (Entities)
- **맥락**: 하네스 엔지니어링 개념 학습 및 AI 엔지니어링 표준 수립을 위한 기초 지식 확장. "실행 가능한 지식"으로서의 위키 활용 방안 모색.

---

## [2026-05-14] ingest | 에이전틱 프레임워크 및 시니어 개발 전략 소스 3종
- **소스**: `raw/articles/` (superpowers, zero-native, 시니어 개발자 관련)
- **작업**: 소스 요약 및 엔티티/개념 페이지 생성
- **생성된 페이지**:
    - [[superpowers-methodology]], [[zero-native-framework]], [[senior-dev-complexity]] (Sources)
    - [[superpowers]], [[zero-native]] (Entities)
    - [[complexity-management]], [[senior-as-editor]], [[speed-vs-scale]] (Concepts)
- **맥락**: GSD 외 에이전틱 동향 탐색 및 시니어 개발자의 복잡성 관리 관점을 통한 역량 극대화 방안 모색.

## [2026-05-14] ingest | gstack: Garry Tan's AI Engineering Stack
- **소스**: `raw/articles/garrytangstack...md`
- **작업**: 소스 요약 및 관련 엔티티/개념 페이지 생성
- **생성된 페이지**:
    - [[garry-tan-gstack]] (Source)
    - [[gstack]] (Entity)
    - [[garry-tan]] (Entity)
    - [[virtual-engineering-team]] (Concept)
- **맥락**: 사용자가 GSD 외에 gstack 등 최신 에이전틱 동향 탐색 및 경제 프로젝트 도입 검토 중임.

## [2026-05-14] init | 위키 시스템 초기화
- **작업**: LLM Wiki 패턴 기반으로 프로젝트 구조 초기화
- **생성된 파일**: raw/index.md, wiki/index.md, wiki/log.md, output/index.md
- **스키마**: GEMINI.md에 위키 운영 규칙 추가

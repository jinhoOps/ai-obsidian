# 🏛️ AI Obsidian Knowledge Base Rulebook

## 🎯 핵심 목표
- 이 저장소는 오직 AI 에이전트의 관점에서 지식을 수집, 정리, 인덱싱하는 '에이전트 중심의 지식 허브'입니다.
- 불필요한 서술을 배제하고, 에이전트가 읽고 활용하기 가장 최적화된 구조(Raw -> Wiki -> Output)를 유지합니다.

## 📂 폴더 구조 및 역할
- `content/raw/`: 외부에서 유입되는 가공되지 않은 정보(스크랩, 뉴스레터, 파일 등) (배포 제외).
- `content/raw/archive/`: 처리가 완료된 원본 데이터의 보관소.
- `content/wiki/`: 가공 및 연결이 완료된 정제된 지식 (웹 배포 대상).
- `content/output/`: 에이전트가 생산한 최종 결과물(보고서, 설계서 등) (배포 제외).

## 🛠️ 핵심 운영 명령어 (Core Commands)

에이전트는 다음 네 가지 핵심 명령을 통해 지식 베이스를 관리합니다. 모든 작업 결과는 `content/log.md`에 기록됩니다.

### 1. Compile (컴파일)
- **목적**: `content/raw/` 폴더의 신규 정보를 분석하여 `content/wiki/`에 정제된 노트로 반영.
- **절차**: 
  1. `content/raw/` 파일 읽기 및 독립적이고 단일한 주제 단위(원자성)로 핵심 개념 분리 및 추출.
  2. `content/wiki/`에 새로운 요약/엔티티 페이지 생성 또는 기존 페이지 업데이트.
  3. 관련 노트 간 위키 링크(`[[...]]`) 삽입.
  4. `content/index.md` 및 `content/log.md` 업데이트.
  5. 처리가 완료된 원본은 `content/raw/archive/`로 이동.

### 2. Query (쿼리)
- **목적**: 사용자의 질문에 대해 지식 베이스를 바탕으로 종합적인 답변 제공.
- **절차**:
  1. `content/index.md` 및 관련 `content/wiki/` 노드를 우선 탐색.
  2. 출처(Citation)를 포함한 답변 생성.
  3. 필요시 새로운 합성 지식을 `content/wiki/` 노드로 저장.

### 3. Lint (린트)
- **목적**: 지식 베이스의 무결성 및 연결성 유지.
- **절차**:
  1. 고립된 노드(Orphan pages) 식별 및 연결.
  2. 누락된 교차 참조(Cross-references) 추가.
  3. 정보 간의 논리적 모순이나 오래된 주장 확인 및 수정 제안.
  4. 특정 주제로 군집화된 노드 발견 시 중간 인덱스(MOC - Map of Content) 허브 노드 자동 생성.

### 4. Audit (감사)
- **목적**: 헌법(Rulebook)과 에이전트 시스템 간의 정합성 유지 및 시스템 병목 진단.
- **절차**:
  1. 현재 지식베이스 구조 및 워크플로우가 헌법(GEMINI.md)의 철학(원자성, 연결성 등)에 부합하는지 점검.
  2. 발견된 문제점, 보안 취약성, 최적화 가능성(룰의 간소화 등)을 진단하여 피드백.
  3. 감사 결과 및 아키텍처 개선 제안 등 구체적인 산출물(리포트)이 발생할 경우, 이를 `content/output/` 폴더에 저장하여 시스템 발전 이력으로 보존.

### 5. Publish (배포)
- **목적**: Zettelkasten 시스템에 구축된 지식을 GitHub Pages 기반웹사이트(Quartz)로 발행.
- **절차**:
  1. 퍼블릭으로 공개할 노트의 프론트매터(Frontmatter) 검증 (`status: budding` 노트나 민감정보 포함 여부 확인, 해당 파일은 자동 필터링됨).
  2. 노트를 작성/수정 후 Git 커밋 및 `main` 브랜치로 푸시(`git push`).
  3. 푸시가 완료되면 GitHub Actions의 `Deploy Quartz site` CI/CD 파이프라인이 백그라운드에서 빌드 후 `https://jinhoops.github.io/ai-obsidian`로 자동 라이브 배포를 진행.

## 📜 에이전트 행동 지침 (Agent Guidelines)
- **인코딩 (Encoding)**: 모든 파일 작성 및 읽기 시 반드시 `UTF-8` 인코딩을 사용합니다.
- **언어 (Language)**: 사용자와의 모든 소통 및 `content/wiki/` 내 문서 작성은 **한국어**를 기본으로 합니다. 전문 용어의 경우 의미 전달을 위해 영문을 병기할 수 있습니다.

## ⚙️ 컴파일 프로세스 (The Compile Workflow)
- `Compile` 명령의 기술적 구현 세부사항입니다.
- **명령어**: `compile`
1. **Analyze (분석)**: `content/raw/` 폴더 내의 신규 및 변경된 파일을 스캔.
2. **Filter (필터링)**: 이미 반영된 파일 제외.
3. **Refine (정제)**: `content/wiki/` 하위 토픽 정리 및 인덱스 업데이트.
4. **Archive & Track (보관 및 추적)**: 완료된 파일 이동 및 상태 추적.
5. **Index (인덱스 갱신)**: `content/index.md` 최신화.

---
*이 문서는 에이전트의 운영 헌법입니다. 시스템은 이 지침에 따라 자동으로 작업을 수행합니다.*

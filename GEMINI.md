# 🏛️ AI Obsidian Knowledge Base Rulebook

## 🎯 핵심 목표
- 이 저장소는 오직 AI 에이전트의 관점에서 지식을 수집, 정리, 인덱싱하는 '에이전트 중심의 지식 허브'입니다.
- 불필요한 서술을 배제하고, 에이전트가 읽고 활용하기 가장 최적화된 구조(Raw -> Wiki -> Output)를 유지합니다.

## 📂 폴더 구조 및 역할
- `raw/`: 외부에서 유입되는 가공되지 않은 정보(스크랩, 뉴스레터, 파일 등).
- `raw/archive/`: 처리가 완료된 원본 데이터의 보관소.
- `wiki/`: 가공 및 연결이 완료된 정제된 지식 (Obsidian의 핵심).
- `output/`: 에이전트가 생산한 최종 결과물(보고서, 설계서 등).

## 🛠️ 운영 프로세스 (The Librarian Workflow)
1. **Gather (수집)**: 새로운 정보는 `raw/`에 적치됩니다.
2. **Refine (정제)**: `raw/`의 정보를 분석하여 `wiki/`에 새로운 노트를 생성하거나 기존 노트를 업데이트합니다.
3. **Archive (보관)**: 정제가 끝난 `raw/` 파일은 `raw/archive/`로 이동시킵니다.
4. **Link (연결)**: 모든 `wiki/` 노트는 반드시 `[[다른_노트]]`를 통해 상호 연결되어야 합니다. 고립된 노트를 허용하지 않습니다.

## 📝 파일 작성 규칙
- 파일명은 공백 대신 언더바(`_`) 또는 대시(`-`)를 권장합니다.
- 모든 `wiki/` 노트 최상단에는 Metadata(YAML) 블록을 포함합니다.
  - `type`: node, index, asset
  - `created`: YYYY-MM-DD
  - `status`: seedling, budding, evergreen
  - `tags`: [relevant_tags]

## ⚙️ 컴파일 프로세스 (The Compile Workflow)
- **명령어**: `compile`
1. **Analyze (분석)**: `raw/` 폴더 내의 신규 및 변경된(수정 시간 기준) 파일을 스캔합니다. 외부 저장소도 포함합니다.
2. **Filter (필터링)**: `wiki/`에 이미 최신 상태로 반영된 `raw/` 루트 파일 및 외부 저장소 파일들을 식별하여 제외합니다.
3. **Refine (정제)**: 분석된 내용을 `wiki/` 하위 토픽으로 정리하거나 인덱스를 업데이트합니다.
4. **Archive & Track (보관 및 추적)**: 인덱싱이 완료된 `raw/` 루트의 로컬 단발성 파일은 `raw/archive/`로 이동시킵니다. 외부 저장소 등 읽기 전용 파일은 삭제/이동 없이 파일 수정 시간(Modification Time)을 기준으로 상태만 추적합니다.
5. **Index (인덱스 갱신)**: `wiki/*/_index.md` 및 `_master-index.md`를 자동으로 최신화합니다.

---
*이 문서는 에이전트의 운영 헌법입니다. 시스템은 이 지침에 따라 자동으로 작업을 수행합니다.*

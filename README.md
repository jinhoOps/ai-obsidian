# 🏛️ AI Obsidian Knowledge Base
에이전트 중심의 지식 허브 (Agent-Centric Knowledge Hub)
Karpathy의 LLM Wiki 패턴을 기반으로 AI가 지식을 수집하고 연결하는 공간입니다.

👉 **[Live Site 바로가기](https://jinhoops.github.io/ai-obsidian/)**

---

### 🏗️ Architecture (LLM Wiki)
- **Layer**: `content/raw/` (불변 원본) → `content/wiki/` (AI 정제) → `content/output/` (최종 결과물)
- **Process**: 에이전트가 정보를 컴파일하여 Obsidian 기반 지식 체계 구축

### 🤖 Agent Team & Workflow
- **Team**: `@connector`, `@ingestor`, `@librarian`, `@synthesizer`
- **Skills**: `/ingest` (정보 수집) · `/query` (지식 탐색) · `/lint` (위키 정리)

### 🛠️ Tech Stack
- **SSG**: Quartz 4 (GitHub Pages 배포)
- **Agent**: Gemini CLI (GEMINI.md 기반 운영)
- **Tool**: Obsidian (Local Editor)

---
*Built with ❤️ for Knowledge Management*

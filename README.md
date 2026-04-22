# 🏛️ AI Obsidian Knowledge Base

> **에이전트 중심의 지식 허브 (Agent-Centric Knowledge Hub)**  
> 외부의 정보를 수집하고 정제하여 나만의 지식 체계(Zettelkasten)로 구축하는 공간입니다.

---

## 🚀 Live Site
공개된 지식 베이스를 확인해 보세요:  
👉 **[https://jinhoops.github.io/ai-obsidian/](https://jinhoops.github.io/ai-obsidian/)**

## 📂 저장소 구조
- **`content/wiki/`**: 정제된 지식 노트 (핵심)
- **`content/raw/`**: 가공 전의 원시 데이터 보관소
- **`content/output/`**: 에이전트가 생산한 최종 결과물
- **`GEMINI.md`**: 지식 베이스 운영을 위한 AI 에이전트 규칙 (헌법)

## 🛠️ 운영 안내
이 저장소는 **Quartz 4** 프레임워크를 기반으로 하며, 다음과 같은 흐름으로 관리됩니다.

1. **수집**: `content/raw/`에 정보 저장.
2. **가공**: AI 에이전트가 `GEMINI.md` 지침에 따라 `wiki/` 노드로 컴파일.
3. **배포**: GitHub Actions를 통해 `main` 브랜치 푸시 시 자동 배포.

---
*Built with ❤️ and [Quartz 4](https://quartz.jzhao.xyz/)*

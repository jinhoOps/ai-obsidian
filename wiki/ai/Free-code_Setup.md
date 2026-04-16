---
type: node
created: 2026-04-16
status: budding
tags: [ai, claude-code, free-code, codex, multi-provider, cli]
---

# 🚀 free-code 설치 및 사용 가이드

`free-code`는 Anthropic의 **Claude Code CLI**를 기반으로 한 오픈소스 포크 프로젝트로, OpenAI Codex, AWS Bedrock, Google Vertex AI 등 다양한 모델 프로바이더를 지원하고 실험적 기능을 활성화한 도구입니다.

## 🌟 주요 특징
- **멀티 프로바이더**: Anthropic 외에도 OpenAI Codex, AWS Bedrock, Google Vertex AI 지원.
- **실험적 기능 해제**: 공식 버전에서 제한된 36개의 실험적 기능을 번들로 포함.
- **Telemetry 제거**: 사용자 데이터 수집 및 가드레일을 최소화한 실험 환경 제공.

## 🛠️ 설치 방법 (macOS/Linux)

### 1. One-liner 설치
가장 빠른 설치 방법은 공식 저장소의 설치 스크립트를 실행하는 것입니다.
```bash
curl -fsSL https://raw.githubusercontent.com/paoloanzn/free-code/main/install.sh | bash
```

### 2. macOS 26 (Tahoe) 트러블슈팅
macOS 26 환경에서 컴파일된 바이너리가 즉시 종료(SIGKILL)되는 경우, 소스 모드 래퍼로 교체하여 해결할 수 있습니다.
```bash
cat > ~/.local/bin/free-code << 'EOF'
#!/bin/zsh
cd ~/free-code && exec bun run ./src/entrypoints/cli.tsx "$@"
EOF
chmod +x ~/.local/bin/free-code
```

## 🔑 인증 및 프로바이더 설정

사용할 프로바이더에 따라 환경변수를 설정한 후 로그인을 진행해야 합니다.

| 프로바이더 | 환경변수 | 로그인 명령어 |
| :--- | :--- | :--- |
| **OpenAI Codex** | `export CLAUDE_CODE_USE_OPENAI=1` | `free-code /login` |
| **AWS Bedrock** | `export CLAUDE_CODE_USE_BEDROCK=1` | AWS CLI 인증 활용 |
| **Google Vertex** | `export CLAUDE_CODE_USE_VERTEX=1` | gcloud ADC 활용 |

## 💡 사용 팁
- **모델 지정**: `free-code --model gpt-5.3-codex`와 같이 특정 모델을 명시하여 실행 가능.
- **로컬 백업**: 저장소 접근이 제한될 가능성을 대비해 `git clone` 후 로컬에 백업해 두는 것이 안전합니다.

---
**관련 노트:**
- [[wiki/ai/Harness_Engineering|하네스 엔지니어링]]
- [[wiki/ai/_index|AI 지식 인덱스]]

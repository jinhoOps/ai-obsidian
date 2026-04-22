---
type: node
created: 2026-04-22
status: budding
tags: [security, kisa, supply-chain, trivy, malware]
---

# ☣️ 개발도구 공급망 연쇄 사이버 공격 (Supply Chain Diffusion Attack)

오픈소스 보안 스캐너(Trivy)의 공급망 침해를 시작으로 다양한 소프트웨어 생태계로 악성코드가 확산된 사례입니다. (2026년 4월 권고)

## 📌 개요
- **CVE ID**: CVE-2026-33634 (CVSS 9.4, Critical)
- **주요 대상**: Trivy(바이너리, Action, Docker), npm 패키지(64+개), PyPI(litellm, telnyx), VS Code 확장 등.
- **감염 트리거**: CI/CD 파이프라인에서 취약한 Trivy 실행 시 자격증명(Token, SSH key 등) 탈취.

## ⚙️ 공격 흐름 (Diffuison Attack)
1. **1단계**: Trivy 공급망 침해를 통한 악성 버전 유포 및 CI/CD 자격증명 탈취.
2. **2단계**: 탈취된 토큰을 활용한 npm(CanisterWorm), PyPI 등 타 생태계 연쇄 감염.
3. **3단계**: 감염 시스템에 `pgmon` 또는 `sysmon` 백도어 설치 후 C2 통신.

## 🛠️ 대응 방안
- **버전 확인**: Trivy v0.69.4, litellm 1.82.7~8, telnyx 4.87.1~2 등 영향받는 버전 사용 중지.
- **자격증명 재발급**: 감염 의심 시 npm, PyPI, GitHub 토큰, SSH 키 등 즉시 변경.
- **호스트 점검**: `~/.local/share/pgmon/`, `~/.config/sysmon/` 경로의 백도어 파일 확인.

## 🔗 연결된 지식
- [[wiki/security/KISA_Security_Notices_Index|KISA 보안 공지 인덱스]]

---
[[index|🏠 마스터 인덱스로 돌아가기]]

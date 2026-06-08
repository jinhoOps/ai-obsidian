## gstack + gsd + superpowers 함께 사용하기

세 도구는 각자의 역할이 명확히 구분됩니다.

```bash
gstack      → "무엇을 왜 만드나" (전략·검증)
  /cso, /qa, /ship, /review

gsd         → "어떤 순서로 만드나" (구조·실행)
  /gsd-plan-phase, /gsd-execute-phase, /gsd-validate-phase

superpowers → "어떻게 잘 만드나" (방법론·품질)
  TDD, 체계적 디버깅, 코드 리뷰 프로토콜
```

실전 파이프라인:

```bash
비전 수립:   /cso  (gstack)
계획 수립:   /gsd-plan-phase  (gsd)
구현:        /gsd-execute-phase + superpowers:test-driven-development
검증:        /gsd-verify-work + /qa  (gstack)
완료:        /gsd-complete-milestone + /ship  (gstack)
```

단순한 AI 대화를 넘어, 실제 소프트웨어 팀이 사용하는 수준의 프로젝트 관리가 Claude Code 안에서 가능해집니다.

---

## 파일 시스템 구조

gsd는 프로젝트 루트의 `.planning/` 디렉토리에 모든 상태를 저장합니다.

```bash
.planning/
  ├── ROADMAP.md          # 전체 로드맵
  ├── milestones/
  │   ├── M1/
  │   │   ├── MILESTONE.md    # 마일스톤 정의
  │   │   ├── phase-1/
  │   │   │   ├── PLAN.md     # 페이즈 계획서
  │   │   │   └── VERIFICATION.md  # 검증 결과
  │   │   └── phase-2/
  │   └── M2/
  └── research/           # 기술 조사 결과
```

이 구조 덕분에 Git으로 프로젝트 계획 자체도 버전 관리할 수 있습니다.

마지막 편집일시: 2026년 5월 13일 2:31 오전

댓글 0 [피드백](#myModal "피드백을 남겨주세요")
---
type: node
created: 2026-04-16
status: budding
tags: [git, github, collaboration, setup]
---

# 🌐 Git 로컬 및 원격 저장소 관리 가이드

이 문서는 프로젝트 초기화 과정에서 수행된 Git 설정 작업과 로컬(Local) 및 원격(Remote) 저장소의 관계를 설명합니다.

## 1. 최근 작업 요약 (2026-04-16)
기존에 잘못 생성된 Git 이력을 완전히 제거하고, 신규 생성한 GitHub 레포지토리에 맞춰 클린 설치(Clean Setup)를 진행했습니다.

- **작업 내용**: `.git` 폴더 강제 삭제 후 `git init` 재수행
- **브랜치 전략**: 기본 브랜치를 `master`에서 `main`으로 변경
- **최종 상태**: 로컬 파일 전량을 [jinhoOps/ai-obsidian](https://github.com/jinhoOps/ai-obsidian) 원격 저장소로 푸시 완료

## 2. Git 저장소 구조와 관계

### 🏗️ 로컬 저장소 (Local Repository)
사용자의 컴퓨터(PC)에 존재하는 저장소입니다. `.git` 폴더가 이 역할을 수행합니다.
- **Working Directory**: 실제 파일들이 있는 공간.
- **Staging Area (Index)**: 커밋하기 전 파일들을 모아두는 장바구니. (`git add`)
- **Local Repo**: 커밋된 파일들이 저장되는 실제 로컬 DB. (`git commit`)

### ☁️ 원격 저장소 (Remote Repository)
GitHub와 같은 서버에 존재하는 저장소입니다. 협업 및 백업의 중심이 됩니다.
- **Origin**: 원격 저장소를 가리키는 기본 별칭(Alias).

### 🔗 연결 고리 (The Link)
- `git remote add origin [URL]`: 로컬 저장소에게 "너의 원격 짝꿍은 여기야"라고 알려주는 과정입니다.
- `git push`: 로컬의 커밋 이력을 원격 저장소로 밀어 넣어 동기화합니다.

## 3. 핵심 명령어 흐름도

```powershell
# 1. 초기화 및 브랜치 설정
git init              # 로컬 저장소 생성
git branch -M main    # 기본 브랜치명을 main으로 고정

# 2. 파일 저장 (Snapshot)
git add .             # 모든 변경사항을 장바구니에 담기
git commit -m "msg"   # 로컬 DB에 영구 저장

# 3. 원격 연결 및 전송
git remote add origin https://github.com/jinhoOps/ai-obsidian.git
git push -u origin main  # -u 옵션은 이후 'git push'만 입력해도 main으로 가도록 설정
```

## 4. 관리 팁
- **동기화**: 작업 시작 전에는 `git pull`을 통해 원격의 최신 상태를 로컬로 가져오는 습관이 중요합니다.
- **상태 확인**: `git status`와 `git log`를 통해 현재 내가 어디에 있는지 자주 확인하세요.

---
[[index|🏠 마스터 인덱스로 돌아가기]]

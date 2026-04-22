---
type: node
created: 2026-04-13
status: evergreen
tags: [windows, windows-11, context-menu, antigravity, powershell]
---

# 🪟 Windows Context Menu: Open with Antigravity

이 문서는 Windows 11에서 Antigravity 에디터를 마우스 오른쪽 버튼 메뉴(컨텍스트 메뉴)에 등록하는 방법을 설명합니다. VS Code의 "폴더로 열기"와 같은 기능을 Antigravity에서도 구현할 수 있습니다.

## 🛠️ 해결 방법: PowerShell 자동화 스크립트

아래 코드는 현재 로그인한 사용자 계정(`HKEY_CURRENT_USER`, `HKCU`)을 기준으로 레지스트리를 수정하므로 관리자 권한 없이 실행 가능합니다.

### 📋 PowerShell 스크립트
```powershell
# 1. 변수 설정 (설치 경로 및 메뉴 이름)
$EXE_PATH = "$ENV:LOCALAPPDATA\Programs\Antigravity\Antigravity.exe"
$MENU_NAME = "Antigravity로 열기"

# 설치 파일 존재 여부 확인
if (-not (Test-Path $EXE_PATH)) {
    Write-Host "오류: $EXE_PATH 경로에서 실행 파일을 찾을 수 없습니다." -ForegroundColor Red
    return
}

# 2. 레지스트리 경로 설정
$REG_SHELL = "HKCU:\Software\Classes\Directory\shell\Antigravity"
$REG_BG = "HKCU:\Software\Classes\Directory\Background\shell\Antigravity"

# 3. 폴더 자체 우클릭 메뉴 등록
if (-not (Test-Path $REG_SHELL)) { New-Item -Path $REG_SHELL -Force }
Set-Item -Path $REG_SHELL -Value $MENU_NAME
Set-ItemProperty -Path $REG_SHELL -Name "Icon" -Value "\`"$EXE_PATH\`""

$COMMAND_PATH = Join-Path $REG_SHELL "command"
if (-not (Test-Path $COMMAND_PATH)) { New-Item -Path $COMMAND_PATH -Force }
Set-Item -Path $COMMAND_PATH -Value "\`"$EXE_PATH\`" \`"%1\`""

# 4. 폴더 내부 빈 공간 우클릭 메뉴 등록
if (-not (Test-Path $REG_BG)) { New-Item -Path $REG_BG -Force }
Set-Item -Path $REG_BG -Value $MENU_NAME
Set-ItemProperty -Path $REG_BG -Name "Icon" -Value "\`"$EXE_PATH\`""

$BG_COMMAND_PATH = Join-Path $REG_BG "command"
if (-not (Test-Path $BG_COMMAND_PATH)) { New-Item -Path $BG_COMMAND_PATH -Force }
Set-Item -Path $BG_COMMAND_PATH -Value "\`"$EXE_PATH\`" \`"%V\`""

Write-Host "성공: Antigravity 우클릭 메뉴가 등록되었습니다." -ForegroundColor Cyan
```

## ✅ 적용 결과 확인
1. 폴더를 선택하고 우클릭합니다.
2. 윈도우 11 기본 메뉴에서 바로 보이지 않는다면 **Shift + 우클릭**을 하거나 [추가 옵션 표시]를 클릭합니다.
3. 목록에 생성된 **[Antigravity로 열기]**를 클릭하면 해당 폴더가 즉시 열립니다.

---
**관련 노트:**
- [[wiki/windows/_index|Windows 설정 인덱스]]
- [[index|마스터 인덱스]]

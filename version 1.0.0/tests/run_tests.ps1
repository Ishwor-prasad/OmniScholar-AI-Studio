Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "  Running OmniScholar Quality Verification Suite" -ForegroundColor Green
Write-Host "======================================================================" -ForegroundColor Cyan

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

$pythonExe = Join-Path $scriptDir "..\..\.venv\Scripts\python.exe"
if (-not (Test-Path $pythonExe)) {
    $pythonExe = "python"
}

& $pythonExe comprehensive_verifier.py

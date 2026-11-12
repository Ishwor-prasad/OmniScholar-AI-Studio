Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  Starting OmniScholar - Scientific Research Studio v1.0.0" -ForegroundColor Green
Write-Host "  Live URL: http://127.0.0.1:8000" -ForegroundColor White
Write-Host "========================================================" -ForegroundColor Cyan

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

$pythonExe = Join-Path $scriptDir "..\..\.venv\Scripts\python.exe"
if (-not (Test-Path $pythonExe)) {
    $pythonExe = "python"
}

& $pythonExe server.py

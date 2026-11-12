Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "  Starting OmniScholar - Autonomous Empirical Research Studio" -ForegroundColor Green
Write-Host "  Founder: Ishwor Prasad Dhungana" -ForegroundColor Yellow
Write-Host "  Live URL: http://127.0.0.1:8000" -ForegroundColor White
Write-Host "======================================================================" -ForegroundColor Cyan

$appDir = Join-Path $PSScriptRoot "version 1.0.0\app"
$pythonExe = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"

if (-not (Test-Path $pythonExe)) {
    $pythonExe = "python"
}

Set-Location $appDir
& $pythonExe server.py

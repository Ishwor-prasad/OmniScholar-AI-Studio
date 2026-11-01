Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  Starting Project OmniScholar - Research AI Studio v1.0.0" -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Cyan
Set-Location $PSScriptRoot
uv run --with fastapi --with uvicorn --with python-multipart --with pandas --with scipy --with matplotlib --with seaborn --with openpyxl python server.py

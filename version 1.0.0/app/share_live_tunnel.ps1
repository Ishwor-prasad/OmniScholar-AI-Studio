Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  Launching OmniScholar Public Shareable Tunnel" -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Cyan
& "C:\Program Files (x86)\cloudflared\cloudflared.exe" tunnel --url http://127.0.0.1:8000

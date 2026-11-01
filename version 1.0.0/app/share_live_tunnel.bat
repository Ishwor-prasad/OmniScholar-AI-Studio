@echo off
echo ========================================================
echo   Launching OmniScholar Public Shareable Tunnel
echo ========================================================
"C:\Program Files (x86)\cloudflared\cloudflared.exe" tunnel --url http://127.0.0.1:8000
pause


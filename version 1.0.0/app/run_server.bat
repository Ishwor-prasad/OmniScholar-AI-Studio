@echo off
title OmniScholar - Scientific Research Studio v1.0.0
echo ========================================================
echo   Starting OmniScholar - Scientific Research Studio v1.0.0
echo   Live URL: http://127.0.0.1:8000
echo ========================================================
cd /d "%~dp0"
if exist "..\..\.venv\Scripts\python.exe" (
    "..\..\.venv\Scripts\python.exe" server.py
) else (
    python server.py
)
pause

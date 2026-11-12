@echo off
title OmniScholar - Autonomous Empirical Research Studio v1.0.0
echo ======================================================================
echo   Starting OmniScholar - Autonomous Empirical Research Studio
echo   Founder: Ishwor Prasad Dhungana
echo   URL: http://127.0.0.1:8000
echo ======================================================================
cd /d "%~dp0\version 1.0.0\app"
if exist "%~dp0\.venv\Scripts\python.exe" (
    "%~dp0\.venv\Scripts\python.exe" server.py
) else (
    python server.py
)
pause

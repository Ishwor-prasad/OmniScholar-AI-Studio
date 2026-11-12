@echo off
title OmniScholar - Test Suite Runner
echo ======================================================================
echo   Running OmniScholar Quality Verification Suite
echo ======================================================================
cd /d "%~dp0"
if exist "..\..\.venv\Scripts\python.exe" (
    "..\..\.venv\Scripts\python.exe" comprehensive_verifier.py
) else (
    python comprehensive_verifier.py
)
pause

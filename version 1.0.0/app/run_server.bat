@echo off
echo ========================================================
echo   Starting Project OmniScholar - Research AI Studio v1.0.0
echo ========================================================
cd /d "%~dp0"
uv run --with fastapi --with uvicorn --with python-multipart --with pandas --with scipy --with matplotlib --with seaborn --with openpyxl python server.py
pause

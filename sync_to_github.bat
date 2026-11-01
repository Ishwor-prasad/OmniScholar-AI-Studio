@echo off
cd /d "%~dp0"
echo Syncing OmniScholar to GitHub...
git add .
git status --porcelain > "%temp%\git_status.tmp"
for %%R in ("%temp%\git_status.tmp") do if %%~zR gtr 0 (
    git commit -m "Auto-update: %date% %time%"
    git push origin main
    echo Successfully synced to GitHub!
) else (
    echo No changes detected to push.
)
del "%temp%\git_status.tmp"
pause


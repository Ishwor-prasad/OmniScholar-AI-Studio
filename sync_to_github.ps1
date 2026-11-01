Write-Host "Syncing OmniScholar to GitHub..." -ForegroundColor Cyan
Set-Location $PSScriptRoot
git add .
$status = git status --porcelain
if ($status) {
    $timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    $msg = if ($args.Count -gt 0) { $args -join " " } else { "Auto-update: $timestamp" }
    git commit -m "$msg"
    git push origin main
    Write-Host "Successfully pushed updates to GitHub!" -ForegroundColor Green
} else {
    Write-Host "Working directory clean; no changes to commit." -ForegroundColor Yellow
}


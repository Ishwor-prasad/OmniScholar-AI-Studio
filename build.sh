#!/usr/bin/env bash
# ==============================================================================
# OmniScholar CI/CD Cloud Build Script (Render / Linux)
# ==============================================================================
set -o errexit

echo "=========================================="
echo "  OmniScholar Cloud Build Pipeline"
echo "=========================================="

echo "[1/3] Upgrading pip and installing Python dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "[2/3] Setting up native Linux Typst compiler (v0.12.0)..."
mkdir -p ./bin

if [ ! -f "./bin/typst" ]; then
    echo "Downloading Typst binary release from GitHub..."
    curl -fsSL https://github.com/typst/typst/releases/download/v0.12.0/typst-x86_64-unknown-linux-musl.tar.xz | tar -xJ
    cp typst-*/typst ./bin/typst
    chmod +x ./bin/typst
    rm -rf typst-*
fi

echo "[3/3] Verifying Typst compiler..."
./bin/typst --version

echo "=========================================="
echo "  Build Completed Successfully!"
echo "=========================================="


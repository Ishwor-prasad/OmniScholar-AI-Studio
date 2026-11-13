"""
OmniScholar Root Production Entrypoint
Seamlessly bridges version 1.0.0/app/server.py for 24/7 Cloud Deployments (Render, Cloud Run, Docker).
"""
import os
import sys
from pathlib import Path

# Add version 1.0.0/app to sys.path
APP_DIR = Path(__file__).resolve().parent / "version 1.0.0" / "app"
sys.path.insert(0, str(APP_DIR))
os.chdir(str(APP_DIR))

from server import app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    print(f"[OmniScholar Production Engine] Listening on http://0.0.0.0:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port)

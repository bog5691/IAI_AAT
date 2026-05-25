# ============================================================
# api/index.py — Vercel Entry Point
# Vercel needs the Flask app in an 'api' folder.
# This file imports the app from the parent directory.
# ============================================================

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
# Add the parent directory to Python's path so we can import app.py
# Vercel runs this file from inside the /api folder,
# so without this line it can't find app.py in the parent folder.

from app import app
# Import the Flask app object from app.py.
# Vercel automatically detects and serves this 'app' variable.

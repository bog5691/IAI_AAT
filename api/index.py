import sys
import os

# Get the directory where this file (api/index.py) lives
api_dir = os.path.dirname(os.path.abspath(__file__))

# Go one level up to get the project root (where app.py is)
root_dir = os.path.dirname(api_dir)

# Add project root to Python's path so it can find app.py
sys.path.insert(0, root_dir)

from app import app
import sys
import os

# Print paths for debugging — visible in Vercel logs
print("Current dir:", os.getcwd())
print("File dir:", os.path.dirname(os.path.abspath(__file__)))
print("Sys path:", sys.path)

api_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(api_dir)
sys.path.insert(0, root_dir)

print("Root dir:", root_dir)
print("Files in root:", os.listdir(root_dir))

from app import app
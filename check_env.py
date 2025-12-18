import sys
import os

print("--- Environment Check ---")
print(f"Python Path: {sys.executable}")
try:
    import requests
    print("✅ Requests is INSTALLED")
except ImportError:
    print("❌ Requests is MISSING")

try:
    import flask
    print("✅ Flask is INSTALLED")
except ImportError:
    print("❌ Flask is MISSING")
"""
launcher
"""
from Core import checkready
import os

try:
    theOS = os.getenv("TRAVIS_OS_NAME")
except:
    print("ok")
if not theOS == "linux":
    checkready()

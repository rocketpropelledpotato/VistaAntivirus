"""
launcher
"""
from Core import checkready
import os

theOS = os.getenv("TRAVIS_OS_NAME")
if not theOS == "linux":
    checkready()

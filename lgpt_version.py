import sys
import os
from pathlib import Path

def get_lgpt_version():
    """Get absolute path to version resource"""

    if getattr(sys, 'frozen', False):
        # Running as executable
        base_path = sys._MEIPASS
    else:
        # Running as script
        base_path = os.path.abspath(".")

    filepath = os.path.join(base_path, "version.txt")

    try:
        version = Path(filepath).read_text(encoding="utf-8")
    except FileNotFoundError:
        version = "unknown"

    return version
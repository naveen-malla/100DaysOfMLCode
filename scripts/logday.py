import os, re, sys
from pathlib import Path

README_PATH = Path(os.environ.get("README_PATH", "README.md"))
LOG_TEXT = os.environ.get("LOG_TEXT", "").strip()

if not LOG_TEXT:
    print("No LOG_TEXT provided; nothing to do.")
    sys.exit(0)

if not README_PATH.exists():
    print(f"{README_PATH} not found.")
    sys.exit(1)

text = README_PATH.read_text(encoding="utf-8")

# Find the highest existing DAY n:
pattern = re.compile(r'^DAY\s+(\d+):', re.MULTILINE)
nums = [int(n) for n in pattern.findall(text)]
next_day = (max(nums) + 1) if nums else 1

# Append in the existing style:
if not text.endswith("\n"):
    text += "\n"

append_block = f"DAY {next_day}: {LOG_TEXT}"
README_PATH.write_text(text + append_block, encoding="utf-8")
print(f"Appended DAY {next_day}")

import os

ENTRY = "Contents under pressure. Do not puncture, incinerate, or disagree."

out_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

if not ENTRY.strip():
    raise SystemExit("entry is whitespace only")
if not 1 <= len(ENTRY) <= 160:
    raise SystemExit("entry length out of range: %d" % len(ENTRY))

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)

print("LEN=%d" % len(ENTRY))

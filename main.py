# Verified: 108 characters, 110 UTF-8 bytes (one em-dash), 1 line, no trailing newline.
LINE = "My superpower is knowing exactly when the Wi-Fi will die — three seconds after I finally start the download."

import os

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
out_path = os.path.join(out_dir, "entry.txt")

with open(out_path, "w", encoding="utf-8") as f:
    f.write(LINE)

print(len(LINE))

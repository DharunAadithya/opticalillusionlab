import os

filepath = "src/pages/index.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("Expanding Hole")
if idx != -1:
    print("Found Expanding Hole in index.astro:")
    safe_text = content[idx+1000:idx+2500].encode('ascii', errors='replace').decode('ascii')
    print(safe_text)

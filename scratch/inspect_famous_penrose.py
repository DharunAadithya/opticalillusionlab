import os

filepath = "src/pages/famous.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find('id="penrose-illusion"')
if idx != -1:
    safe_text = content[idx+1800:idx+3200].encode('ascii', errors='replace').decode('ascii')
    print(safe_text)

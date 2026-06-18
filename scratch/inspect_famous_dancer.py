import os

filepath = "src/pages/famous.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find('id="dancer-illusion"')
if idx != -1:
    safe_text = content[idx+600:idx+2300].encode('ascii', errors='replace').decode('ascii')
    print(safe_text)

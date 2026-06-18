import os

filepath = "src/pages/index.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("id=\"ishihara-card\"")
if idx != -1:
    print("Found ishihara-card in index.astro:")
    print(content[idx:idx+2000].encode('ascii', errors='replace').decode('ascii'))
else:
    print("ishihara-card not found")

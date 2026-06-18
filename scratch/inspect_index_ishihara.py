import os

filepath = "src/pages/index.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

print("Occurrences of 'ishihara':", content.lower().count("ishihara"))
idx = content.lower().find("ishihara")
if idx != -1:
    print(content[idx:idx+1500].encode('ascii', errors='replace').decode('ascii'))
else:
    print("Not found")

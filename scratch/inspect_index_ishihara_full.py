import os

filepath = "src/pages/index.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("id=\"ishihara-card\"")
if idx != -1:
    end_idx = content.find("</div>\n      </div>", idx + 2000)
    if end_idx == -1:
        end_idx = idx + 3500
    print(content[idx:end_idx].encode('ascii', errors='replace').decode('ascii'))
else:
    print("ishihara-card not found")

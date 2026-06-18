import re
import os

filepath = "src/pages/index.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Search for the cards or SVGs in the homepage
# Let's search for card containers or titles
# Hompage might have a gallery or list
cards = re.findall(r'<div class="group[^"]*"(.*?)</div>\s*</div>', content, re.DOTALL)
print(f"Found {len(cards)} card structures in index.astro.")

# Let's look for titles in headers like h3
titles = re.findall(r'<h3[^>]*>(.*?)</h3>', content, re.DOTALL)
print("Found h3 titles in index.astro:")
for t in titles:
    print(f" - {t.strip()}")

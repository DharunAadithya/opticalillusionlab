import re
import os

filepath = "src/pages/what-do-you-see.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for card structures
card_blocks = re.findall(r'<div class="wdys-card".*?</div>\s*</div>', content, re.DOTALL)
print(f"Found {len(card_blocks)} card blocks.")

for i, block in enumerate(card_blocks, 1):
    title_match = re.search(r'<h2 class="wdys-card-title">(.*?)</h2>', block)
    desc_match = re.search(r'<p class="wdys-card-desc">(.*?)</p>', block)
    id_match = re.search(r'id="(.*?)"', block)
    
    title = title_match.group(1) if title_match else "No Title"
    desc = desc_match.group(1) if desc_match else "No Desc"
    cid = id_match.group(1) if id_match else "No ID"
    
    print(f"Card {i}: ID='{cid}' | Title='{title}' | Desc='{desc[:60]}...'")

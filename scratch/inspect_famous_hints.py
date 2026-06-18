import os
import re

filepath = "src/pages/famous.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Find any occurrences of '👉' or 'Hint' or 'Instruction'
matches = re.finditer(r'(👉|Hint|Instruction).*?\n', content)
print("Famous page hints/guides:")
count = 0
for m in matches:
    print(m.group(0).strip())
    count += 1
    if count > 20:
        break

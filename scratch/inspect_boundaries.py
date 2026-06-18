import re
import os

filepath = "src/pages/what-do-you-see.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Let's find Card 12 and see what comes after it
idx = content.find('id="card-12"')
if idx != -1:
    print("Found card 12. Context after it:")
    print(content[idx+500:idx+2500])
else:
    print("Could not find card 12")

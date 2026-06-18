import os

filepath = "src/pages/famous.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Let's count how many times 'stairsContainer' occurs
print("Occurrences of 'stairsContainer':", content.count("stairsContainer"))

# Let's find index of all occurrences
idx = 0
while True:
    idx = content.find("stairsContainer", idx)
    if idx == -1:
        break
    print(f"Index: {idx}. Context:")
    print(content[idx:idx+300].encode('ascii', errors='replace').decode('ascii'))
    idx += len("stairsContainer")

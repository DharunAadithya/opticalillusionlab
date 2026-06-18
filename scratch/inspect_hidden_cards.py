import os

filepath = "src/pages/hidden.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for card 7 (Hermann) and card 10 (Elephant)
for card_id in ["hermann-grid", "impossible-elephant"]:
    idx = content.find(f'data-id="{card_id}"')
    if idx != -1:
        print(f"\n--- Card {card_id} ---")
        print(content[idx:idx+5000].encode('ascii', errors='replace').decode('ascii'))
    else:
        print(f"Card {card_id} not found")

import os

filepath = "src/pages/famous.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Let's locate the Hermann Grid card block
hermann_start_str = '<a href="/illusions/hermann-grid" id="hermann-illusion"'
hermann_idx = content.find(hermann_start_str)
if hermann_idx == -1:
    print("Error: Could not find Hermann Grid card start")
    exit(1)

# Find the end of the Hermann Grid card block. It ends with </a> followed by a newline and some spacing
# Let's find the next "</a>" after hermann_idx
hermann_end_tag = '</a>'
next_end_tag_idx = content.find(hermann_end_tag, hermann_idx)
if next_end_tag_idx == -1:
    print("Error: Could not find Hermann Grid card end")
    exit(1)

hermann_block_end = next_end_tag_idx + len(hermann_end_tag)
hermann_block = content[hermann_idx:hermann_block_end]
print("Found Hermann Grid block of length:", len(hermann_block))

# Now, let's locate the duplicate Cards 16-20 block that starts with Card 16 comment at the bottom
# Let's search for the second occurrence of "<!-- Card 16: Penrose Stairs -->"
stairs_comment = "<!-- Card 16: Penrose Stairs -->"
first_stairs_idx = content.find(stairs_comment)
second_stairs_idx = content.find(stairs_comment, first_stairs_idx + 1)

if second_stairs_idx == -1:
    print("Error: Could not find second occurrence of Penrose Stairs comment")
    exit(1)

# The duplicate block goes from second_stairs_idx to the end of McGurk card
# McGurk card ends right before "</div>\n  </section>"
end_section_str = "</div>\n  </section>"
dup_end_idx = content.find(end_section_str, second_stairs_idx)
if dup_end_idx == -1:
    print("Error: Could not find end of section after duplicate cards")
    exit(1)

duplicate_block = content[second_stairs_idx:dup_end_idx]
print("Found duplicate block of length:", len(duplicate_block))

# Now let's extract the clean content without the duplicate block, and without the misplaced Hermann Grid card
# misplaces Hermann Grid is at hermann_idx to hermann_block_end.
# Since hermann grid is before duplicate block, let's check:
# content is structured as:
# [Pre-Hermann Content] + [Hermann Block] + [Between Block] + [Duplicate Block] + [Post-Duplicate Content]
# Let's split content accordingly:
pre_hermann = content[:hermann_idx]
between_block = content[hermann_block_end:second_stairs_idx]
post_duplicate = content[dup_end_idx:]

# Let's see: the first stairs comment is at line 1021.
# We want to insert the Hermann block right before "<!-- Card 16: Penrose Stairs -->" in the first block.
# Let's find "<!-- Card 16: Penrose Stairs -->" in pre_hermann:
card_15_comment = "<!-- Card 15: Hermann Grid -->"
card_15_idx = pre_hermann.find(card_15_comment)
if card_15_idx == -1:
    print("Error: Could not find Card 15 comment in pre-Hermann content")
    exit(1)

# We will place Hermann Grid card block right after "<!-- Card 15: Hermann Grid -->\n      "
insert_idx = card_15_idx + len(card_15_comment)
# Let's find the newline after the comment:
next_nl = pre_hermann.find("\n", insert_idx)
if next_nl != -1:
    insert_idx = next_nl + 1

# Reconstruct:
# 1. pre_hermann up to insert_idx
# 2. hermann_block + \n
# 3. pre_hermann from insert_idx to end
# 4. between_block
# 5. post_duplicate
new_pre = pre_hermann[:insert_idx] + "      " + hermann_block + "\n\n" + pre_hermann[insert_idx:]
new_content = new_pre + between_block + post_duplicate

# Save to famous_new.astro and inspect
with open("src/pages/famous.astro", "w", encoding="utf-8") as f:
    f.write(new_content)

print("famous.astro reorganized successfully!")

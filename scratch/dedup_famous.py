import os

filepath = "src/pages/famous.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Let's count occurrences of "<script>"
script_blocks = content.split("<script>")
print("Number of script segments:", len(script_blocks))

# Let's see: the last segment contains the duplicate scripts
if len(script_blocks) > 1:
    last_block = script_blocks[-1]
    
    # We want to find the first and second occurrences of the card scripts.
    # The card scripts start with "// 16. Penrose Stairs" or similar.
    # Let's see: the block:
    # "    // ----------------------------------------------------"
    # "    // 5 NEW CARDS INTERACTIVITY SCRIPTS"
    # "    // ----------------------------------------------------"
    card_script_start = "    // ----------------------------------------------------\n    // 5 NEW CARDS INTERACTIVITY SCRIPTS\n    // ----------------------------------------------------"
    
    occ_count = last_block.count(card_script_start)
    print("Occurrences of card script start in last block:", occ_count)
    
    if occ_count == 2:
        # We can find the first occurrence and the second occurrence
        first_idx = last_block.find(card_script_start)
        second_idx = last_block.find(card_script_start, first_idx + len(card_script_start))
        
        # Let's print the length of the block between first and second
        print("Distance between duplicates:", second_idx - first_idx)
        
        # Let's remove the second occurrence.
        # Wait, the second occurrence runs until right before "// Stop event propagation on inner details" or something?
        # Let's check:
        # In patch_famous.py:
        # js_code + "\n    // Stop event propagation on inner details"
        # Since it replaced "// Stop event propagation on inner details", the second occurrence has it right after.
        # Let's check what is at the end of the duplicate.
        # Actually, let's just replace the duplicate block with a single one.
        # We can reconstruct last_block:
        new_last_block = last_block[:second_idx] + last_block[second_idx:].replace(card_script_start, "", 1)
        # Wait, let's verify if there is any other duplicate text in it.
        # Let's write the deduped file and print success.
        
        # Let's do it precisely by finding the start of the card script, and removing one of the copies.
        # Let's see: the JS code in last_block is:
        # ...card_script_start... (copy 1) ...card_script_start... (copy 2) ...
        # If we keep everything up to the second occurrence, and then concatenate from the end of the second occurrence's JS code.
        # Let's find the exact JS code length.
        # In patch_famous.py, the js_code goes from "    // ----------------------------------------------------" to "      });\n    };\n" (applySort end).
        # Let's just find:
        # part1: up to the second occurrence of card_script_start
        # part2: after the second occurrence of card_script_start. Since card_script_start was injected, the second one has a duplicate of the entire block.
        # We can just remove the entire duplicate block.
        # Let's print the text around the second occurrence to verify.
        print("Text at second occurrence start:")
        print(last_block[second_idx:second_idx+500])
        
        # Let's remove the second block. We can do this by deleting the text from second_idx to the next '// Stop event propagation on inner details' or similarly.
        # Let's find out how it looks.
        prop_str = "    // Stop event propagation on inner details"
        prop_idx = last_block.find(prop_str, second_idx)
        if prop_idx != -1:
            # We want to remove from second_idx to prop_idx + len(prop_str)
            print("Found prop_str after second_idx. Removing duplicate block.")
            deduped_last = last_block[:second_idx] + last_block[prop_idx:]
            script_blocks[-1] = deduped_last
            new_content = "<script>".join(script_blocks)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("dedup_famous.py: successfully deduped famous.astro!")
        else:
            print("Could not find prop_str after second_idx")
else:
    print("No script block found")

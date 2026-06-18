import re

filepath = "src/pages/what-do-you-see.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Let's locate the card-12 div
card_idx = content.find('id="card-12"')
if card_idx != -1:
    print("Found Card 12 in file.")
    # Search for the next section closing tag
    section_close_idx = content.find('</section>', card_idx)
    if section_close_idx != -1:
        # Find the last </div> before the section close, which is the card's closing </div>
        last_div_idx = content.rfind('</div>', card_idx, section_close_idx)
        if last_div_idx != -1:
            injections = """
        <!-- Collapsible Explanation -->
        <details class="w-full mt-4 border-t border-slate-800/40 pt-3 text-xs text-slate-400 select-none text-left">
          <summary class="font-bold cursor-pointer hover:text-purple-400">👁️ Reveal Answer & Science</summary>
          <p class="mt-2 font-normal leading-relaxed text-slate-400">
            W.E. Hill's classic 'My Wife and My Mother-in-Law' is a bistable portrait. The young lady's chin is the old lady's nose, and her necklace is the old lady's mouth, illustrating top-down prediction processing.
          </p>
        </details>

        <!-- Explore Link -->
        <div class="w-full mt-4 pt-4 border-t border-slate-500/10 flex justify-between items-center text-xs font-black text-indigo-400 hover:text-indigo-300 transition-colors">
          <span>Explore Science & Facts</span>
          <a href="/illusions/wife-mother-in-law" class="hover:underline">Explore &rarr;</a>
        </div>
"""
            content = content[:last_div_idx] + injections + content[last_div_idx:]
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print("Successfully patched Card 12!")
        else:
            print("Could not find last div before section close")
    else:
        print("Could not find section close after card-12")
else:
    print("Could not find card-12")

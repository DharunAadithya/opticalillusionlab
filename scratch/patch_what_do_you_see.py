import re
import os

filepath = "src/pages/what-do-you-see.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

card_data = {
    1: {
        "slug": "old-woman-young-woman",
        "instruction": "Observe the profile line. Can you see a young lady looking away, or an old woman looking downwards in profile?",
        "explanation": "The Old Woman / Young Woman portrait is a classic bistable ambiguous figure. The young woman's cheek and chin double as the old woman's nose, her ear represents the old woman's eye, and her neckband is perceived as the old woman's mouth. The brain cannot resolve both interpretations simultaneously, toggling its attention between them.",
    },
    2: {
        "slug": "duck-rabbit",
        "instruction": "Observe the protrusions on the left. Do you see them as a duck's open bill facing left, or a rabbit's ears facing right?",
        "explanation": "The Duck-Rabbit is a classic bistable figure. The horizontal protrusions function as either a duck's bill or a rabbit's ears. The brain alternates between these interpretations based on top-down semantic priming and gaze orientation.",
    },
    3: {
        "slug": "rubins-vase",
        "instruction": "Stare at the center. Do you see a yellow vase, or two dark profiles facing each other?",
        "explanation": "Rubin's Vase is a classic figure-ground illusion. The visual cortex must decide whether to assign the central contour to the foreground (creating a vase) or the background (creating two profiles facing each other).",
    },
    4: {
        "slug": "duck-squirrel",
        "instruction": "Observe the main figure shape. Is it a duck looking to the left, or a squirrel holding a nut facing right?",
        "explanation": "The Duck-Squirrel is a modern figure-ground bistable illusion. The shape of the squirrel's tail forms the duck's beak on the left. The brain's object recognition system interprets the contours based on semantic priming.",
    },
    5: {
        "slug": "skull-women",
        "instruction": "Squint your eyes or step back. Do you see a large skull, or two women in dresses sitting opposite each other at a table?",
        "explanation": "This skull composite drawing is an ambiguous illusion. When viewed close, high-frequency details (two women at a table) dominate. From a distance, low-frequency details group to form a human skull, where the women's heads form the eyes and the plates form the teeth.",
    },
    6: {
        "slug": "saxophonist-woman",
        "instruction": "Look at the black silhouette. Do you see a profile of a saxophone player, or the white background shaping a woman's face in highlight?",
        "explanation": "The Saxophonist / Woman's Face is a figure-ground bistable outline. The black silhouette outlines a saxophone player, while the white negative space outlines a woman's face lit from the side.",
    },
    7: {
        "slug": "penguin-cat",
        "instruction": "Observe the white negative space. Is it a waddling penguin, or a silhouette of a cat's head?",
        "explanation": "The Penguin / Cat is a silhouette bistable illusion. The white inner shape represents a penguin's body, while the surrounding black contours outline a cat's head, showing how figure-ground segregation defines object boundaries.",
    },
    8: {
        "slug": "spinning-dancer",
        "instruction": "Observe the dancer's silhouette. Is she spinning clockwise or counter-clockwise? Toggle the helper belt to help focus.",
        "explanation": "The Spinning Dancer is an ambiguous silhouette illusion. Since it has no depth or volumetric cues (no shadows or light reflections), the brain cannot determine whether the rotation is clockwise or counter-clockwise.",
    },
    9: {
        "slug": "necker-cube",
        "instruction": "Look at the wireframe cube. Which face is in the front? Watch it flip in your mind's eye.",
        "explanation": "The Necker Cube is a wireframe bistable projection. With no depth markers, both the front and back planes are equally plausible, causing the visual system to constantly toggle the cube's orientation in 3D space.",
    },
    10: {
        "slug": "three-dots-motion",
        "instruction": "Watch the two moving circles. Do they appear to pass through each other, or bounce off each other? Drag the cover slider to check.",
        "explanation": "The three dots motion (or bouncing dots) illusion demonstrates how the brain resolves ambiguous motion paths. Without line context, the dots appear to bounce off each other; adding a grid or occlusion primes the brain to see them pass through.",
    },
    11: {
        "slug": "seasonal-duck-rabbit",
        "instruction": "Look at the animal outline. Jastrow's research shows that the current month primes your brain to see one animal first.",
        "explanation": "The Seasonal Duck-Rabbit demonstrates how top-down cognitive priming works. The current season (spring/summer vs autumn/winter) primes our semantic pathways, influencing which animal our visual cortex resolves first.",
    },
    12: {
        "slug": "wife-mother-in-law",
        "instruction": "Stare at the nose and chin area. Can you see a young lady looking away, or an elderly woman looking downwards?",
        "explanation": "W.E. Hill's classic 'My Wife and My Mother-in-Law' is a bistable portrait. The young lady's chin is the old lady's nose, and her necklace is the old lady's mouth, illustrating top-down prediction processing.",
    }
}

# 1. Update Card 2 SVG to the upgraded high-contrast Duck-Rabbit
old_duck_rabbit_svg = """          <svg id="svg-duck-rabbit" class="wdys-svg" viewBox="0 0 280 200" xmlns="http://www.w3.org/2000/svg">
            <!-- Duck/Rabbit ambiguous body -->
            <ellipse class="wdys-fill-primary" cx="145" cy="105" rx="70" ry="50"/>
            <!-- Head/beak area -->
            <ellipse class="wdys-fill-primary" cx="85" cy="95" rx="38" ry="33"/>
            <!-- Duck bill / Rabbit ears -->
            <path class="wdys-fill-primary" d="M 48,78 Q 20,68 8,85 Q 14,98 48,95 Z"/>
            <path class="wdys-fill-primary" d="M 48,95 Q 20,98 10,115 Q 18,128 48,112 Z"/>
            <!-- Rabbit ear 1 (top) — same as duck bill top -->
            <!-- Eye -->
            <circle cx="72" cy="82" r="5" fill="white"/>
            <circle cx="72" cy="82" r="2.5" fill="#1e293b"/>
            <!-- Highlight -->
            <circle cx="73" cy="81" r="1" fill="white"/>
            <!-- Tail (rabbit) / Wing nub (duck) -->
            <path class="wdys-fill-secondary" d="M 210,88 Q 230,82 235,100 Q 228,115 210,112 Z"/>
            <!-- Webbed foot / fluffy bottom -->
            <path class="wdys-fill-secondary" d="M 140,152 Q 155,165 170,158 Q 175,148 160,145 Z"/>
            <path class="wdys-fill-secondary" d="M 118,155 Q 130,168 145,162 Q 148,150 134,147 Z"/>
          </svg>"""

new_duck_rabbit_svg = """          <svg id="svg-duck-rabbit" class="wdys-svg" viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" style="background: #0f172a; border-radius: 12px; padding: 10px;">
            <!-- Upgraded high contrast Duck-Rabbit with white fill on dark background -->
            <ellipse cx="160" cy="110" rx="75" ry="55" fill="#ffffff" />
            <ellipse cx="95" cy="100" rx="40" ry="35" fill="#ffffff" />
            <path d="M 58,82 Q 25,72 10,90 Q 18,103 58,100 Z" fill="#ffffff" />
            <path d="M 58,100 Q 25,103 12,120 Q 20,133 58,117 Z" fill="#ffffff" />
            <circle cx="82" cy="86" r="6" fill="#0f172a" />
            <circle cx="82" cy="86" r="3" fill="#ffffff" />
            <path d="M 95,120 Q 90,110 95,100" stroke="#0f172a" stroke-width="2.5" fill="none" />
          </svg>"""

if old_duck_rabbit_svg in content:
    content = content.replace(old_duck_rabbit_svg, new_duck_rabbit_svg)
    print("Upgraded Duck-Rabbit SVG in Card 2")
else:
    # Try alternate formatting
    content = re.sub(
        r'<svg id="svg-duck-rabbit".*?</svg>',
        new_duck_rabbit_svg,
        content,
        flags=re.DOTALL
    )
    print("Upgraded Duck-Rabbit SVG in Card 2 via regex")

# Let's perform card updates step-by-step
for num, info in card_data.items():
    card_pattern = rf'(<!-- ===== CARD {num}: .*? ===== -->\s*<div class="wdys-card"[^>]*id="card-{num}"[^>]*>)'
    # Find this header
    match = re.search(card_pattern, content)
    if not match:
        print(f"Error: Card {num} pattern not found")
        continue
    
    # We want to inject the Instruction Box above <div class="wdys-demo-area">
    # Let's locate the next <div class="wdys-demo-area"> after the card match
    card_idx = match.end()
    demo_idx = content.find('<div class="wdys-demo-area">', card_idx)
    if demo_idx == -1:
        demo_idx = content.find('<div class="wdys-demo-area"', card_idx)
    
    if demo_idx != -1:
        ins_box = f"""
        <!-- Instruction Box -->
        <div class="my-3 flex items-start gap-2 rounded-xl border border-indigo-500/10 bg-indigo-500/5 p-3 text-xs text-slate-350 text-left">
          <span class="text-base leading-none">👁️</span>
          <div>
            <strong class="text-slate-200">Instructions:</strong> {info['instruction']}
          </div>
        </div>
"""
        content = content[:demo_idx] + ins_box + content[demo_idx:]
        print(f"Injected Instruction Box for Card {num}")
        
    # We also want to inject the collapsible explanation and Explore link right before the closing </div> of the card.
    # Let's find the closing </div> of this card.
    # To find the card's ending, let's search for the start of the next card or the end of the grid:
    next_card_comment = f'<!-- ===== CARD {num+1}:' if num < 12 else '</div>\n  </section>\n\n  <!-- Results Section -->'
    end_search_idx = content.find(next_card_comment, card_idx + 200) # search further down
    if end_search_idx != -1:
        # Find the last </div> before this next comment, which is the card's closing </div>
        # Let's search backwards from end_search_idx for '</div>'
        last_div_idx = content.rfind('</div>', card_idx, end_search_idx)
        if last_div_idx != -1:
            injections = f"""
        <!-- Collapsible Explanation -->
        <details class="w-full mt-4 border-t border-slate-800/40 pt-3 text-xs text-slate-400 select-none text-left">
          <summary class="font-bold cursor-pointer hover:text-purple-400">👁️ Reveal Answer & Science</summary>
          <p class="mt-2 font-normal leading-relaxed text-slate-400">
            {info['explanation']}
          </p>
        </details>

        <!-- Explore Link -->
        <div class="w-full mt-4 pt-4 border-t border-slate-500/10 flex justify-between items-center text-xs font-black text-indigo-400 hover:text-indigo-300 transition-colors">
          <span>Explore Science & Facts</span>
          <a href="/illusions/{info['slug']}" class="hover:underline">Explore &rarr;</a>
        </div>
"""
            content = content[:last_div_idx] + injections + content[last_div_idx:]
            print(f"Injected Explanation and Explore Link for Card {num}")
        else:
            print(f"Error: Could not find closing div for Card {num}")
    else:
        print(f"Error: Could not find next card boundary for Card {num}")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("what-do-you-see.astro successfully patched!")

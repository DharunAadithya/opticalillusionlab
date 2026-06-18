import os
import re

workspace_dir = "c:/Users/Amrutha/Documents/opticalillusionlab"
pages_dir = os.path.join(workspace_dir, "src/pages")
hidden_path = os.path.join(pages_dir, "hidden.astro")

if os.path.exists(hidden_path):
    print("Found hidden.astro, preparing restructure...")
    
    # We will read the top part of hidden.astro up to '<!-- Main Content Grid -->'
    # and the bottom part starting from '<style>'
    # and we will generate the stacked, single-column cards dynamically in the middle!
    
    content = open(hidden_path, "r", encoding="utf-8").read()
    
    # Let's extract the header part of the page
    main_grid_idx = content.find('<main class="py-16 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">')
    header_part = content[:main_grid_idx + len('<main class="py-16 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">\n    <div class="grid grid-cols-1 gap-16 max-w-3xl mx-auto">')]
    
    # Let's extract the script and style part at the bottom
    script_idx = content.find('<style>')
    footer_part = content[script_idx:]
    
    # Define our 10 cards data
    cards_data = [
        {
            "id": "wife-mother-in-law",
            "slug": "wife-mother-in-law",
            "difficulty": "🟡 Medium",
            "category": "Ambiguous",
            "title": "1. My Wife and My Mother-in-Law",
            "desc": "One of the most famous ambiguous figures in history. A single drawing depicts both a young lady facing away and an old woman looking downwards.",
            "ins": "Can you see both? The young woman's chin is the old woman's nose. The young woman's ear is the old woman's eye. The young woman's necklace is the old woman's mouth.",
            "svg": """<svg class="w-full h-full select-none" viewBox="0 0 400 400" id="svg-wife-mother" style="background: #808080; border-radius: 16px;">
              <!-- Background / Headscarf -->
              <path d="M 100,80 Q 200,40 300,80 Q 350,150 310,250 Q 260,330 180,330 Q 140,330 110,290" fill="none" stroke="#111" stroke-width="4" />
              <!-- Feather -->
              <path d="M 230,80 Q 250,20 230,5" fill="none" stroke="#111" stroke-width="2.5" />
              <!-- Hair / Fur coat base -->
              <path d="M 120,290 Q 180,310 240,290 C 270,270 290,220 300,180" fill="none" stroke="#111" stroke-width="3" />
              <!-- Nose (Young cheek/jaw vs Old nose) -->
              <path d="M 180,180 Q 150,200 168,230 Q 182,245 178,255 Q 192,275 180,300 Q 190,310 200,320" fill="none" stroke="#111" stroke-width="4.5" />
              <!-- Neckband / Mouth (Young necklace vs Old mouth) -->
              <path d="M 190,300 Q 210,303 230,297" fill="none" stroke="#111" stroke-width="3" stroke-linecap="round" />
              <!-- Ear / Eye (Young ear vs Old eye) -->
              <path d="M 220,210 C 215,205 210,210 212,216 C 214,222 222,220 220,210" fill="none" stroke="#111" stroke-width="3" />
              <!-- Old chin / Young chest -->
              <path d="M 180,330 Q 210,350 250,355" fill="none" stroke="#111" stroke-width="3.5" />
              <!-- Eyelash of Young / Nose bridge of Old -->
              <path d="M 172,185 Q 166,190 162,197" fill="none" stroke="#111" stroke-width="2" />
              
              <!-- Diagram Highlights Overlay (Revealed via JS) -->
              <g class="diagram-overlay opacity-0 transition-opacity duration-300">
                <!-- Young Woman markers -->
                <path d="M 180,180 L 160,200 L 168,230" stroke="#3b82f6" stroke-width="3" fill="none" class="young-path" />
                <circle cx="215" cy="213" r="10" stroke="#3b82f6" stroke-width="2.5" fill="none" />
                <path d="M 190,300 Q 210,303 230,297" stroke="#3b82f6" stroke-width="4.5" fill="none" />
                <text x="70" y="210" fill="#3b82f6" font-size="12" font-weight="900">Young Cheek / Jaw</text>
                <text x="250" y="200" fill="#3b82f6" font-size="12" font-weight="900">Young Ear</text>
                <text x="250" y="320" fill="#3b82f6" font-size="12" font-weight="900">Choker Necklace</text>

                <!-- Old Woman markers -->
                <path d="M 180,180 Q 150,200 168,230" stroke="#ef4444" stroke-width="4.5" fill="none" />
                <circle cx="215" cy="213" r="5" fill="#ef4444" />
                <path d="M 190,300 Q 210,303 230,297" stroke="#ef4444" stroke-width="4.5" fill="none" />
                <text x="70" y="240" fill="#ef4444" font-size="12" font-weight="900">Old Large Nose</text>
                <text x="250" y="230" fill="#ef4444" font-size="12" font-weight="900">Old Eye</text>
                <text x="250" y="280" fill="#ef4444" font-size="12" font-weight="900">Old Mouth</text>
              </g>
            </svg>""",
            "controls": """<div class="flex flex-wrap gap-3 justify-center">
              <button class="btn-vote bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs px-4 py-2.5 rounded-xl transition-all shadow" data-vote="young">👱‍♀️ Young Woman first</button>
              <button class="btn-vote bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs px-4 py-2.5 rounded-xl transition-all shadow" data-vote="old">👵 Old Woman first</button>
              <button class="btn-reveal border border-purple-500/30 text-purple-400 hover:bg-purple-500/10 font-bold text-xs px-4 py-2.5 rounded-xl transition-all">Reveal Outlines</button>
            </div>
            
            <div class="stats-panel hidden w-full p-4 bg-purple-500/5 border border-purple-500/20 rounded-xl text-xs space-y-2">
              <div class="flex justify-between font-black text-slate-900 dark:text-white">
                <span>👱‍♀️ Young Woman: <span class="pct-young">52%</span></span>
                <span>👵 Old Woman: <span class="pct-old">48%</span></span>
              </div>
              <div class="w-full bg-slate-700 h-2 rounded-full overflow-hidden flex">
                <div class="bg-purple-500 h-full bar-young" style="width: 52%;"></div>
                <div class="bg-indigo-400 h-full bar-old" style="width: 48%;"></div>
              </div>
              <p class="text-[10px] text-slate-400 italic">Which one you see first may depend on your age! Fun fact: younger viewers usually spot the young woman first.</p>
            </div>""",
            "explanation": "My Wife and My Mother-in-Law is one of the most famous bistable ambiguous figures. Popularized by cartoonist W. E. Hill in 1915, the drawing contains both a young woman facing away into the background and an old woman looking downward in profile. The visual cortex experiences a rivalry between the two interpretations because the same line segments represent different facial features in each version: the young woman's chin functions as the old woman's nose, the young woman's ear acts as the old woman's eye, and the young woman's necklace is perceived as the old woman's mouth. This demonstrates that object recognition is a top-down prediction process.",
            "min_h": "400px"
        },
        {
            "id": "all-is-vanity",
            "slug": "all-is-vanity",
            "difficulty": "🟡 Medium",
            "category": "Ambiguous",
            "title": "2. All is Vanity",
            "desc": "Created by Charles Allan Gilbert in 1892. This illustration shows a woman sitting at a vanity table, but the overall composition morphs into a giant human skull.",
            "ins": "Squint your eyes or step back from the screen. The round vanity mirror forms the skull dome; the woman's head and reflection form the eye sockets; the makeup bottles on the counter form the teeth.",
            "svg": """<svg class="w-full h-full select-none" viewBox="0 0 200 200" id="svg-vanity">
              <!-- Vanity mirror (Skull head outline) -->
              <circle cx="100" cy="80" r="50" fill="none" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-200" />
              <!-- Eye sockets (Woman's head and its reflection) -->
              <circle cx="85" cy="85" r="14" fill="none" stroke="currentColor" stroke-width="1.5" class="text-slate-400 dark:text-slate-600" />
              <circle cx="115" cy="85" r="14" fill="none" stroke="currentColor" stroke-width="1.5" class="text-slate-400 dark:text-slate-600" />
              <path d="M 80,85 C 80,75 90,75 90,85" fill="none" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-200" />
              <path d="M 110,85 C 110,75 120,75 120,85" fill="none" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-200" />
              <!-- Table / Jaw line -->
              <path d="M 40,140 L 160,140 L 150,175 L 50,175 Z" fill="none" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-200" />
              <!-- Perfume bottles (Teeth) -->
              <g stroke="currentColor" stroke-width="1.5" class="text-slate-900 dark:text-slate-200">
                <line x1="85" y1="140" x2="85" y2="152" />
                <line x1="92" y1="140" x2="92" y2="152" />
                <line x1="100" y1="140" x2="100" y2="152" />
                <line x1="108" y1="140" x2="108" y2="152" />
                <line x1="115" y1="140" x2="115" y2="152" />
              </g>
              
              <g class="diagram-overlay opacity-0 transition-opacity duration-300">
                <!-- Outer skull outline in red -->
                <circle cx="100" cy="80" r="50" fill="none" stroke="#ef4444" stroke-width="3" />
                <path d="M 75,130 L 125,130 L 115,160 L 85,160 Z" fill="none" stroke="#ef4444" stroke-width="3" />
                <text x="100" y="25" fill="#ef4444" font-size="12" font-weight="900" text-anchor="middle">Skull Shape</text>
              </g>
            </svg>""",
            "controls": """<div class="flex flex-wrap gap-3 justify-center">
              <button class="btn-vote bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs px-4 py-2.5 rounded-xl transition-all shadow" data-vote="woman">A Woman 👩</button>
              <button class="btn-vote bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs px-4 py-2.5 rounded-xl transition-all shadow" data-vote="skull">A Skull 💀</button>
              <button class="btn-reveal border border-purple-500/30 text-purple-400 hover:bg-purple-500/10 font-bold text-xs px-4 py-2.5 rounded-xl transition-all">Reveal Skull Outline</button>
            </div>
            
            <div class="stats-panel hidden w-full p-4 bg-purple-500/5 border border-purple-500/20 rounded-xl text-xs space-y-2">
              <div class="flex justify-between font-black text-slate-900 dark:text-white">
                <span>👩 A Woman: <span class="pct-young">45%</span></span>
                <span>💀 A Skull: <span class="pct-old">55%</span></span>
              </div>
              <div class="w-full bg-slate-700 h-2 rounded-full overflow-hidden flex">
                <div class="bg-purple-500 h-full bar-young" style="width: 45%;"></div>
                <div class="bg-indigo-400 h-full bar-old" style="width: 55%;"></div>
              </div>
            </div>""",
            "explanation": "All is Vanity is a classic ambiguous composite drawing created by American illustrator Charles Allan Gilbert in 1892. It depicts a young woman sitting at a vanity mirror, looking at her reflection. However, when viewed from a distance, the entire scene blends to form the shape of a human skull. The round vanity mirror forms the dome of the skull, the woman's head and its reflection form the dark eye sockets, and the perfume bottles and cosmetics on the table form the row of teeth along the jaw. This illusion demonstrates how the visual system groups high-frequency detail (the woman and cosmetics) and low-frequency structures (the skull) differently based on viewing distance and focus.",
            "min_h": "400px"
        },
        {
            "id": "duck-rabbit",
            "slug": "duck-rabbit",
            "difficulty": "🟢 Easy",
            "category": "Ambiguous",
            "title": "3. Duck or Rabbit?",
            "desc": "First published in Germany in 1892 and popularized by Joseph Jastrow in 1899. A single outline forms either a duck facing left or a rabbit facing right.",
            "ins": "Observe the two protrusions on the left. Are they a duck's open bill or a rabbit's long ears? Use the hint button to see how seasonal contexts prime your brain.",
            "svg": """<svg class="w-full max-w-[300px] h-[200px] select-none bg-slate-900 rounded-xl" viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
              <!-- Upgraded high contrast Duck-Rabbit with white fill on dark background -->
              <ellipse cx="160" cy="110" rx="75" ry="55" fill="#ffffff" />
              <ellipse cx="95" cy="100" rx="40" ry="35" fill="#ffffff" />
              <path d="M 58,82 Q 25,72 10,90 Q 18,103 58,100 Z" fill="#ffffff" />
              <path d="M 58,100 Q 25,103 12,120 Q 20,133 58,117 Z" fill="#ffffff" />
              <circle cx="82" cy="86" r="6" fill="#0f172a" />
              <circle cx="82" cy="86" r="3" fill="#ffffff" />
              <path d="M 95,120 Q 90,110 95,100" stroke="#0f172a" stroke-width="2.5" fill="none" />
              
              <g class="diagram-overlay opacity-0 transition-opacity duration-300">
                <text x="150" y="45" fill="#ef4444" font-size="12" font-weight="900" text-anchor="middle">Left: Bill/Ears | Right: Tail</text>
              </g>
            </svg>""",
            "controls": """<div class="flex flex-wrap gap-3 justify-center">
              <button class="btn-vote bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs px-4 py-2.5 rounded-xl transition-all shadow" data-vote="duck">Duck 🦆</button>
              <button class="btn-vote bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs px-4 py-2.5 rounded-xl transition-all shadow" data-vote="rabbit">Rabbit 🐇</button>
              <button class="btn-reveal border border-purple-500/30 text-purple-400 hover:bg-purple-500/10 font-bold text-xs px-4 py-2.5 rounded-xl transition-all">Show Hint</button>
            </div>
            
            <div class="stats-panel hidden w-full p-4 bg-purple-500/5 border border-purple-500/20 rounded-xl text-xs space-y-2 text-left">
              <div class="flex justify-between font-black text-slate-900 dark:text-white">
                <span>🦆 Duck: <span class="pct-young">50%</span></span>
                <span>🐇 Rabbit: <span class="pct-old">50%</span></span>
              </div>
              <div class="w-full bg-slate-700 h-2 rounded-full overflow-hidden flex">
                <div class="bg-purple-500 h-full bar-young" style="width: 50%;"></div>
                <div class="bg-indigo-400 h-full bar-old" style="width: 50%;"></div>
              </div>
              <p class="text-[10px] text-slate-400 id='seasonal-hint-box'"></p>
            </div>""",
            "explanation": "The Duck-Rabbit Illusion is a classic ambiguous figure popularized by psychologist Joseph Jastrow in 1899. The silhouette is bistable: it can be seen as a duck facing to the left (where the protrusions are its bill) or a rabbit facing to the right (where the same protrusions are its ears). The visual system cannot hold both interpretations in conscious awareness simultaneously, forcing a perceptual toggle. Jastrow used the illusion to demonstrate that perception is not a passive recording of sensory data, but an active, cognitive interpretation that is heavily influenced by mental focus, context, and semantic priming.",
            "min_h": "300px"
        },
        {
            "id": "boring-figure",
            "slug": "boring-figure",
            "difficulty": "🟡 Medium",
            "category": "Ambiguous",
            "title": "4. Young Woman or Old Woman (Boring Figure)",
            "desc": "This alternative rendering of the classic Boring Figure provides an elegant layout illustrating visual bistability.",
            "ins": "Stare at the center. Do you see the young woman's ear and jawline, or the old woman's large hooked nose and mouth?",
            "svg": """<svg class="w-full h-full select-none" viewBox="0 0 200 200" id="svg-boring">
              <!-- Hat and hair -->
              <path d="M 50,40 Q 100,20 150,40 Q 170,80 140,130" fill="none" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-200" />
              <!-- Face contour -->
              <path d="M 90,40 Q 70,60 80,85 Q 85,95 83,100 Q 92,113 86,125 Q 92,133 95,138 Q 102,145 105,153" fill="none" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-100" />
              <!-- Eye / Ear -->
              <path d="M 115,100 C 111,98 109,102 111,106 C 113,108 118,106 116,102" fill="none" stroke="currentColor" stroke-width="2" class="text-slate-900 dark:text-slate-200" />
              <!-- Neckband / Mouth -->
              <path d="M 95,138 Q 105,139 115,137" fill="none" stroke="currentColor" stroke-width="2" class="text-slate-900 dark:text-slate-200" stroke-linecap="round" />
              <!-- Feather -->
              <path d="M 120,40 Q 140,5 120,0" fill="none" stroke="currentColor" stroke-width="2" class="text-slate-900 dark:text-slate-200" />

              <g class="diagram-overlay opacity-0 transition-opacity duration-300">
                <circle cx="113" cy="103" r="8" stroke="#ef4444" stroke-width="2" fill="none" />
                <text x="130" y="105" fill="#ef4444" font-size="10" font-weight="900">Young Ear / Old Eye</text>
                <path d="M 80,85 Q 85,95 83,100" stroke="#ef4444" stroke-width="3.5" fill="none" />
                <text x="20" y="95" fill="#ef4444" font-size="10" font-weight="900">Young Nose / Old Eye lash</text>
              </g>
            </svg>""",
            "controls": """<div class="flex flex-wrap gap-3 justify-center">
              <button class="btn-vote bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs px-4 py-2.5 rounded-xl transition-all shadow" data-vote="young">👱‍♀️ Young Woman</button>
              <button class="btn-vote bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs px-4 py-2.5 rounded-xl transition-all shadow" data-vote="old">👵 Old Woman</button>
              <button class="btn-reveal border border-purple-500/30 text-purple-400 hover:bg-purple-500/10 font-bold text-xs px-4 py-2.5 rounded-xl transition-all">Reveal Labels</button>
            </div>
            
            <div class="stats-panel hidden w-full p-4 bg-purple-500/5 border border-purple-500/20 rounded-xl text-xs space-y-2">
              <div class="flex justify-between font-black text-slate-900 dark:text-white">
                <span>👱‍♀️ Young: <span class="pct-young">58%</span></span>
                <span>👵 Old: <span class="pct-old">42%</span></span>
              </div>
              <div class="w-full bg-slate-700 h-2 rounded-full overflow-hidden flex">
                <div class="bg-purple-500 h-full bar-young" style="width: 58%;"></div>
                <div class="bg-indigo-400 h-full bar-old" style="width: 42%;"></div>
              </div>
            </div>""",
            "explanation": "The Boring Figure is another name for the classic Wife and Mother-in-Law illusion. It is named after American psychologist Edwin Boring, who published a detailed analysis of the drawing in 1930. Boring used the figure to map out the mathematical boundaries of visual bistability and investigate how the brain assigns outlines to different shapes. The illusion demonstrates how the visual cortex alternates between two completely separate semantic frameworks when interpreting identical visual contours.",
            "min_h": "400px"
        },
        {
            "id": "hidden-faces-trees",
            "slug": "hidden-faces-trees",
            "difficulty": "🔴 Hard",
            "category": "Ambiguous",
            "title": "5. 6 Hidden Faces in the Trees",
            "desc": "A complex botanical sketch containing negative spaces that map to six distinct human profiles.",
            "ins": "Scan the branches and negative spaces. Can you find all 6 hidden faces? Tap the face outlines directly in the drawing to highlight them.",
            "svg": """<svg class="w-full h-full select-none" viewBox="0 0 200 200" id="svg-trees">
              <!-- Base trunk & branches -->
              <path d="M 30,190 Q 50,130 50,80 Q 30,40 20,20 Q 50,40 60,70 L 60,190" fill="none" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-300" />
              <path d="M 170,190 Q 150,120 150,70 Q 170,30 180,10 Q 150,30 140,60 L 140,190" fill="none" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-300" />
              
              <!-- Face 1 target (young profile on left trunk branch) -->
              <path d="M 50,80 Q 42,75 42,70 Q 45,66 48,68 Q 45,60 50,55" fill="none" stroke="transparent" stroke-width="8" class="face-target cursor-pointer" data-idx="1" />
              <path id="highlight-1" d="M 50,80 Q 42,75 42,70 Q 45,66 48,68 Q 45,60 50,55" fill="none" stroke="#22c55e" stroke-width="2" class="opacity-0 transition-opacity" />
              
              <!-- Face 2 target (old profile on right trunk branch) -->
              <path d="M 150,70 Q 158,65 158,60 Q 155,56 152,58 Q 155,50 150,45" fill="none" stroke="transparent" stroke-width="8" class="face-target cursor-pointer" data-idx="2" />
              <path id="highlight-2" d="M 150,70 Q 158,65 158,60 Q 155,56 152,58 Q 155,50 150,45" fill="none" stroke="#22c55e" stroke-width="2" class="opacity-0 transition-opacity" />

              <!-- Face 3 target (lower branches left) -->
              <path d="M 60,130 Q 52,125 52,120 Q 55,116 58,118 Q 55,110 60,105" fill="none" stroke="transparent" stroke-width="8" class="face-target cursor-pointer" data-idx="3" />
              <path id="highlight-3" d="M 60,130 Q 52,125 52,120 Q 55,116 58,118 Q 55,110 60,105" fill="none" stroke="#22c55e" stroke-width="2" class="opacity-0 transition-opacity" />

              <!-- Face 4 target (lower branches right) -->
              <path d="M 140,130 Q 148,125 148,120 Q 145,116 142,118 Q 145,110 140,105" fill="none" stroke="transparent" stroke-width="8" class="face-target cursor-pointer" data-idx="4" />
              <path id="highlight-4" d="M 140,130 Q 148,125 148,120 Q 145,116 142,118 Q 145,110 140,105" fill="none" stroke="#22c55e" stroke-width="2" class="opacity-0 transition-opacity" />

              <!-- Face 5 target (ground root left) -->
              <path d="M 60,170 Q 50,165 50,160 M 50,160 Q 55,155 60,152" fill="none" stroke="transparent" stroke-width="8" class="face-target cursor-pointer" data-idx="5" />
              <path id="highlight-5" d="M 60,170 Q 50,165 50,160 M 50,160 Q 55,155 60,152" fill="none" stroke="#22c55e" stroke-width="2" class="opacity-0 transition-opacity" />

              <!-- Face 6 target (ground root right) -->
              <path d="M 140,170 Q 150,165 150,160 M 150,160 Q 145,155 140,152" fill="none" stroke="transparent" stroke-width="8" class="face-target cursor-pointer" data-idx="6" />
              <path id="highlight-6" d="M 140,170 Q 150,165 150,160 M 150,160 Q 145,155 140,152" fill="none" stroke="#22c55e" stroke-width="2" class="opacity-0 transition-opacity" />
            </svg>""",
            "controls": """<div class="flex flex-col sm:flex-row items-center justify-between w-full p-4 bg-slate-900/60 border border-slate-800 rounded-xl text-xs gap-3">
              <div class="font-bold">Faces found: <span class="faces-count text-green-400 text-sm">0</span> / 6</div>
              <div class="flex gap-2">
                <button class="reset-faces-btn bg-purple-600 hover:bg-purple-500 text-white font-bold px-3 py-1.5 rounded-lg">Reset 🔄</button>
              </div>
            </div>
            <p class="face-message hidden text-xs font-bold text-green-400 uppercase tracking-widest text-center">🎉 Amazing! You found all 6 faces!</p>""",
            "explanation": "The 6 Hidden Faces in Trees is a popular ambiguous puzzle that exploits the brain's tendency toward pareidolia—our natural urge to find human faces and familiar shapes in random patterns. The branches and trunks of the trees are drawn such that their negative spaces and bark contours trace the profiles of human faces. Because the brain's fusiform face area (FFA) is highly specialized to detect face configurations, it actively scans the forest outlines, assembling the profiles out of the raw branches. This shows how top-down face processing override works.",
            "min_h": "300px"
        },
        {
            "id": "skull-coffee",
            "slug": "skull-coffee",
            "difficulty": "🔴 Hard",
            "category": "Ambiguous",
            "title": "6. Coffee Skull",
            "desc": "A foam design on top of an espresso cup that creates a bistable interpretation of coffee froth vs a human skull.",
            "ins": "Observe the mug. Do you see the rich brown coffee froth forming a skull, or the white milk foam outlining two cups/saucers?",
            "svg": """<svg class="w-full h-full select-none" viewBox="0 0 200 200" id="svg-coffee-skull">
              <!-- Outer cup edge -->
              <circle cx="100" cy="100" r="80" fill="none" stroke="currentColor" stroke-width="3.5" class="text-slate-900 dark:text-slate-300" />
              <circle cx="100" cy="100" r="70" fill="url(#coffee-foam-grad)" />
              
              <!-- Skull eye cavities / Coffee pools -->
              <circle cx="80" cy="85" r="14" fill="#582f0e" />
              <circle cx="120" cy="85" r="14" fill="#582f0e" />
              <path d="M 92,110 L 108,110 L 100,122 Z" fill="#582f0e" /> <!-- Nose cavity -->
              
              <!-- Teeth dashes -->
              <line x1="88" y1="140" x2="88" y2="148" stroke="#582f0e" stroke-width="2" />
              <line x1="96" y1="140" x2="96" y2="148" stroke="#582f0e" stroke-width="2" />
              <line x1="104" y1="140" x2="104" y2="148" stroke="#582f0e" stroke-width="2" />
              <line x1="112" y1="140" x2="112" y2="148" stroke="#582f0e" stroke-width="2" />

              <defs>
                <radialGradient id="coffee-foam-grad" cx="50%" cy="50%" r="50%">
                  <stop offset="0%" stop-color="#ddb892" />
                  <stop offset="100%" stop-color="#ede0d4" />
                </radialGradient>
              </defs>
            </svg>""",
            "controls": """<div class="flex flex-wrap gap-3 justify-center">
              <button class="btn-vote bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs px-4 py-2.5 rounded-xl transition-all shadow" data-vote="coffee">Coffee Foam ☕</button>
              <button class="btn-vote bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs px-4 py-2.5 rounded-xl transition-all shadow" data-vote="skull">Skull 💀</button>
            </div>""",
            "explanation": "The Coffee Skull is a modern ambiguous figure where the foam patterns in a cup of coffee form a skull. The dark coffee liquid represents the empty eye sockets and nose cavity, while the surrounding light foam forms the bone structure and teeth. Like the Salvador Dalí and Charles Allan Gilbert skull illusions, this highlights how our visual system matches raw contrast boundaries to familiar cognitive templates. The brain toggles between seeing a cup of espresso and a human skull.",
            "min_h": "300px"
        },
        {
            "id": "hermann-grid",
            "slug": "hermann-grid",
            "difficulty": "🟡 Medium",
            "category": "Physiological",
            "title": "7. Hermann Grid Dots",
            "desc": "A grid layout of black tiles with gray intersections. Ghostly dark dots appear in your periphery, disappearing when you look at them.",
            "ins": "Look at the intersections of the white paths. Do you see dark spots flickering? Try to count them, or input your guess below.",
            "svg": """<svg class="w-full h-full select-none" viewBox="0 0 200 200" id="svg-hermann">
              <rect width="200" height="200" fill="#000000" />
              <!-- Grid lines -->
              <g stroke="#ffffff" stroke-width="12">
                <line x1="40" y1="0" x2="40" y2="200" />
                <line x1="80" y1="0" x2="80" y2="200" />
                <line x1="120" y1="0" x2="120" y2="200" />
                <line x1="160" y1="0" x2="160" y2="200" />
                
                <line x1="0" y1="40" x2="200" y2="40" />
                <line x1="0" y1="80" x2="200" y2="80" />
                <line x1="0" y1="120" x2="200" y2="120" />
                <line x1="0" y1="160" x2="200" y2="160" />
              </g>
            </svg>""",
            "controls": """<div class="flex flex-col sm:flex-row items-center justify-between w-full p-4 bg-slate-900/60 border border-slate-800 rounded-xl text-xs gap-3">
              <div class="flex items-center space-x-2 w-full">
                <label for="dots-count-input" class="font-bold shrink-0">How many dark dots? </label>
                <input type="number" id="dots-count-input" class="w-20 bg-slate-950 border border-slate-700 text-center font-bold text-white rounded p-1" value="0" />
              </div>
              <button id="submit-dots-btn" class="bg-purple-600 hover:bg-purple-500 text-white font-bold px-4 py-2 rounded-lg shrink-0">Submit</button>
            </div>
            <div id="dots-feedback-panel" class="hidden text-xs font-bold text-green-400 text-center uppercase tracking-wider" id="dots-feedback-title"></div>""",
            "explanation": "The Hermann Grid is a lateral inhibition illusion. Visual receptors in your retina compete with neighboring cells to process light. The intersections of white lines are flanked by white areas on four sides, while the straight path segments are flanked by black on only two sides. Consequently, the receptors processing the intersections receive more surround inhibition, causing them to signal less brightness to the brain, which creates the illusion of gray dots.",
            "min_h": "300px"
        },
        {
            "id": "spinning-dancer",
            "slug": "spinning-dancer",
            "difficulty": "🔴 Hard",
            "category": "Ambiguous",
            "title": "8. The Spinning Dancer",
            "desc": "A rotating silhouette whose direction of spin (clockwise or counter-clockwise) is entirely decided by your mind.",
            "ins": "Observe the dancer. Is she spinning clockwise on her left foot, or counter-clockwise on her right foot? Use the belt checkbox below to assist your focus.",
            "svg": """<div class="flex items-center justify-center w-full h-full" style="perspective: 600px;">
              <svg id="dancer-svg" class="dancer-svg w-32 h-44 text-slate-900 dark:text-slate-200" viewBox="0 0 200 200" style="transform-style: preserve-3d; animation: spin-dancer-scale 4s linear infinite;">
                <circle cx="100" cy="30" r="8" fill="currentColor" />
                <path d="M95,42 C92,60 92,80 96,95 L104,95 C108,80 108,60 105,42 Z" fill="currentColor" />
                <path class="dancer-left-limb" d="M96,44 Q65,42 40,35 Q65,48 96,49 Z M97,95 L97,165 C97,168 99,170 101,170 L101,95 Z" fill="currentColor" />
                <path class="dancer-right-limb" d="M104,44 Q135,42 160,35 Q135,48 104,49 Z M103,95 Q125,115 130,125 Q115,125 103,115 Z" fill="currentColor" />
                
                <!-- Helper colored belt -->
                <path id="dancer-belt" class="opacity-0 transition-opacity duration-300" d="M 96,94 L 104,94" stroke="#ec4899" stroke-width="4" stroke-linecap="round" />
              </svg>
            </div>""",
            "controls": """<div class="flex flex-wrap gap-4 items-center justify-between w-full p-4 bg-slate-900/60 border border-slate-800 rounded-xl text-xs">
              <label class="flex items-center space-x-2 cursor-pointer font-bold select-none">
                <input type="checkbox" id="dancer-belt-toggle" class="rounded border-slate-700 bg-slate-950 text-purple-650 accent-purple-650" />
                <span>Show Colored Reference Belt 🎗️</span>
              </label>
              <div class="flex gap-2">
                <button class="btn-vote bg-purple-600 hover:bg-purple-500 text-white font-bold px-3 py-1.5 rounded-lg" data-vote="cw">Clockwise ➡️</button>
                <button class="btn-vote bg-purple-600 hover:bg-purple-500 text-white font-bold px-3 py-1.5 rounded-lg" data-vote="ccw">Counter-Clockwise ⬅️</button>
              </div>
            </div>""",
            "explanation": "The Spinning Dancer is an ambiguous bistable illusion presenting a silhouette of a dancer. Because there is a lack of depth cues (no shadows, light reflections, or volumetric hints), the brain cannot determine whether the dancer is spinning clockwise on her left leg or counter-clockwise on her right leg. The visual cortex oscillates between two equally plausible 3D reconstructions.",
            "min_h": "300px"
        },
        {
            "id": "hidden-tiger",
            "slug": "hidden-tiger",
            "difficulty": "🟡 Medium",
            "category": "Ambiguous",
            "title": "9. Hidden Tiger",
            "desc": "A visual puzzle where the words 'the hidden tiger' are spelled out along the tiger's side stripes.",
            "ins": "Observe the stripes on the tiger's side. Can you read the words 'the hidden tiger' written in them? Click 'Reveal Outlines' to see them highlighted.",
            "svg": """<svg class="w-full h-full select-none bg-amber-500 rounded-2xl" viewBox="0 0 200 120" id="svg-tiger">
              <!-- Tiger body representation -->
              <ellipse cx="100" cy="60" rx="70" ry="40" fill="#f59e0b" stroke="#000000" stroke-width="2" />
              <!-- Head -->
              <circle cx="40" cy="50" r="24" fill="#f59e0b" stroke="#000000" stroke-width="2" />
              <circle cx="32" cy="45" r="3" fill="#000000" />
              <!-- Side stripes spelling out 'the hidden tiger' -->
              <path d="M 70,30 Q 75,50 72,70 M 80,25 Q 86,50 82,75 M 92,20 Q 98,60 94,90 M 110,22 Q 116,60 112,85 M 125,24 Q 130,55 127,82 M 140,28 Q 142,50 144,76" fill="none" stroke="#000000" stroke-width="3" />
              
              <g class="diagram-overlay opacity-0 transition-opacity duration-300">
                <!-- Highlighted stripes representing text -->
                <path d="M 70,30 Q 75,50 72,70 M 80,25 Q 86,50 82,75 M 92,20 Q 98,60 94,90" fill="none" stroke="#ef4444" stroke-width="4.5" />
                <text x="100" y="112" fill="#ef4444" font-size="10" font-weight="900" text-anchor="middle">Text in Stripes: T-H-E H-I-D-D-E-N T-I-G-E-R</text>
              </g>
            </svg>""",
            "controls": """<div class="flex flex-wrap gap-3 justify-center">
              <button class="btn-vote bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs px-4 py-2.5 rounded-xl transition-all shadow" data-vote="yes">I Read It! 📖</button>
              <button class="btn-vote bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs px-4 py-2.5 rounded-xl transition-all shadow" data-vote="no">No, Just Stripes 🦓</button>
              <button class="btn-reveal border border-purple-500/30 text-purple-400 hover:bg-purple-500/10 font-bold text-xs px-4 py-2.5 rounded-xl transition-all">Reveal Text</button>
            </div>""",
            "explanation": "The Hidden Tiger is a classic visual puzzle where a tiger is standing in a forest, but a second tiger is hidden in the stripes of the first tiger. Specifically, the words 'the hidden tiger' are spelled out along the tiger's side stripes. This illusion demonstrates how semantic text patterns can be hidden within natural biological patterns, requiring the visual cortex to switch from object/pattern recognition to text reading to solve the puzzle.",
            "min_h": "300px"
        },
        {
            "id": "impossible-elephant",
            "slug": "impossible-elephant",
            "difficulty": "🔴 Hard",
            "category": "Impossible",
            "title": "10. Impossible Elephant",
            "desc": "A classic impossible drawing of an elephant (also known as L'egs-istential Dread) containing a leg paradox.",
            "ins": "Observe the elephant's legs. How many legs does it have? Count them carefully. Click 'Reveal Highlights' to see why your brain gets confused.",
            "svg": """<svg class="w-full h-full select-none" viewBox="0 0 200 200" id="svg-elephant">
              <!-- Body outline -->
              <path d="M 50,60 C 50,40 160,40 160,70 L 160,110 C 160,110 150,115 140,110" fill="none" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-200" />
              <!-- 4 Leg connections from top body -->
              <line x1="60" y1="100" x2="60" y2="130" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-200" />
              <line x1="85" y1="100" x2="85" y2="130" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-200" />
              <line x1="110" y1="100" x2="110" y2="130" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-200" />
              <line x1="135" y1="100" x2="135" y2="130" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-200" />
              <!-- Hooves drawn out of sync at bottom -->
              <path d="M 50,160 Q 55,160 55,155 L 55,130" fill="none" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-200" />
              <path d="M 72,160 Q 77,160 77,155 L 77,130" fill="none" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-200" />
              <path d="M 97,160 Q 102,160 102,155 L 102,130" fill="none" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-200" />
              <path d="M 122,160 Q 127,160 127,155 L 127,130" fill="none" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-200" />
              <path d="M 147,160 Q 152,160 152,155 L 152,130" fill="none" stroke="currentColor" stroke-width="2.5" class="text-slate-900 dark:text-slate-200" />
              
              <!-- Bottom curves of hooves -->
              <circle cx="50" cy="160" r="3.5" class="fill-slate-900 dark:fill-slate-200" />
              <circle cx="72" cy="160" r="3.5" class="fill-slate-900 dark:fill-slate-200" />
              <circle cx="97" cy="160" r="3.5" class="fill-slate-900 dark:fill-slate-200" />
              <circle cx="122" cy="160" r="3.5" class="fill-slate-900 dark:fill-slate-200" />
              <circle cx="147" cy="160" r="3.5" class="fill-slate-900 dark:fill-slate-200" />

              <!-- Red highlight overlay pointing to spaces between legs -->
              <g class="diagram-overlay opacity-0 transition-opacity duration-300">
                <circle cx="68" cy="138" r="7" stroke="#ef4444" stroke-width="2" fill="none" />
                <circle cx="115" cy="138" r="7" stroke="#ef4444" stroke-width="2" fill="none" />
                <text x="100" y="180" fill="#ef4444" font-size="10" font-weight="900" text-anchor="middle">Spaces drawn as legs!</text>
              </g>
            </svg>""",
            "controls": """<div class="flex flex-wrap gap-3 justify-center">
              <button class="btn-vote bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs px-4 py-2.5 rounded-xl transition-all shadow" data-vote="four">4 Legs 🐘</button>
              <button class="btn-vote bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs px-4 py-2.5 rounded-xl transition-all shadow" data-vote="five">5 Legs 🐘</button>
              <button class="btn-reveal border border-purple-500/30 text-purple-400 hover:bg-purple-500/10 font-bold text-xs px-4 py-2.5 rounded-xl transition-all">Reveal Highlights</button>
            </div>""",
            "explanation": "The Impossible Elephant (also known as L'egs-istential Dread) is an impossible object created by cognitive scientist Roger Shepard. The drawing depicts an elephant with a normal body, but its legs and feet are drawn inconsistently. The blank space between its legs is drawn as feet, while the actual legs end in blank space. The brain tries to construct a 3D model of the elephant but experiences cognitive friction because the contour lines are shared between the positive shapes (legs) and negative spaces (gaps), leading to a paradox.",
            "min_h": "300px"
        }
    ]

    cards_html = ""
    for c in cards_data:
        cards_html += f"""
      <!-- Illusion {c['title']} -->
      <section class="illusion-container bg-white dark:bg-slate-900/40 rounded-3xl border border-slate-200 dark:border-slate-800 p-8 shadow-sm flex flex-col gap-6 max-w-[800px] w-full mx-auto relative overflow-hidden" data-id="{c['id']}">
        
        <!-- Header -->
        <div class="w-full space-y-4 text-center">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2">
              <span class="text-xs font-bold px-2 py-0.5 rounded bg-yellow-500/10 text-yellow-500 border border-yellow-500/25">{c['difficulty']}</span>
              <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">{c['category']}</span>
            </div>
            <button class="share-btn p-2 rounded-lg bg-slate-50 dark:bg-slate-800 text-slate-400 hover:text-purple-400 transition-colors z-20" data-name="{c['title'].split('.')[1].strip()}">
              <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M15 8a3 3 0 1 0-2.977-2.63l-4.94 2.47a3 3 0 1 0 0 4.319l4.94 2.47a3 3 0 1 0 .895-1.789l-4.94-2.47a3.027 3.027 0 0 0 0-.74l4.94-2.47C13.456 7.68 14.19 8 15 8Z"/></svg>
            </button>
          </div>
          
          <h2 class="font-display text-3xl font-black text-slate-900 dark:text-white">{c['title']}</h2>
          <p class="text-sm text-slate-650 dark:text-slate-400 max-w-xl mx-auto leading-relaxed font-semibold">
            {c['desc']}
          </p>
        </div>

        <!-- Highlighted Instruction Box -->
        <div class="w-full my-3 flex items-start gap-2 rounded-xl border border-indigo-500/10 bg-indigo-500/5 p-3 text-xs text-slate-350 text-left">
          <span class="text-base leading-none">👁️</span>
          <div>
            <strong class="text-slate-200">Instructions:</strong> {c['ins']}
          </div>
        </div>

        <!-- Visual Display -->
        <div class="w-full flex flex-col items-center justify-center bg-slate-150 dark:bg-slate-950/60 rounded-2xl p-6 border border-slate-200 dark:border-slate-800 min-h-[{c['min_h']}]">
          <div class="relative w-full max-w-[400px] h-[300px] flex items-center justify-center">
            {c['svg']}
          </div>
        </div>

        <!-- Controls, Voting, and Stopwatch Time Tracker -->
        <div class="w-full space-y-4 pt-2 flex flex-col items-center text-center">
          
          <!-- Time Tracker Bar -->
          <div class="w-full flex items-center justify-between p-3 bg-slate-50 dark:bg-slate-950 rounded-xl border border-slate-200 dark:border-slate-800 text-xs">
            <div class="flex items-center space-x-2">
              <button class="btn-spot bg-emerald-600 hover:bg-emerald-500 text-white font-bold px-3 py-1.5 rounded-lg">I See It! ⏱️</button>
              <span class="spot-time font-mono font-bold text-slate-700 dark:text-slate-300">0.0s</span>
            </div>
            <div class="text-slate-550 dark:text-slate-400 font-bold">
              Personal Best: <span class="pb-time font-mono text-purple-400">-.-s</span>
            </div>
          </div>

          <!-- Controls panel -->
          {c['controls']}

        </div>

        <!-- Collapsible Explanation -->
        <details class="w-full mt-4 border-t border-slate-800/40 pt-3 text-xs text-slate-400 select-none text-left">
          <summary class="font-bold cursor-pointer hover:text-purple-400">👁️ Reveal Answer & Science</summary>
          <p class="mt-2 font-normal leading-relaxed text-slate-400">
            {c['explanation']}
          </p>
        </details>

        <!-- Explore Link -->
        <div class="w-full mt-4 pt-4 border-t border-slate-500/10 flex justify-between items-center text-xs font-black text-purple-650 dark:text-purple-400 hover:text-purple-500 transition-colors">
          <span>Explore Full Science & Facts</span>
          <a href="/illusions/{c['slug']}" class="hover:underline">Explore &rarr;</a>
        </div>

      </section>
"""

    restructured_main = header_part + cards_html + "\n    </div>\n  </main>\n\n" + footer_part
    
    # Patch stopwatch Javascript inside footer_part to use the toFixed(1) delta method
    # Locate pageLoadTime and setInterval inside the script
    # Look at original timer function and replace
    old_timer_code = """    const startGlobalTimer = () => {
      const pageLoadTime = Date.now();
      
      setInterval(() => {
        const elapsedMs = Date.now() - pageLoadTime;
        const totalSeconds = Math.floor(elapsedMs / 1000);
        const minutes = Math.floor(totalSeconds / 60);
        const seconds = totalSeconds % 60;
        const timeStr = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        
        document.querySelectorAll('.spot-time').forEach(el => {
          if (!el.classList.contains('stopped')) {
            el.textContent = timeStr;
          }
        });
      }, 500);
    };"""

    new_timer_code = """    const startGlobalTimer = () => {
      const pageLoadTime = Date.now();
      
      setInterval(() => {
        const elapsedMs = Date.now() - pageLoadTime;
        const seconds = (elapsedMs / 1000).toFixed(1);
        const timeStr = `${seconds}s`;
        
        document.querySelectorAll('.spot-time').forEach(el => {
          if (!el.classList.contains('stopped')) {
            el.textContent = timeStr;
          }
        });
      }, 100);
    };"""

    restructured_main = restructured_main.replace(old_timer_code, new_timer_code)

    # Change loadPersonalBests local storage key from pb-hidden- to pb-hidden-1-
    # and default time values
    restructured_main = restructured_main.replace('"00:00"', '"0.0s"')
    restructured_main = restructured_main.replace("pbEl.textContent = pb;", "pbEl.textContent = pb;")
    restructured_main = restructured_main.replace("const spotTime = spotTimeEl.textContent || \"00:00\";", "const spotTime = spotTimeEl.textContent || \"0.0s\";")
    
    with open(hidden_path, "w", encoding="utf-8") as f:
        f.write(restructured_main)
    print("hidden.astro successfully restructured to single-column layout with stopwatch delta patch!")
else:
    print("hidden.astro path error.")

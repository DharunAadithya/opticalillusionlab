import re

# Read famous.astro
file_path = "src/pages/famous.astro"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define mapping for existing cards
# (id, category, difficulty, difficulty-level, year)
mappings = {
    "dancer-illusion": ("Ambiguous", "medium", "2", "2003"),
    "rubin-illusion": ("Ambiguous", "easy", "1", "1915"),
    "penrose-illusion": ("Impossible", "hard", "3", "1958"),
    "dress-illusion": ("Color", "easy", "1", "2015"),
    "muller-illusion": ("Geometric", "easy", "1", "1889"),
    "cafe-illusion": ("Geometric", "medium", "2", "1898"),
    "necker-illusion": ("Ambiguous", "easy", "1", "1832"),
    "kanizsa-illusion": ("Geometric", "easy", "1", "1955"),
    "ponzo-illusion": ("Geometric", "easy", "1", "1911"),
    "zoellner-illusion": ("Geometric", "medium", "2", "1860"),
    "ames-illusion": ("Geometric", "hard", "3", "1946"),
    "hollow-illusion": ("Ambiguous", "hard", "3", "1970"),
    "snakes-illusion": ("Motion", "medium", "2", "2003"),
    "fraser-illusion": ("Geometric", "hard", "3", "1908"),
    "hermann-illusion": ("Physiological", "medium", "2", "1870")
}

# 1. Inject attributes into existing card anchor tags
for cid, (cat, diff, diff_level, year) in mappings.items():
    pattern = rf'id="{cid}"'
    replacement = f'id="{cid}" data-category="{cat}" data-difficulty="{diff}" data-difficulty-level="{diff_level}" data-year="{year}"'
    content = re.sub(pattern, replacement, content)

# 2. Add filters and sort HTML right before the cards grid starts
grid_start_pattern = r'(<!-- The 15 Illusion Cards Grid -->\s*<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">)'
filters_html = """<!-- Filters and Sort controls -->
    <div class="flex flex-col md:flex-row items-center justify-between gap-4 mt-6 p-4 bg-slate-50 dark:bg-slate-900/40 border border-indigo-500/10 rounded-2xl">
      <!-- Filter buttons -->
      <div class="flex flex-wrap gap-2" id="famous-filters">
        <button data-filter="all" class="filter-btn text-xs font-bold px-3 py-1.5 rounded-lg bg-purple-650 text-white transition-all shadow-sm">All</button>
        <button data-filter="Geometric" class="filter-btn text-xs font-bold px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:text-white transition-all">Geometric</button>
        <button data-filter="Color" class="filter-btn text-xs font-bold px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:text-white transition-all">Color</button>
        <button data-filter="Motion" class="filter-btn text-xs font-bold px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:text-white transition-all">Motion</button>
        <button data-filter="Ambiguous" class="filter-btn text-xs font-bold px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:text-white transition-all">Ambiguous</button>
        <button data-filter="Impossible" class="filter-btn text-xs font-bold px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:text-white transition-all">Impossible</button>
        <button data-filter="Physiological" class="filter-btn text-xs font-bold px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:text-white transition-all">Physiological</button>
      </div>

      <!-- Sort dropdown -->
      <div class="flex items-center space-x-2">
        <label for="famous-sort" class="text-xs font-bold text-slate-400">Sort by:</label>
        <select id="famous-sort" class="bg-slate-800 border border-slate-700 text-slate-200 text-xs rounded-lg px-2.5 py-1.5 focus:outline-none focus:border-purple-500 transition-colors">
          <option value="popular">Most Popular</option>
          <option value="newest">Newest</option>
          <option value="hardest">Hardest</option>
          <option value="easiest">Easiest</option>
        </select>
      </div>
    </div>

    <!-- The 15 Illusion Cards Grid -->
    <div id="famous-gallery-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">"""

content = re.sub(r'<!-- The 15 Illusion Cards Grid -->\s*<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">', filters_html, content)

# 3. Add the 5 new cards just before the closing </div> of the cards grid (which is right before FAQ section)
# We can find card 15 end a tag, which is followed by:
#         </div>
#       </a>
# 
#     </div>
#   </section>
# 
#   <!-- FAQ Section Accordion -->

new_cards_html = """      <!-- Card 16: Penrose Stairs -->
      <div id="stairs-illusion" data-category="Impossible" data-difficulty="hard" data-difficulty-level="3" data-year="1958" class="illusion-card flex flex-col justify-between rounded-2xl border border-indigo-100/10 bg-white dark:bg-[#1a1a2e] backdrop-blur-sm p-6 shadow-xl relative group">
        <button class="share-btn absolute top-6 right-6 p-2 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-400 hover:text-slate-200 border border-slate-500/10 transition-colors z-20" aria-label="Share this illusion">
          <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M15 8a3 3 0 1 0-2.977-2.63l-4.94 2.47a3 3 0 1 0 0 4.319l4.94 2.47a3 3 0 1 0 .895-1.789l-4.94-2.47a3.027 3.027 0 0 0 0-.74l4.94-2.47C13.456 7.68 14.19 8 15 8Z"/></svg>
          <span class="share-toast absolute bottom-full right-0 mb-2 px-2.5 py-1 text-[10px] font-bold text-white bg-purple-600 rounded-lg shadow-md opacity-0 pointer-events-none transition-opacity duration-200 whitespace-nowrap">Link Copied! ✓</span>
        </button>
        <div>
          <h3 class="font-display text-xl font-bold text-slate-900 dark:text-white mb-1 flex flex-col xs:flex-row xs:items-center gap-2 pr-10">
            <span>Penrose Stairs</span>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-rose-500/10 text-rose-500 border border-rose-500/20 w-fit">🔴 Hard</span>
          </h3>
          <div class="text-[10px] font-bold text-indigo-400 uppercase tracking-wide mb-2">Category: Impossible Objects</div>
          <p class="text-xs text-slate-600 dark:text-slate-400 mb-6">
            You can climb these stairs forever and never get higher. Inspired M.C. Escher's Ascending and Descending (1960).
          </p>
        </div>
        <div class="demo-area relative flex flex-col items-center justify-center h-64 w-full bg-slate-100 dark:bg-slate-950/40 rounded-xl overflow-hidden border border-indigo-500/5">
          <svg class="w-full h-44 p-2 select-none" viewBox="0 0 200 200">
            <!-- Isometric Stairs loop -->
            <g transform="translate(100, 105) scale(0.85)" stroke="currentColor" stroke-width="2.5" fill="none" class="text-slate-900 dark:text-slate-200">
              <!-- Top Left Stairs -->
              <path d="M -40,-40 L -20,-30 L -20,-50 L 0,-40 L 0,-60 L 20,-50 M -40,-20 L -40,-40" />
              <!-- Top Right Stairs -->
              <path d="M 20,-50 L 40,-40 L 40,-20 L 20,-30 M 40,-40 L 60,-30 L 60,-10 L 40,-20" />
              <!-- Bottom Right Stairs -->
              <path d="M 60,-10 L 40,0 L 40,20 L 60,10 M 40,0 L 20,10 L 20,30 L 40,20" />
              <!-- Bottom Left Stairs -->
              <path d="M 20,30 L -20,10 L -20,-10 L -40,-20 L -40,-40 M -20,10 L 0,0 L 0,-20 L 20,-10" />
            </g>
            <!-- Walking dot -->
            <circle id="stairs-dot" cx="100" cy="100" r="5" fill="#ef4444" />
          </svg>
          <div class="absolute bottom-2 w-11/12 px-4 flex flex-col space-y-1 bg-white/80 dark:bg-slate-900/80 p-2 rounded-xl border border-slate-250">
            <div class="flex items-center justify-between text-[9px] text-slate-500 font-bold uppercase">
              <span>Walking Speed</span>
            </div>
            <input type="range" min="1" max="10" value="5" id="stairs-speed-slider" class="w-full h-1 bg-slate-200 dark:bg-slate-800 rounded-lg appearance-none cursor-pointer accent-purple-600 focus:outline-none" />
          </div>
        </div>
        <div class="mt-3 text-[11px] text-slate-500 dark:text-slate-400">
          <strong>Discoverer:</strong> Lionel & Roger Penrose (1958)
        </div>
        <details class="mt-4 border-t border-slate-500/10 pt-3 text-xs text-slate-600 dark:text-slate-400">
          <summary class="font-bold cursor-pointer hover:text-purple-500 dark:hover:text-purple-400 transition-colors select-none">🔬 Why it works</summary>
          <p class="mt-2 leading-relaxed font-normal">
            The Penrose Stairs is a 2D depiction of a staircase in which the stairs make four 90-degree turns as they ascent or descent yet form a continuous loop. This represents a geometric impossibility in three-dimensional space, where each step should change height. The brain's visual system processes local details (each individual step looks normal and consistent) and assumes they connect globally, creating a perpetual motion loop that contradicts standard gravity.
          </p>
        </details>
        <div class="mt-5 flex items-center justify-between text-xs font-bold text-purple-600 dark:text-purple-400 group-hover:text-purple-500 transition-colors">
          <a href="/illusions/penrose-stairs" class="hover:underline">View Full Science & Facts</a>
        </div>
      </div>

      <!-- Card 17: Shepard Tables -->
      <div id="shepard-illusion" data-category="Geometric" data-difficulty="medium" data-difficulty-level="2" data-year="1990" class="illusion-card flex flex-col justify-between rounded-2xl border border-indigo-100/10 bg-white dark:bg-slate-900/60 backdrop-blur-sm p-6 shadow-xl relative group">
        <button class="share-btn absolute top-6 right-6 p-2 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-400 hover:text-slate-200 border border-slate-500/10 transition-colors z-20" aria-label="Share this illusion">
          <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M15 8a3 3 0 1 0-2.977-2.63l-4.94 2.47a3 3 0 1 0 0 4.319l4.94 2.47a3 3 0 1 0 .895-1.789l-4.94-2.47a3.027 3.027 0 0 0 0-.74l4.94-2.47C13.456 7.68 14.19 8 15 8Z"/></svg>
          <span class="share-toast absolute bottom-full right-0 mb-2 px-2.5 py-1 text-[10px] font-bold text-white bg-purple-600 rounded-lg shadow-md opacity-0 pointer-events-none transition-opacity duration-200 whitespace-nowrap">Link Copied! ✓</span>
        </button>
        <div>
          <h3 class="font-display text-xl font-bold text-slate-900 dark:text-white mb-1 flex flex-col xs:flex-row xs:items-center gap-2 pr-10">
            <span>Shepard Tables</span>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-amber-500/10 text-amber-500 border border-amber-500/20 w-fit">🟡 Medium</span>
          </h3>
          <div class="text-[10px] font-bold text-indigo-400 uppercase tracking-wide mb-2">Category: Geometric</div>
          <p class="text-xs text-slate-600 dark:text-slate-400 mb-6">
            Two tabletops appearing completely different sizes. In reality, their 2D shapes are identical parallelograms.
          </p>
        </div>
        <div class="demo-area relative flex flex-col items-center justify-center h-64 w-full bg-slate-100 dark:bg-slate-950/40 rounded-xl overflow-hidden border border-indigo-500/5">
          <svg class="w-full h-44 p-2 select-none overflow-visible" viewBox="0 0 200 200">
            <!-- Table 1 (Left, vertical orientation) -->
            <g id="table-left" transform="translate(10, 0)">
              <!-- Legs -->
              <line x1="30" y1="100" x2="30" y2="150" stroke="#78350f" stroke-width="6" />
              <line x1="80" y1="100" x2="80" y2="150" stroke="#78350f" stroke-width="6" />
              <line x1="60" y1="120" x2="60" y2="160" stroke="#78350f" stroke-width="6" />
              <!-- Top parallelogram -->
              <polygon points="30,70 80,70 60,120 10,120" fill="#d97706" stroke="#b45309" stroke-width="2" />
            </g>
            <!-- Table 2 (Right, horizontal orientation) -->
            <g id="table-right" class="transition-transform duration-[1500ms] ease-in-out">
              <!-- Legs -->
              <line x1="120" y1="90" x2="120" y2="140" stroke="#78350f" stroke-width="6" />
              <line x1="170" y1="100" x2="170" y2="150" stroke="#78350f" stroke-width="6" />
              <line x1="140" y1="110" x2="140" y2="155" stroke="#78350f" stroke-width="6" />
              <!-- Top parallelogram (Identical shape rotated) -->
              <!-- Tabletop itself will be translated to Table 1 to check -->
              <polygon id="tabletop-right" points="100,80 150,80 130,130 80,130" fill="#d97706" stroke="#b45309" stroke-width="2" class="transition-transform duration-[1500ms] ease-in-out origin-center" style="transform-origin: 115px 105px;" />
            </g>
          </svg>
          <div class="absolute bottom-3">
            <button id="btn-overlay-shepard" class="text-[10px] font-semibold px-2.5 py-1.5 rounded-lg bg-purple-600 hover:bg-purple-500 text-white shadow-md transition-colors">
              Verify (Overlay Tables)
            </button>
          </div>
        </div>
        <div class="mt-3 text-[11px] text-slate-500 dark:text-slate-400">
          <strong>Discoverer:</strong> Roger Shepard (1990)
        </div>
        <details class="mt-4 border-t border-slate-500/10 pt-3 text-xs text-slate-600 dark:text-slate-400">
          <summary class="font-bold cursor-pointer hover:text-purple-500 dark:hover:text-purple-400 transition-colors select-none">🔬 Why it works</summary>
          <p class="mt-2 leading-relaxed font-normal">
            One of the most shocking geometric illusions ever created. The two tabletop parallelograms have the exact same size and shape on the page, yet the left tabletop looks long and narrow while the right looks almost square. The brain interprets the 2D drawings as 3D objects with depth. It automatically scales the shapes depending on their orientation to account for perspective, leading us to perceive completely different surface dimensions.
          </p>
        </details>
        <div class="mt-5 flex items-center justify-between text-xs font-bold text-purple-600 dark:text-purple-400 group-hover:text-purple-500 transition-colors">
          <a href="/illusions/shepard-tables" class="hover:underline">View Full Science & Facts</a>
        </div>
      </div>

      <!-- Card 18: Coffer Illusion -->
      <div id="coffer-illusion" data-category="Geometric" data-difficulty="hard" data-difficulty-level="3" data-year="2006" class="illusion-card flex flex-col justify-between rounded-2xl border border-indigo-100/10 bg-white dark:bg-slate-900/60 backdrop-blur-sm p-6 shadow-xl relative group">
        <button class="share-btn absolute top-6 right-6 p-2 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-400 hover:text-slate-200 border border-slate-500/10 transition-colors z-20" aria-label="Share this illusion">
          <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M15 8a3 3 0 1 0-2.977-2.63l-4.94 2.47a3 3 0 1 0 0 4.319l4.94 2.47a3 3 0 1 0 .895-1.789l-4.94-2.47a3.027 3.027 0 0 0 0-.74l4.94-2.47C13.456 7.68 14.19 8 15 8Z"/></svg>
          <span class="share-toast absolute bottom-full right-0 mb-2 px-2.5 py-1 text-[10px] font-bold text-white bg-purple-600 rounded-lg shadow-md opacity-0 pointer-events-none transition-opacity duration-200 whitespace-nowrap">Link Copied! ✓</span>
        </button>
        <div>
          <h3 class="font-display text-xl font-bold text-slate-900 dark:text-white mb-1 flex flex-col xs:flex-row xs:items-center gap-2 pr-10">
            <span>Coffer Illusion</span>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-rose-500/10 text-rose-500 border border-rose-500/20 w-fit">🔴 Hard</span>
          </h3>
          <div class="text-[10px] font-bold text-indigo-400 uppercase tracking-wide mb-2">Category: Geometric</div>
          <p class="text-xs text-slate-600 dark:text-slate-400 mb-6">
            A grid of rectangular panels/coffers. 16 circles are hidden in the image, but almost nobody sees them at first.
          </p>
        </div>
        <div class="demo-area relative flex flex-col items-center justify-center h-64 w-full bg-slate-100 dark:bg-slate-950/40 rounded-xl overflow-hidden border border-indigo-500/5">
          <svg class="w-44 h-44 select-none" viewBox="0 0 160 160">
            <!-- Draw grid lines with diagonals that imply coffers or circles -->
            <rect x="0" y="0" width="160" height="160" fill="#7f7f7f" />
            <!-- Vertical and horizontal grooves -->
            <g stroke="#ffffff" stroke-width="1.5">
              <line x1="40" y1="0" x2="40" y2="160" />
              <line x1="80" y1="0" x2="80" y2="160" />
              <line x1="120" y1="0" x2="120" y2="160" />
              <line x1="0" y1="40" x2="160" y2="40" />
              <line x1="0" y1="80" x2="160" y2="80" />
              <line x1="0" y1="120" x2="160" y2="120" />
            </g>
            <g stroke="#000000" stroke-width="1.5">
              <line x1="20" y1="0" x2="20" y2="160" stroke-dasharray="4,4" />
              <line x1="60" y1="0" x2="60" y2="160" stroke-dasharray="4,4" />
              <line x1="100" y1="0" x2="100" y2="160" stroke-dasharray="4,4" />
              <line x1="140" y1="0" x2="140" y2="160" stroke-dasharray="4,4" />
            </g>
            <!-- Circular outlines that are hidden by details -->
            <g class="coffer-circles opacity-0 transition-opacity duration-300">
              <circle cx="20" cy="20" r="16" fill="none" stroke="#ef4444" stroke-width="3" />
              <circle cx="60" cy="20" r="16" fill="none" stroke="#ef4444" stroke-width="3" />
              <circle cx="100" cy="20" r="16" fill="none" stroke="#ef4444" stroke-width="3" />
              <circle cx="140" cy="20" r="16" fill="none" stroke="#ef4444" stroke-width="3" />
              <circle cx="20" cy="60" r="16" fill="none" stroke="#ef4444" stroke-width="3" />
              <circle cx="60" cy="60" r="16" fill="none" stroke="#ef4444" stroke-width="3" />
              <circle cx="100" cy="60" r="16" fill="none" stroke="#ef4444" stroke-width="3" />
              <circle cx="140" cy="60" r="16" fill="none" stroke="#ef4444" stroke-width="3" />
              <circle cx="20" cy="100" r="16" fill="none" stroke="#ef4444" stroke-width="3" />
              <circle cx="60" cy="100" r="16" fill="none" stroke="#ef4444" stroke-width="3" />
              <circle cx="100" cy="100" r="16" fill="none" stroke="#ef4444" stroke-width="3" />
              <circle cx="140" cy="100" r="16" fill="none" stroke="#ef4444" stroke-width="3" />
              <circle cx="20" cy="140" r="16" fill="none" stroke="#ef4444" stroke-width="3" />
              <circle cx="60" cy="140" r="16" fill="none" stroke="#ef4444" stroke-width="3" />
              <circle cx="100" cy="140" r="16" fill="none" stroke="#ef4444" stroke-width="3" />
              <circle cx="140" cy="140" r="16" fill="none" stroke="#ef4444" stroke-width="3" />
            </g>
          </svg>
          <div class="absolute bottom-2 w-11/12 px-4 flex flex-col items-center bg-white/80 dark:bg-slate-900/80 p-2 rounded-xl backdrop-blur-sm border border-slate-200 dark:border-white/5 space-y-1">
            <div class="flex items-center justify-between w-full text-[9px] text-slate-500 font-bold uppercase">
              <span>Find Circles:</span>
            </div>
            <div class="flex w-full space-x-1">
              <input type="number" id="input-coffer-guess" class="bg-slate-950 border border-slate-700 text-white rounded text-[10px] px-1 w-12 focus:outline-none" placeholder="0" />
              <button id="btn-coffer-check" class="bg-purple-650 hover:bg-purple-500 text-white font-bold text-[9px] px-2 py-0.5 rounded flex-1">Check</button>
            </div>
          </div>
        </div>
        <div class="mt-3 text-[11px] text-slate-500 dark:text-slate-400">
          <strong>Discoverer:</strong> Anthony Norcia (2006)
        </div>
        <details class="mt-4 border-t border-slate-500/10 pt-3 text-xs text-slate-600 dark:text-slate-400">
          <summary class="font-bold cursor-pointer hover:text-purple-500 dark:hover:text-purple-400 transition-colors select-none">🔬 Why it works</summary>
          <p class="mt-2 leading-relaxed font-normal">
            The Coffer Illusion contains 16 circles that are fully present but disguised by the dominant horizontal and vertical lines which define the "coffers" (sunken rectangular panels). The brain strongly groups the straight, intersecting lines as rectangular frames, grouping them as 3D panels. This layout suppresses the circular contours, preventing the circular grouping until your focus shifts specifically to the intersections.
          </p>
        </details>
        <div class="mt-5 flex items-center justify-between text-xs font-bold text-purple-600 dark:text-purple-400 group-hover:text-purple-500 transition-colors">
          <a href="/illusions/coffer-illusion" class="hover:underline">View Full Science & Facts</a>
        </div>
      </div>

      <!-- Card 19: Vertical-Horizontal Illusion -->
      <div id="v-h-illusion" data-category="Geometric" data-difficulty="easy" data-difficulty-level="1" data-year="1858" class="illusion-card flex flex-col justify-between rounded-2xl border border-indigo-100/10 bg-white dark:bg-[#1a1a2e] backdrop-blur-sm p-6 shadow-xl relative group">
        <button class="share-btn absolute top-6 right-6 p-2 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-400 hover:text-slate-200 border border-slate-500/10 transition-colors z-20" aria-label="Share this illusion">
          <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M15 8a3 3 0 1 0-2.977-2.63l-4.94 2.47a3 3 0 1 0 0 4.319l4.94 2.47a3 3 0 1 0 .895-1.789l-4.94-2.47a3.027 3.027 0 0 0 0-.74l4.94-2.47C13.456 7.68 14.19 8 15 8Z"/></svg>
          <span class="share-toast absolute bottom-full right-0 mb-2 px-2.5 py-1 text-[10px] font-bold text-white bg-purple-600 rounded-lg shadow-md opacity-0 pointer-events-none transition-opacity duration-200 whitespace-nowrap">Link Copied! ✓</span>
        </button>
        <div>
          <h3 class="font-display text-xl font-bold text-slate-900 dark:text-white mb-1 flex flex-col xs:flex-row xs:items-center gap-2 pr-10">
            <span>Vertical-Horizontal</span>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-500 border border-emerald-500/20 w-fit">🟢 Easy</span>
          </h3>
          <div class="text-[10px] font-bold text-indigo-400 uppercase tracking-wide mb-2">Category: Geometric</div>
          <p class="text-xs text-slate-600 dark:text-slate-400 mb-6">
            A vertical line appears up to 20% longer than a horizontal line of the exact same length. Rotate to verify.
          </p>
        </div>
        <div class="demo-area relative flex flex-col items-center justify-center h-64 w-full bg-slate-100 dark:bg-slate-950/40 rounded-xl overflow-hidden border border-indigo-500/5">
          <svg class="w-full h-44 select-none overflow-visible" viewBox="0 0 200 200">
            <!-- Horizontal base line -->
            <line x1="40" y1="120" x2="160" y2="120" stroke="#3b82f6" stroke-width="4" />
            <!-- Vertical line (identical length 120px) -->
            <line id="vh-vertical" x1="100" y1="120" x2="100" y2="0" stroke="#ef4444" stroke-width="4" class="transition-transform duration-1000 origin-bottom" style="transform-origin: 100px 120px;" />
          </svg>
          <div class="absolute bottom-3">
            <button id="btn-rotate-vh" class="text-[10px] font-semibold px-2.5 py-1.5 rounded-lg bg-purple-600 hover:bg-purple-500 text-white shadow-md transition-colors">
              Rotate to Compare
            </button>
          </div>
        </div>
        <div class="mt-3 text-[11px] text-slate-500 dark:text-slate-400">
          <strong>Discoverer:</strong> Wilhelm Wundt (1858)
        </div>
        <details class="mt-4 border-t border-slate-500/10 pt-3 text-xs text-slate-600 dark:text-slate-400">
          <summary class="font-bold cursor-pointer hover:text-purple-500 dark:hover:text-purple-400 transition-colors select-none">🔬 Why it works</summary>
          <p class="mt-2 leading-relaxed font-normal">
            The vertical-horizontal illusion is one of the oldest known visual distortions. A vertical line appears roughly 15% to 20% longer than an identical horizontal line. This is partly because our binocular visual field is horizontal (wide) rather than vertical, so tracing vertical lines requires more effort from our eye muscles. The brain interprets this muscular effort as a greater physical distance.
          </p>
        </details>
        <div class="mt-5 flex items-center justify-between text-xs font-bold text-purple-600 dark:text-purple-400 group-hover:text-purple-500 transition-colors">
          <a href="/illusions/vertical-horizontal" class="hover:underline">View Full Science & Facts</a>
        </div>
      </div>

      <!-- Card 20: McGurk Effect -->
      <div id="mcgurk-illusion" data-category="Physiological" data-difficulty="medium" data-difficulty-level="2" data-year="1976" class="illusion-card flex flex-col justify-between rounded-2xl border border-indigo-100/10 bg-white dark:bg-slate-900/60 backdrop-blur-sm p-6 shadow-xl relative group">
        <button class="share-btn absolute top-6 right-6 p-2 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-400 hover:text-slate-200 border border-slate-500/10 transition-colors z-20" aria-label="Share this illusion">
          <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 20 20"><path d="M15 8a3 3 0 1 0-2.977-2.63l-4.94 2.47a3 3 0 1 0 0 4.319l4.94 2.47a3 3 0 1 0 .895-1.789l-4.94-2.47a3.027 3.027 0 0 0 0-.74l4.94-2.47C13.456 7.68 14.19 8 15 8Z"/></svg>
          <span class="share-toast absolute bottom-full right-0 mb-2 px-2.5 py-1 text-[10px] font-bold text-white bg-purple-600 rounded-lg shadow-md opacity-0 pointer-events-none transition-opacity duration-200 whitespace-nowrap">Link Copied! ✓</span>
        </button>
        <div>
          <h3 class="font-display text-xl font-bold text-slate-900 dark:text-white mb-1 flex flex-col xs:flex-row xs:items-center gap-2 pr-10">
            <span>McGurk Effect</span>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-amber-500/10 text-amber-500 border border-amber-500/20 w-fit">🟡 Medium</span>
          </h3>
          <div class="text-[10px] font-bold text-indigo-400 uppercase tracking-wide mb-2">Category: Physiological</div>
          <p class="text-xs text-slate-600 dark:text-slate-400 mb-6">
            Visual mouth movements override the auditory signal, making you hear "DA" instead of the actual audio "BA".
          </p>
        </div>
        <div class="demo-area relative flex flex-col items-center justify-center h-64 w-full bg-slate-100 dark:bg-slate-950/40 rounded-xl overflow-hidden border border-indigo-500/5 p-4 space-y-4">
          <!-- Mouth sync SVG -->
          <svg class="w-32 h-20 select-none overflow-visible" viewBox="0 0 100 60">
            <!-- Mouth outline -->
            <path id="mcgurk-lips" d="M 10,30 Q 50,15 90,30 Q 50,45 10,30 Z" fill="#f43f5e" stroke="#db2777" stroke-width="2" />
            <!-- Teeth & Tongue -->
            <rect id="mcgurk-teeth" x="30" y="25" width="40" height="4" fill="#ffffff" class="opacity-0 transition-opacity" />
            <path id="mcgurk-tongue" d="M 35,33 Q 50,25 65,33 Z" fill="#fda4af" class="opacity-0 transition-opacity" />
          </svg>
          
          <button id="btn-play-mcgurk" class="text-[10px] font-semibold px-2.5 py-1.5 rounded-lg bg-purple-600 hover:bg-purple-500 text-white shadow-md transition-colors flex items-center space-x-1">
            <span>🔊 Play Video & Audio</span>
          </button>

          <!-- Vote controls -->
          <div class="flex items-center space-x-2 bg-slate-900/95 border border-white/10 rounded-lg p-0.5 text-[9px] text-slate-350">
            <button data-vote-mc="ba" class="btn-mc-vote px-2 py-0.5 rounded hover:text-white">BA</button>
            <button data-vote-mc="ga" class="btn-mc-vote px-2 py-0.5 rounded hover:text-white">GA</button>
            <button data-vote-mc="da" class="btn-mc-vote px-2 py-0.5 rounded hover:text-white">DA</button>
          </div>
          
          <div id="mcgurk-feedback" class="hidden text-[10px] font-bold text-center bg-purple-500/10 border border-purple-500/20 p-2 rounded max-w-[95%] text-slate-300">
            "If you heard DA, your brain merged both signals! Now close your eyes and listen again — you'll hear BA!"
          </div>
        </div>
        <div class="mt-3 text-[11px] text-slate-500 dark:text-slate-400">
          <strong>Discoverer:</strong> Harry McGurk & John MacDonald (1976)
        </div>
        <details class="mt-4 border-t border-slate-500/10 pt-3 text-xs text-slate-600 dark:text-slate-400">
          <summary class="font-bold cursor-pointer hover:text-purple-500 dark:hover:text-purple-400 transition-colors select-none">🔬 Why it works</summary>
          <p class="mt-2 leading-relaxed font-normal">
            The McGurk Effect is a powerful audio-visual illusion showing how visual speech inputs alter auditory speech perception. When the mouth is seen speaking "GA" (velar consonant) but the audio track says "BA" (bilabial consonant), the brain integrates the conflicting visual and auditory streams to perceive "DA" (alveolar consonant), which is a fusion of the two coordinates. This proves that speech perception is multimodal.
          </p>
        </details>
        <div class="mt-5 flex items-center justify-between text-xs font-bold text-purple-600 dark:text-purple-400 group-hover:text-purple-500 transition-colors">
          <a href="/illusions/mcgurk-effect" class="hover:underline">View Full Science & Facts</a>
        </div>
      </div>
"""

# Append new cards HTML before FAQ section closing section tag
cards_pattern = r'(\s*<!-- Card 15: Hermann Grid -->.*?</a>\s*)(\s*</div>\s*</section>\s*<!-- FAQ Section Accordion -->)'
match = re.search(cards_pattern, content, re.DOTALL)
if match:
    # Inject new cards
    replacement = match.group(1) + new_cards_html + "\n\n" + match.group(2)
    content = content.replace(match.group(0), replacement)
    print("New cards HTML appended successfully.")
else:
    # Fallback to general cards grid end replacing
    print("Cards pattern not found, trying fallback...")
    content = content.replace("<!-- Card 15: Hermann Grid -->", "<!-- Card 15: Hermann Grid -->\n" + new_cards_html)

# 4. Add the Javascript code for new cards, filters, and sorting
# We will append the new scripts right before the closing </script> in famous.astro
js_code = """
    // ----------------------------------------------------
    // 5 NEW CARDS INTERACTIVITY SCRIPTS
    // ----------------------------------------------------

    // 16. Penrose Stairs
    const stairsContainer = document.getElementById('stairs-illusion');
    const stairsSpeedSlider = document.getElementById('stairs-speed-slider') as HTMLInputElement;
    const stairsDot = document.getElementById('stairs-dot');
    
    let stairsStep = 0;
    // Walk loop coordinates around the isometric loop
    const stairsPoints = [
      {cx: 100, cy: 55}, // top
      {cx: 120, cy: 65},
      {cx: 140, cy: 75}, // right turn
      {cx: 120, cy: 85},
      {cx: 100, cy: 95}, // bottom right
      {cx: 80, cy: 105}, // bottom left
      {cx: 60, cy: 95},
      {cx: 80, cy: 75}  // top left
    ];

    let stairsInterval: any = null;
    const runStairsAnimation = () => {
      if (stairsInterval) clearInterval(stairsInterval);
      const speed = stairsSpeedSlider ? parseInt(stairsSpeedSlider.value) : 5;
      const intervalMs = Math.max(100, 1000 - (speed * 90)); // 100ms to 910ms
      
      stairsInterval = setInterval(() => {
        stairsStep = (stairsStep + 1) % stairsPoints.length;
        const pt = stairsPoints[stairsStep];
        if (stairsDot) {
          stairsDot.setAttribute('cx', pt.cx.toString());
          stairsDot.setAttribute('cy', pt.cy.toString());
        }
      }, intervalMs);
    };

    stairsSpeedSlider?.addEventListener('input', () => {
      runStairsAnimation();
    });
    runStairsAnimation();

    // 17. Shepard Tables
    const shepardContainer = document.getElementById('shepard-illusion');
    const btnOverlayShepard = document.getElementById('btn-overlay-shepard');
    const tabletopRight = document.getElementById('tabletop-right');
    let shepardOverlayActive = false;

    btnOverlayShepard?.addEventListener('click', (e) => {
      e.stopPropagation();
      shepardOverlayActive = !shepardOverlayActive;
      if (tabletopRight) {
        if (shepardOverlayActive) {
          // Slide left by 90px, rotate to match orientation (rotate -60deg or so)
          // Table 1 parallelogram left is at cx=45, Table 2 tabletop-right is at cx=115
          // Rotate it from horizontal table representation to vertical tabletop shape
          tabletopRight.style.transform = 'translate(-80px, 12px) rotate(45deg)';
          if (btnOverlayShepard) btnOverlayShepard.textContent = 'Reset Tables';
        } else {
          tabletopRight.style.transform = '';
          if (btnOverlayShepard) btnOverlayShepard.textContent = 'Verify (Overlay Tables)';
        }
      }
    });

    // 18. Coffer Illusion
    const cofferContainer = document.getElementById('coffer-illusion');
    const inputCofferGuess = document.getElementById('input-coffer-guess') as HTMLInputElement;
    const btnCofferCheck = document.getElementById('btn-coffer-check');
    const cofferCircles = cofferContainer?.querySelector('.coffer-circles');

    btnCofferCheck?.addEventListener('click', (e) => {
      e.stopPropagation();
      const val = parseInt(inputCofferGuess?.value || '0');
      if (cofferCircles) {
        if (val === 16) {
          cofferCircles.classList.remove('opacity-0');
          cofferCircles.classList.add('opacity-100');
          alert("🎉 Correct! There are exactly 16 circles hidden in plain sight.");
        } else {
          cofferCircles.classList.remove('opacity-0');
          cofferCircles.classList.add('opacity-100');
          alert(`You guessed ${val}. The correct answer is 16 circles! Look at the red highlights.`);
        }
      }
    });

    // 19. Vertical-Horizontal
    const vhContainer = document.getElementById('v-h-illusion');
    const btnRotateVh = document.getElementById('btn-rotate-vh');
    const vhVertical = document.getElementById('vh-vertical');
    let vhRotated = false;

    btnRotateVh?.addEventListener('click', (e) => {
      e.stopPropagation();
      vhRotated = !vhRotated;
      if (vhVertical) {
        if (vhRotated) {
          // Rotate 90deg to lie flat next to or on top of horizontal line
          vhVertical.style.transform = 'rotate(90deg) translate(0px, 0px)';
          if (btnRotateVh) btnRotateVh.textContent = 'Reset Line';
        } else {
          vhVertical.style.transform = '';
          if (btnRotateVh) btnRotateVh.textContent = 'Rotate to Compare';
        }
      }
    });

    // 20. McGurk Effect Audio & Animation Synthesizer
    const mcgurkContainer = document.getElementById('mcgurk-illusion');
    const btnPlayMcgurk = document.getElementById('btn-play-mcgurk');
    const mcgurkLips = document.getElementById('mcgurk-lips');
    const mcgurkTeeth = document.getElementById('mcgurk-teeth');
    const mcgurkTongue = document.getElementById('mcgurk-tongue');
    const btnMcVotes = mcgurkContainer?.querySelectorAll('.btn-mc-vote');
    const mcFeedback = document.getElementById('mcgurk-feedback');

    btnPlayMcgurk?.addEventListener('click', (e) => {
      e.stopPropagation();
      
      // 1. Play sound synthesized using Web Audio API
      try {
        const audioCtx = new (window.AudioContext || (window as any).webkitAudioContext)();
        
        // Simulating the "BA" sound synthesis:
        // Consonants like B have a quick burst of low frequencies
        const osc = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();
        
        osc.connect(gainNode);
        gainNode.connect(audioCtx.destination);
        
        // Pitch envelope: drops from 280Hz to 120Hz (simulating BA)
        osc.frequency.setValueAtTime(280, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(120, audioCtx.currentTime + 0.12);
        
        // Volume envelope: fast attack, quick decay
        gainNode.gain.setValueAtTime(0, audioCtx.currentTime);
        gainNode.gain.linearRampToValueAtTime(0.8, audioCtx.currentTime + 0.02);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.25);
        
        osc.start(audioCtx.currentTime);
        osc.stop(audioCtx.currentTime + 0.25);
      } catch (err) {
        console.error("Web Audio failed: ", err);
      }

      // 2. Animate lips to simulate "GA" (mouth wider and tongue visible)
      if (mcgurkLips && mcgurkTeeth && mcgurkTongue) {
        // Morph lips to "GA": flatter, open
        mcgurkLips.setAttribute('d', 'M 10,30 Q 50,5 90,30 Q 50,55 10,30 Z');
        mcgurkTeeth.classList.remove('opacity-0');
        mcgurkTongue.classList.remove('opacity-0');
        
        setTimeout(() => {
          // Reset mouth to closed state
          mcgurkLips.setAttribute('d', 'M 10,30 Q 50,15 90,30 Q 50,45 10,30 Z');
          mcgurkTeeth.classList.add('opacity-0');
          mcgurkTongue.classList.add('opacity-0');
        }, 300);
      }
    });

    btnMcVotes?.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        mcFeedback?.classList.remove('hidden');
      });
    });


    // ----------------------------------------------------
    // CLIENT-SIDE FILTERING & SORTING FOR FAMOUS PAGE
    // ----------------------------------------------------
    const filterButtons = document.querySelectorAll('.filter-btn');
    const sortSelect = document.getElementById('famous-sort') as HTMLSelectElement;
    const galleryGrid = document.getElementById('famous-gallery-grid');
    
    // Perform Filtering
    const applyFilter = (filterVal: string) => {
      const cards = document.querySelectorAll('#famous-gallery-grid .illusion-card');
      cards.forEach(card => {
        const cat = card.getAttribute('data-category');
        if (filterVal === 'all' || cat === filterVal) {
          (card as HTMLElement).style.display = 'flex';
        } else {
          (card as HTMLElement).style.display = 'none';
        }
      });
    };

    filterButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        filterButtons.forEach(b => {
          b.classList.remove('bg-purple-650', 'text-white');
          b.classList.add('bg-slate-800', 'text-slate-300');
        });
        btn.classList.remove('bg-slate-800', 'text-slate-300');
        btn.classList.add('bg-purple-650', 'text-white');
        
        const filterVal = btn.getAttribute('data-filter') || 'all';
        applyFilter(filterVal);
      });
    });

    // Perform Sorting
    const applySort = (sortVal: string) => {
      if (!galleryGrid) return;
      const cards = Array.from(document.querySelectorAll('#famous-gallery-grid .illusion-card'));
      
      cards.sort((a, b) => {
        const diffA = parseInt(a.getAttribute('data-difficulty-level') || '1');
        const diffB = parseInt(b.getAttribute('data-difficulty-level') || '1');
        const yearA = parseInt(a.getAttribute('data-year') || '1900');
        const yearB = parseInt(b.getAttribute('data-year') || '1900');

        if (sortVal === 'popular') {
          // Sort by difficulty (easy first) to increase engagement
          return diffA - diffB;
        } else if (sortVal === 'easiest') {
          return diffA - diffB;
        } else if (sortVal === 'hardest') {
          return diffB - diffA;
        } else if (sortVal === 'newest') {
          return yearB - yearA;
        }
        return 0;
      });

      // Clear grid and append in new order
      galleryGrid.innerHTML = '';
      cards.forEach(card => {
        galleryGrid.appendChild(card);
      });

      // Re-setup stopping click propagation for newly appended cards
      const famousCards = document.querySelectorAll('.illusion-card');
      famousCards.forEach(card => {
        card.querySelectorAll('button, input, select, details, summary, label, a, .toggle-dancer, .rubin-btn').forEach(el => {
          el.addEventListener('click', (e) => e.stopPropagation());
          el.addEventListener('mousedown', (e) => e.stopPropagation());
          el.addEventListener('touchstart', (e) => e.stopPropagation());
        });
      });
    };

    sortSelect?.addEventListener('change', () => {
      applySort(sortSelect.value);
    });
"""

content = content.replace("// Stop event propagation on inner details", js_code + "\n    // Stop event propagation on inner details")

# Write changes back to famous.astro
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("famous.astro successfully patched with 5 new cards, tags filtering, and sorting!")

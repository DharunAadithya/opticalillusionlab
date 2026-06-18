import os
import re

workspace_dir = "c:/Users/Amrutha/Documents/opticalillusionlab"
pages_dir = os.path.join(workspace_dir, "src/pages")

color_path = os.path.join(pages_dir, "color.astro")
moving_path = os.path.join(pages_dir, "moving.astro")

# ==========================================
# PATCHING color.astro
# ==========================================
if os.path.exists(color_path):
    content = open(color_path, "r", encoding="utf-8").read()
    
    # Replace link targets for experiments
    # whites: wertheimer-koffka -> whites-illusion
    content = content.replace(
        'href="/illusions/wertheimer-koffka" class="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 flex flex-col justify-between hover:border-purple-500/40 hover:-translate-y-1 hover:shadow-[0_0_20px_rgba(168,85,247,0.35)] cursor-pointer transition-all duration-300 block group" data-exp="whites"',
        'href="/illusions/whites-illusion" class="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 flex flex-col justify-between hover:border-purple-500/40 hover:-translate-y-1 hover:shadow-[0_0_20px_rgba(168,85,247,0.35)] cursor-pointer transition-all duration-300 block group" data-exp="whites"'
    )
    
    # contrast: wertheimer-koffka -> simultaneous-contrast
    content = content.replace(
        'href="/illusions/wertheimer-koffka" class="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 flex flex-col justify-between hover:border-purple-500/40 hover:-translate-y-1 hover:shadow-[0_0_20px_rgba(168,85,247,0.35)] cursor-pointer transition-all duration-300 block group" data-exp="contrast"',
        'href="/illusions/simultaneous-contrast" class="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 flex flex-col justify-between hover:border-purple-500/40 hover:-translate-y-1 hover:shadow-[0_0_20px_rgba(168,85,247,0.35)] cursor-pointer transition-all duration-300 block group" data-exp="contrast"'
    )
    
    # afterimage: troxler-fading -> afterimage-stare
    content = content.replace(
        'href="/illusions/troxler-fading" class="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 flex flex-col justify-between hover:border-purple-500/40 hover:-translate-y-1 hover:shadow-[0_0_20px_rgba(168,85,247,0.35)] cursor-pointer transition-all duration-300 block group" data-exp="afterimage"',
        'href="/illusions/afterimage-stare" class="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 flex flex-col justify-between hover:border-purple-500/40 hover:-translate-y-1 hover:shadow-[0_0_20px_rgba(168,85,247,0.35)] cursor-pointer transition-all duration-300 block group" data-exp="afterimage"'
    )
    
    # aberration: the-dress -> chromatic-aberration
    content = content.replace(
        'href="/illusions/the-dress" class="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 flex flex-col justify-between hover:border-purple-500/40 hover:-translate-y-1 hover:shadow-[0_0_20px_rgba(168,85,247,0.35)] cursor-pointer transition-all duration-300 block group" data-exp="aberration"',
        'href="/illusions/chromatic-aberration" class="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 flex flex-col justify-between hover:border-purple-500/40 hover:-translate-y-1 hover:shadow-[0_0_20px_rgba(168,85,247,0.35)] cursor-pointer transition-all duration-300 block group" data-exp="aberration"'
    )

    # Convert cornsweet div to a tag
    content = content.replace(
        '<div class="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 flex flex-col justify-between hover:border-purple-500/25 transition-all duration-300" data-exp="cornsweet">',
        '<a href="/illusions/cornsweet-illusion" class="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 flex flex-col justify-between hover:border-purple-500/40 hover:-translate-y-1 hover:shadow-[0_0_20px_rgba(168,85,247,0.35)] cursor-pointer transition-all duration-300 block group" data-exp="cornsweet">'
    )
    # Close it: before check-exp="whites"
    content = content.replace(
        '<!-- Experiment 4: White\'s Illusion -->',
        '</a>\n\n      <!-- Experiment 4: White\'s Illusion -->'
    )
    # Convert contours div to a tag
    content = content.replace(
        '<div class="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 flex flex-col justify-between hover:border-purple-500/25 transition-all duration-300" data-exp="contours">',
        '<a href="/illusions/color-from-lines" class="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 flex flex-col justify-between hover:border-purple-500/40 hover:-translate-y-1 hover:shadow-[0_0_20px_rgba(168,85,247,0.35)] cursor-pointer transition-all duration-300 block group" data-exp="contours">'
    )
    # Close it: before data-exp="contrast"
    content = content.replace(
        '<!-- Experiment 6: Simultaneous Contrast -->',
        '</a>\n\n      <!-- Experiment 6: Simultaneous Contrast -->'
    )

    # Inject Instruction Box & Collapsible Explain Box for each of the 8 experiments
    # Define instructions mapping
    instructions = {
        "checkerboard": "Look at tiles A and B. Click 'Reveal Truth' to see they have identical gray colors.",
        "spheres": "Observe the spheres. Click 'Remove Colored Lines' to see that they are all the same shade of gray.",
        "cornsweet": "Look at the left and right halves. Hover or click to cover the dividing edge and see they are identical.",
        "whites": "Examine the gray bars on white and black stripes. Click 'Isolate Gray Bars' to see they are identical.",
        "contours": "Observe the yellow and blue regions. Click 'Remove Contours' to see the grid lines are completely black.",
        "contrast": "Stare at the orange square. Drag the background slider and see how its color appears to change.",
        "afterimage": "Stare at the white center dot in the cyan cross for 30s. Look at the white box when the timer ends.",
        "aberration": "Focus on the white center dot. Red circles will float forward while blue circles recede behind."
    }
    
    explanations = {
        "checkerboard": "The brain does not measure raw luminance; it evaluates colors relative to lighting. Because Tile B is inside the shadow, the brain scales its perceived brightness up, making it look white compared to Tile A.",
        "spheres": "Chromatic assimilation (neon color spreading) causes local color signals from foreground lines to bleed into the adjacent gray circles in our visual cortex, tricking us into seeing red, blue, or green spheres.",
        "cornsweet": "The Cornsweet illusion shows that surface brightness is computed from edge contrast. The gradient boundary trick-forces the brain to paint the entire left half lighter and the right half darker.",
        "whites": "Gestalt grouping rules prioritize horizontal line continuity. Because the gray bars are grouped with the stripes they break, they absorb different contrast weights, overriding retinal lateral inhibition.",
        "contours": "The brain expects colored shadows and transparency in layered objects. It fills the color across the white spaces to create a continuous glowing layer under the black grid lines.",
        "contrast": "Simultaneous contrast is caused by lateral inhibition in retina cells. A dark background causes adjacent cells processing the orange square to fire faster, enhancing its perceived brightness.",
        "afterimage": "Continuous staring exhausts the green/blue photoreceptors. Shifting gaze to white triggers the rested red receptors to fire faster, producing a complementary red/pink ghost afterimage.",
        "aberration": "Because the eye's lens refracts different light wavelengths at different angles, red focuses further back than blue, forcing your visual cortex to compute different depth planes for each color."
    }

    for key in instructions:
        # Locate the card's inner content and inject instruction/explanation
        # We find: data-exp="key" and then the next my-6 flex
        target_card_start = f'data-exp="{key}"'
        idx = content.find(target_card_start)
        if idx != -1:
            # Search for the demo area inside this card
            demo_search = 'class="my-6 flex flex-col items-center justify-center bg-slate-950/40'
            demo_idx = content.find(demo_search, idx)
            if demo_idx != -1:
                # Prepend instruction box before demo area
                ins_box = f"""
        <!-- Instruction Box -->
        <div class="my-3 flex items-start gap-2 rounded-xl border border-indigo-500/10 bg-indigo-500/5 p-3 text-xs text-slate-350">
          <span class="text-base leading-none">👁️</span>
          <div>
            <strong class="text-slate-200">Instructions:</strong> {instructions[key]}
          </div>
        </div>
"""
                content = content[:demo_idx] + ins_box + content[demo_idx:]
                
                # Append collapsible explanation before the action buttons panel
                # Find the next mt-5 flex panel
                panel_search = 'class="mt-5 flex items-center justify-between border-t border-slate-850 pt-4"'
                panel_idx = content.find(panel_search, demo_idx + len(ins_box))
                if panel_idx != -1:
                    exp_box = f"""
        <!-- Collapsible Explanation -->
        <details class="mt-4 border-t border-slate-800/40 pt-3 text-xs text-slate-400 select-none">
          <summary class="font-bold cursor-pointer hover:text-purple-400">👁️ Reveal Answer & Science</summary>
          <p class="mt-2 font-normal leading-relaxed text-slate-400">
            {explanations[key]}
          </p>
        </details>
"""
                    content = content[:panel_idx] + exp_box + content[panel_idx:]
                    print(f"Injected boxes for {key} in color.astro")

    with open(color_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("color.astro patched successfully.")

# ==========================================
# PATCHING moving.astro
# ==========================================
if os.path.exists(moving_path):
    content = open(moving_path, "r", encoding="utf-8").read()
    
    # 1. Update broken links
    content = content.replace('href="/illusions/reverse-spoke" id="waterfall-illusion"', 'href="/illusions/waterfall-effect" id="waterfall-illusion"')
    content = content.replace('href="/illusions/reverse-spoke" id="motion-aftereffect"', 'href="/illusions/motion-aftereffect" id="motion-aftereffect"')
    content = content.replace('href="/illusions/rotating-snakes" id="ouchi-illusion"', 'href="/illusions/ouchi-illusion" id="ouchi-illusion"')
    content = content.replace('href="/illusions/motion-binding" id="enigma-illusion"', 'href="/illusions/enigma-illusion" id="enigma-illusion"')
    content = content.replace('href="/illusions/breathing-square" id="levitating-ball"', 'href="/illusions/levitating-ball" id="levitating-ball"')
    print("Links patched in moving.astro")

    # 2. Upgrade generateRingSectors to support rInner
    old_helper = """// Generate concentric ring sectors for Moving Snakes & Peripheral Drift
function generateRingSectors(cx: number, cy: number, r: number, count: number, reversed: boolean) {
  const colors = [
    'fill-slate-950 dark:fill-slate-900',          // Black
    'fill-indigo-600 dark:fill-indigo-500',       // Blue
    'fill-white dark:fill-slate-100',              // White
    'fill-yellow-400 dark:fill-yellow-300'         // Yellow
  ];
  if (reversed) {
    colors.reverse();
  }
  for (let i = 0; i < count; i++) {
    const baseAngle = (i * 360) / count;
    const step = 360 / count / 4;
    for (let c = 0; c < 4; c++) {
      sectors.push({
        path: getWedgePath(cx, cy, r, baseAngle + c * step, baseAngle + (c + 1) * step),
        color: colors[c]
      });
    }
  }
  return sectors;
}"""

    # Wait, let's replace generateRingSectors in moving.astro frontmatter exactly.
    # Let's read the lines 16 to 40 of moving.astro and do an exact replace.
    # Let's inspect moving.astro lines 16-41 in moving_path.
    content = re.sub(
        r'function generateRingSectors\(cx: number, cy: number, r: number, count: number, reversed: boolean\).*?return sectors;\s*\}',
        """function generateRingSectors(cx: number, cy: number, rOuter: number, rInner: number, count: number, reversed: boolean) {
  const sectors = [];
  const colors = [
    'fill-slate-950 dark:fill-slate-900',          // Black
    'fill-slate-400 dark:fill-slate-500',          // Gray
    'fill-white dark:fill-slate-100',              // White
    'fill-yellow-400 dark:fill-yellow-300'         // Yellow
  ];
  if (reversed) {
    colors.reverse();
  }
  const rad = Math.PI / 180;
  for (let i = 0; i < count; i++) {
    const baseAngle = (i * 360) / count;
    const step = 360 / count / 4;
    for (let c = 0; c < 4; c++) {
      const startAngle = baseAngle + c * step;
      const endAngle = baseAngle + (c + 1) * step;
      
      const x1_out = cx + rOuter * Math.cos(startAngle * rad);
      const y1_out = cy + rOuter * Math.sin(startAngle * rad);
      const x2_out = cx + rOuter * Math.cos(endAngle * rad);
      const y2_out = cy + rOuter * Math.sin(endAngle * rad);
      
      const x1_in = cx + rInner * Math.cos(startAngle * rad);
      const y1_in = cy + rInner * Math.sin(startAngle * rad);
      const x2_in = cx + rInner * Math.cos(endAngle * rad);
      const y2_in = cy + rInner * Math.sin(endAngle * rad);
      
      const path = `M ${x1_in},${y1_in} L ${x1_out},${y1_out} A ${rOuter},${rOuter} 0 0,1 ${x2_out},${y2_out} L ${x2_in},${y2_in} A ${rInner},${rInner} 0 0,0 ${x1_in},${y1_in} Z`;
      
      sectors.push({
        path,
        color: colors[c]
      });
    }
  }
  return sectors;
}""",
        content,
        flags=re.DOTALL
    )
    print("generateRingSectors helper updated in moving.astro")

    # Update driftOuter and driftInner calls to pass rInner
    content = content.replace(
        "const driftOuter = generateRingSectors(100, 100, 90, 24, false);",
        "const driftOuter = generateRingSectors(100, 100, 90, 55, 24, false);"
    )
    content = content.replace(
        "const driftInner = generateRingSectors(100, 100, 55, 16, true);",
        "const driftInner = generateRingSectors(100, 100, 55, 25, 16, true);"
    )

    # 3. Define the 6 rings for Rotating Snakes on listing page in the frontmatter of moving.astro
    # Let's insert the definition of r1..r6 before the template starts (e.g. before "const driftOuter = ...")
    content = content.replace(
        "const driftOuter = generateRingSectors",
        """const r1 = generateRingSectors(100, 100, 95, 80, 24, false);
const r2 = generateRingSectors(100, 100, 80, 66, 20, true);
const r3 = generateRingSectors(100, 100, 66, 52, 16, false);
const r4 = generateRingSectors(100, 100, 52, 38, 12, true);
const r5 = generateRingSectors(100, 100, 38, 24, 8, false);
const r6 = generateRingSectors(100, 100, 24, 10, 6, true);

const driftOuter = generateRingSectors"""
    )
    print("Rotating Snakes 6-rings variables declared in moving.astro")

    # 4. Replace Rotating Snakes SVG code in moving.astro to render 6 concentric rings with opposite animation styles
    old_snakes_svg = """          <div class="grid grid-cols-2 gap-4 max-w-[200px] select-none pointer-events-none">
            {Array.from({ length: 4 }).map((_, idx) => {
              const isClockwise = idx % 2 === 0;
              const oRing = generateRingSectors(100, 100, 80, 12, isClockwise);
              const iRing = generateRingSectors(100, 100, 50, 8, !isClockwise);
              return (
                <svg 
                  class="w-20 h-20 origin-center transition-transform select-none" 
                  viewBox="0 0 200 200"
                  style={`animation: ${isClockwise ? 'spin-clockwise' : 'spin-counter'} calc(15s / var(--card-speed, 1)) var(--card-play-state, running) linear infinite;`}
                >
                  <g class="outer-snakes">
                    {oRing.map(sect => (
                      <path d={sect.path} class={sect.color} stroke="none" />
                    ))}
                  </g>
                  <g class="inner-snakes">
                    {iRing.map(sect => (
                      <path d={sect.path} class={sect.color} stroke="none" />
                    ))}
                  </g>
                  <circle cx="100" cy="100" r="22" class="fill-slate-100 dark:fill-slate-950 transition-colors" />
                </svg>
              )
            })}
          </div>"""

    # Render individual concentric ring groups with opposite rotations
    new_snakes_svg = """          <div class="grid grid-cols-2 gap-4 max-w-[200px] select-none pointer-events-none">
            {Array.from({ length: 4 }).map((_, idx) => {
              const isClockwise = idx % 2 === 0;
              return (
                <svg 
                  class="w-20 h-20 origin-center transition-transform select-none overflow-visible" 
                  viewBox="0 0 200 200"
                >
                  <!-- Ring 1 -->
                  <g class="origin-center" style={`transform-origin: 100px 100px; animation: ${isClockwise ? 'spin-clockwise' : 'spin-counter'} calc(15s / var(--card-speed, 1)) var(--card-play-state, running) linear infinite;`}>
                    {r1.map(sect => (
                      <path d={sect.path} class={sect.color} stroke="none" />
                    ))}
                  </g>
                  <!-- Ring 2 -->
                  <g class="origin-center" style={`transform-origin: 100px 100px; animation: ${!isClockwise ? 'spin-clockwise' : 'spin-counter'} calc(15s / var(--card-speed, 1)) var(--card-play-state, running) linear infinite;`}>
                    {r2.map(sect => (
                      <path d={sect.path} class={sect.color} stroke="none" />
                    ))}
                  </g>
                  <!-- Ring 3 -->
                  <g class="origin-center" style={`transform-origin: 100px 100px; animation: ${isClockwise ? 'spin-clockwise' : 'spin-counter'} calc(15s / var(--card-speed, 1)) var(--card-play-state, running) linear infinite;`}>
                    {r3.map(sect => (
                      <path d={sect.path} class={sect.color} stroke="none" />
                    ))}
                  </g>
                  <!-- Ring 4 -->
                  <g class="origin-center" style={`transform-origin: 100px 100px; animation: ${!isClockwise ? 'spin-clockwise' : 'spin-counter'} calc(15s / var(--card-speed, 1)) var(--card-play-state, running) linear infinite;`}>
                    {r4.map(sect => (
                      <path d={sect.path} class={sect.color} stroke="none" />
                    ))}
                  </g>
                  <!-- Ring 5 -->
                  <g class="origin-center" style={`transform-origin: 100px 100px; animation: ${isClockwise ? 'spin-clockwise' : 'spin-counter'} calc(15s / var(--card-speed, 1)) var(--card-play-state, running) linear infinite;`}>
                    {r5.map(sect => (
                      <path d={sect.path} class={sect.color} stroke="none" />
                    ))}
                  </g>
                  <!-- Ring 6 -->
                  <g class="origin-center" style={`transform-origin: 100px 100px; animation: ${!isClockwise ? 'spin-clockwise' : 'spin-counter'} calc(15s / var(--card-speed, 1)) var(--card-play-state, running) linear infinite;`}>
                    {r6.map(sect => (
                      <path d={sect.path} class={sect.color} stroke="none" />
                    ))}
                  </g>
                  <circle cx="100" cy="100" r="10" class="fill-slate-100 dark:fill-slate-950 transition-colors" />
                </svg>
              )
            })}
          </div>"""

    if old_snakes_svg in content:
        content = content.replace(old_snakes_svg, new_snakes_svg)
        print("Rotating snakes SVG upgraded in moving.astro")
    else:
        # Try a regex-based block replace
        content = re.sub(
            r'<div class="grid grid-cols-2 gap-4 max-w-\[200px\] select-none pointer-events-none">.*?\{Array\.from\(\{ length: 4 \}\).*?<\/div>\s*<\/div>',
            new_snakes_svg + "\n        </div>",
            content,
            flags=re.DOTALL
        )
        print("Fallback Rotating snakes SVG upgraded in moving.astro")

    # 5. Replace Expanding Hole SVG code in moving.astro to include high contrast concentric dots & 80px core
    old_hole_svg = """          <svg class="w-64 h-64 select-none rounded-xl" viewBox="0 0 200 200">
            <defs>
              <radialGradient id="hole-grad-famous" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stop-color="#020617" />
                <stop offset="60%" stop-color="#020617" stop-opacity="0.8" />
                <stop offset="100%" stop-color="#020617" stop-opacity="0" />
              </radialGradient>
              <pattern id="dot-pattern-famous" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
                <circle cx="10" cy="10" r="3.5" fill="#64748b" />
              </pattern>
            </defs>
            <rect width="200" height="200" fill="url(#dot-pattern-famous)" />
            <circle 
              cx="100" 
              cy="100" 
              r="65" 
              fill="url(#hole-grad-famous)" 
              class="origin-center" 
              style="transform-origin: 100px 100px; animation: expand-hole calc(6s / var(--card-speed, 1)) var(--card-play-state, running) ease-in-out infinite;" 
            />
          </svg>"""

    new_hole_svg = """          <svg class="w-64 h-64 select-none rounded-xl" viewBox="0 0 200 200">
            <defs>
              <filter id="radial-blur-hole-unique-moving">
                <feGaussianBlur stdDeviation="8" />
              </filter>
              <radialGradient id="hole-grad-core-unique-moving" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stop-color="#000000" />
                <stop offset="65%" stop-color="#000000" />
                <stop offset="100%" stop-color="#000000" stop-opacity="0" />
              </radialGradient>
            </defs>
            
            <!-- Dark background -->
            <rect width="200" height="200" fill="#0f172a" />
            
            <!-- Concentric depth rings -->
            <g stroke="#1e293b" stroke-width="1.5" fill="none">
              <circle cx="100" cy="100" r="95" stroke-opacity="0.1" />
              <circle cx="100" cy="100" r="85" stroke-opacity="0.2" />
              <circle cx="100" cy="100" r="75" stroke-opacity="0.3" />
              <circle cx="100" cy="100" r="65" stroke-opacity="0.4" />
              <circle cx="100" cy="100" r="55" stroke-opacity="0.5" />
              <circle cx="100" cy="100" r="45" stroke-opacity="0.6" />
              <circle cx="100" cy="100" r="35" stroke-opacity="0.7" />
              <circle cx="100" cy="100" r="25" stroke-opacity="0.8" />
            </g>
            
            <!-- Concentric rings of dots pattern (polar coordinates layout) -->
            <g fill="#475569">
              <!-- Outer Ring: R=90 -->
              <circle cx="100" cy="10" r="2.5" /><circle cx="122" cy="11" r="2.5" /><circle cx="143" cy="17" r="2.5" /><circle cx="162" cy="27" r="2.5" />
              <circle cx="177" cy="42" r="2.5" /><circle cx="187" cy="60" r="2.5" /><circle cx="190" cy="80" r="2.5" />
              <circle cx="190" cy="100" r="2.5" /><circle cx="190" cy="120" r="2.5" /><circle cx="187" cy="140" r="2.5" />
              <circle cx="177" cy="158" r="2.5" /><circle cx="162" cy="173" r="2.5" /><circle cx="143" cy="183" r="2.5" />
              <circle cx="122" cy="189" r="2.5" /><circle cx="100" cy="190" r="2.5" /><circle cx="78" cy="189" r="2.5" />
              <circle cx="57" cy="183" r="2.5" /><circle cx="38" cy="173" r="2.5" /><circle cx="23" cy="158" r="2.5" />
              <circle cx="13" cy="140" r="2.5" /><circle cx="10" cy="120" r="2.5" /><circle cx="10" cy="100" r="2.5" />
              <circle cx="10" cy="80" r="2.5" /><circle cx="13" cy="60" r="2.5" /><circle cx="23" cy="42" r="2.5" />
              <circle cx="38" cy="27" r="2.5" /><circle cx="57" cy="17" r="2.5" /><circle cx="78" cy="11" r="2.5" />
              
              <!-- Ring 2: R=75 -->
              <circle cx="100" cy="25" r="2.2" /><circle cx="125" cy="28" r="2.2" /><circle cx="147" cy="39" r="2.2" /><circle cx="164" cy="56" r="2.2" />
              <circle cx="172" cy="78" r="2.2" /><circle cx="175" cy="100" r="2.2" /><circle cx="172" cy="122" r="2.2" />
              <circle cx="164" cy="144" r="2.2" /><circle cx="147" cy="161" r="2.2" /><circle cx="125" cy="172" r="2.2" />
              <circle cx="100" cy="175" r="2.2" /><circle cx="75" cy="172" r="2.2" /><circle cx="53" cy="161" r="2.2" />
              <circle cx="36" cy="144" r="2.2" /><circle cx="28" cy="122" r="2.2" /><circle cx="25" cy="100" r="2.2" />
              <circle cx="28" cy="78" r="2.2" /><circle cx="36" cy="56" r="2.2" /><circle cx="53" cy="39" r="2.2" /><circle cx="75" cy="28" r="2.2" />
              
              <!-- Ring 3: R=55 -->
              <circle cx="100" cy="45" r="1.8" /><circle cx="119" cy="48" r="1.8" /><circle cx="135" cy="58" r="1.8" /><circle cx="145" cy="75" r="1.8" />
              <circle cx="148" cy="95" r="1.8" /><circle cx="145" cy="115" r="1.8" /><circle cx="135" cy="132" r="1.8" />
              <circle cx="119" cy="142" r="1.8" /><circle cx="100" cy="145" r="1.8" /><circle cx="81" cy="142" r="1.8" />
              <circle cx="65" cy="132" r="1.8" /><circle cx="55" cy="115" r="1.8" /><circle cx="52" cy="95" r="1.8" />
              <circle cx="55" cy="75" r="1.8" /><circle cx="65" cy="58" r="1.8" /><circle cx="81" cy="48" r="1.8" />

              <!-- Ring 4: R=35 -->
              <circle cx="100" cy="65" r="1.5" /><circle cx="115" cy="68" r="1.5" /><circle cx="127" cy="80" r="1.5" /><circle cx="130" cy="95" r="1.5" />
              <circle cx="127" cy="110" r="1.5" /><circle cx="115" cy="122" r="1.5" /><circle cx="100" cy="125" r="1.5" />
              <circle cx="85" cy="122" r="1.5" /><circle cx="73" cy="110" r="1.5" /><circle cx="70" cy="95" r="1.5" /><circle cx="73" cy="80" r="1.5" /><circle cx="85" cy="68" r="1.5" />
            </g>

            <!-- Radial blur black void overlay -->
            <circle cx="100" cy="100" r="46" fill="url(#hole-grad-core-unique-moving)" filter="url(#radial-blur-hole-unique-moving)" opacity="0.95" />
            
            <!-- Sharp central core of 80px diameter (radius 40) with animation -->
            <circle 
              cx="100" 
              cy="100" 
              r="40" 
              fill="#000000" 
              class="origin-center" 
              style="transform-origin: 100px 100px; animation: expand-hole calc(6s / var(--card-speed, 1)) var(--card-play-state, running) ease-in-out infinite;" 
            />
          </svg>"""

    if old_hole_svg in content:
        content = content.replace(old_hole_svg, new_hole_svg)
        print("Expanding hole SVG upgraded in moving.astro")
    else:
        # Fallback
        content = re.sub(
            r'<svg class="w-64 h-64 select-none rounded-xl" viewBox="0 0 200 200">.*?<\/svg>',
            new_hole_svg,
            content,
            flags=re.DOTALL
        )
        print("Fallback Expanding hole SVG upgraded in moving.astro")

    # 6. Inject Instructions and Collapsible Reveal Answer Box for each card in moving.astro
    # Locate elements inside each card in moving.astro and perform edits
    moving_instructions = {
        "1. Rotating Snakes": "Stare at the center of one of the circles. Notice how the rotation stops, but the surrounding circles continue to spin in your periphery.",
        "2. Peripheral Drift Wheels": "Scan your eyes around the wheels. The inner and outer wheels will appear to rotate in opposite directions.",
        "3. Pulsing Grid": "Stare at the intersections of the grid. Notice how the yellow dots appear to expand, contract, and glow dynamically.",
        "4. Waterfall Effect": "Stare at the red dot in the center for 30s. The moving background will fatigue your motion detectors. Focus elsewhere to see drift.",
        "5. Expanding Hole": "Stare at the black center core. The dark void will appear to expand outward, swallowing the screen.",
        "6. Tilted House": "Watch the parallel lines. The diagonal segments make them look tilted and wobbly rather than perfectly horizontal.",
        "7. Motion Aftereffect": "Stare at the center of the spinning spiral for 30s. Shifting your gaze will make stationary objects expand or contract.",
        "8. Ouchi Illusion": "Tilt your head or scroll the page up and down. The circular disc in the center will appear to float and slide across the grid.",
        "9. Enigma": "Observe the circular rings. The radiating black and white lines generate a rapid, circular flowing liquid movement in the rings.",
        "10. Levitating Ball": "Observe the sphere and the moving shadow. The ball appears to rise and fall in height relative to the ground."
    }

    moving_explanations = {
        "1. Rotating Snakes": "Visual neurons process contrast levels at different latencies. The black-to-white shift triggers direction cells faster than blue-to-yellow, creating a phantom spin in your periphery.",
        "2. Peripheral Drift Wheels": "Micro-saccades shift the radial contrast boundaries across your retina, triggering directional orientation columns in area MT/V5, simulating physical rotation.",
        "3. Pulsing Grid": "Receptive fields in your retina compete via lateral inhibition. The high-contrast intersections appear to glow and breathe as they adjust to neighboring stimulus levels.",
        "4. Waterfall Effect": "Staring at downward movement fatigues downward-detecting cells. Looking at a static image leaves the upward-detecting cells firing relatively faster, generating upward motion.",
        "5. Expanding Hole": "The dark radial gradient triggers a pupil dilation response. The visual cortex interprets this as moving into a dark tunnel, causing the hole to expand.",
        "6. Tilted House": "Intersecting diagonal grids skew your spatial coordinate frame. Your brain interprets the angles incorrectly, distorting the alignment of parallel lines.",
        "7. Motion Aftereffect": "Staring at the spiral adapts direction-sensitive neurons. Looking at a static target causes non-adapted neurons representing opposite directions to fire, simulating expansion/contraction.",
        "8. Ouchi Illusion": "Eye micro-movements stimulate the orthogonal horizontal and vertical checkers at different rates, causing the brain to segment the circle as a separate 3D layer.",
        "9. Enigma": "Involuntary micro-saccades shift the radial ray contours, causing transient motion signals that are interpreted by the visual cortex as circular flow along the rings.",
        "10. Levitating Ball": "Our depth estimation system depends heavily on shadows. Moving the shadow further away from the ball forces the brain to calculate that the ball is rising in height."
    }

    # Inject instruction boxes above demo-area and details boxes below
    for title, ins in moving_instructions.items():
        title_idx = content.find(title)
        if title_idx != -1:
            # Locate next demo-area
            demo_search = 'class="demo-area'
            demo_idx = content.find(demo_search, title_idx)
            if demo_idx != -1:
                ins_box = f"""
        <!-- Instruction Box -->
        <div class="my-3 flex items-start gap-2 rounded-xl border border-indigo-500/10 bg-indigo-500/5 p-3 text-xs text-slate-350">
          <span class="text-base leading-none">👁️</span>
          <div>
            <strong class="text-slate-200">Instructions:</strong> {ins}
          </div>
        </div>
"""
                content = content[:demo_idx] + ins_box + content[demo_idx:]
                
                # Append collapsible explanation details box
                # Find the next mt-4 flex panel or details summary
                details_search = '<details class="mt-4 border-t border-slate-500/10'
                details_idx = content.find(details_search, demo_idx + len(ins_box))
                if details_idx != -1:
                    exp_box = f"""
        <!-- Collapsible Explanation -->
        <details class="mt-4 border-t border-slate-500/10 pt-3 text-xs text-slate-400 select-none">
          <summary class="font-bold cursor-pointer hover:text-purple-400">👁️ Reveal Answer & Science</summary>
          <p class="mt-2 font-normal leading-relaxed text-slate-450">
            {moving_explanations[title]}
          </p>
        </details>
"""
                    content = content[:details_idx] + exp_box + content[details_idx:]
                    print(f"Injected boxes for {title} in moving.astro")

    with open(moving_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("moving.astro patched successfully.")

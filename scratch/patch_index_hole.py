import os
import re

filepath = "src/pages/index.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Locate the old SVG in index.astro
old_svg_pattern = r'<svg class="w-44 h-44 select-none" viewBox="0 0 200 200">\s*<defs>\s*<radialGradient id="hole-grad-static-home".*?</svg>'

new_svg = """<svg class="w-44 h-44 select-none rounded-xl" viewBox="0 0 200 200">
            <defs>
              <filter id="radial-blur-hole-unique-home">
                <feGaussianBlur stdDeviation="8" />
              </filter>
              <radialGradient id="hole-grad-core-unique-home" cx="50%" cy="50%" r="50%">
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
            <circle cx="100" cy="100" r="46" fill="url(#hole-grad-core-unique-home)" filter="url(#radial-blur-hole-unique-home)" opacity="0.95" />
            
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

new_content = re.sub(old_svg_pattern, new_svg, content, flags=re.DOTALL)
if new_content != content:
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully patched Expanding Hole SVG in index.astro")
else:
    print("Warning: Could not match Expanding Hole SVG in index.astro")

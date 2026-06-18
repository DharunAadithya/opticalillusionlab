import os
import re

def print_svg(file_path):
    if not os.path.exists(file_path):
        print(f"{file_path} not found")
        return
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = re.finditer(r'<svg[^>]*>', content)
    print(f"\n--- SVGs in {file_path} ---")
    for m in matches:
        start_idx = m.start()
        end_idx = content.find("</svg>", start_idx) + 6
        svg_code = content[start_idx:end_idx]
        if "hole-grad" in svg_code or "radial-blur-hole" in svg_code or "expand-hole" in svg_code:
            print(svg_code.encode('ascii', errors='replace').decode('ascii'))

print_svg("src/pages/index.astro")
print_svg("src/pages/illusions/expanding-hole.astro")

import os
import re

def print_svg(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Let's find all SVGs in the file
    matches = re.finditer(r'<svg[^>]*>', content)
    print(f"\n--- SVGs in {file_path} ---")
    for m in matches:
        start_idx = m.start()
        end_idx = content.find("</svg>", start_idx) + 6
        svg_code = content[start_idx:end_idx]
        if "viewBox" in svg_code and ("penrose" in svg_code or "impossible" in svg_code or "points=" in svg_code or "w-44" in svg_code or "h-44" in svg_code or "w-full" in svg_code or "h-64" in svg_code):
            print(svg_code[:400] + "\n...\n" + svg_code[-100:])

print_svg("src/pages/famous.astro")
print_svg("src/pages/illusions/penrose-triangle.astro")

import os

files_to_patch = [
    "src/pages/famous.astro",
    "src/pages/illusions/penrose-triangle.astro"
]

old_svg_block = """              <polygon points="0,-120 30,-102 30,58 -30,92 -30,-68" fill="#6366f1" />
              <polygon points="30,-102 90,-68 30,-34 -30,-68" fill="#818cf8" />
              <polygon points="-30,92 30,58 90,-68 90,-34 30,92 -30,126" fill="#4f46e5" />
              <polygon points="30,92 90,58 30,24 -30,58" fill="#3730a3" />
              <polygon points="-30,126 30,92 -90,-68 -90,-102 -30,-68 -30,126" fill="#4338ca" />
              <polygon points="-30,-68 -90,-102 -30,-136 30,-102" fill="#312e81" />"""

new_svg_block = """              <polygon points="0,-120 30,-102 30,58 -30,92 -30,-68" fill="#cbd5e1" />
              <polygon points="30,-102 90,-68 30,-34 -30,-68" fill="#e2e8f0" />
              <polygon points="-30,92 30,58 90,-68 90,-34 30,92 -30,126" fill="#94a3b8" />
              <polygon points="30,92 90,58 30,24 -30,58" fill="#64748b" />
              <polygon points="-30,126 30,92 -90,-68 -90,-102 -30,-68 -30,126" fill="#334155" />
              <polygon points="-30,-68 -90,-102 -30,-136 30,-102" fill="#1e293b" />"""

for file_path in files_to_patch:
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        if old_svg_block in content:
            content = content.replace(old_svg_block, new_svg_block)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Successfully patched Penrose Triangle SVG in {file_path}")
        else:
            # Try a slightly more loose replacement (handling potential whitespace differences)
            normalized_content = content.replace('\r\n', '\n')
            normalized_old = old_svg_block.replace('\r\n', '\n')
            normalized_new = new_svg_block.replace('\r\n', '\n')
            
            if normalized_old in normalized_content:
                normalized_content = normalized_content.replace(normalized_old, normalized_new)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(normalized_content)
                print(f"Successfully patched Penrose Triangle SVG with normalized spacing in {file_path}")
            else:
                print(f"Warning: Penrose Triangle block not found in {file_path}")
    else:
        print(f"Error: {file_path} not found")

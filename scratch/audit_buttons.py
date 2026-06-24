import os
import re

def audit_buttons():
    button_regex = re.compile(r'<button[^>]*>', re.IGNORECASE)
    src_dir = 'c:/Users/Amrutha/Documents/opticalillusionlab/src'
    
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.astro'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                matches = button_regex.findall(content)
                if matches:
                    print(f"--- {os.path.relpath(path, src_dir)} ---")
                    for m in matches:
                        print(f"  {m.strip()}")

if __name__ == '__main__':
    audit_buttons()

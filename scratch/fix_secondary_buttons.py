import os

def fix_secondary_buttons():
    src_dir = 'c:/Users/Amrutha/Documents/opticalillusionlab/src'
    
    replacements = [
        # Hide buttons on hidden pages
        (
            'class="flex-1 bg-slate-200 hover:bg-slate-300 text-slate-800 dark:bg-slate-800 dark:hover:bg-slate-700 dark:text-white font-bold text-xs py-2.5 rounded-lg border-none transition-colors cursor-pointer shadow hidden"',
            'class="flex-1 bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-bold text-xs py-2.5 rounded-lg border-none transition-colors cursor-pointer shadow hidden"'
        ),
        (
            'class="flex-1 bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs py-2.5 rounded-lg border border-slate-700 transition-colors cursor-pointer shadow hidden"',
            'class="flex-1 bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-bold text-xs py-2.5 rounded-lg border-none transition-colors cursor-pointer shadow hidden"'
        ),
        # Try again / reset experience buttons
        (
            'class="w-full border border-purple-500/30 text-purple-400 hover:bg-purple-500/10 font-bold text-[10px] py-2 rounded-lg transition-colors bg-transparent cursor-pointer"',
            'class="w-full bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-bold text-[10px] py-2 rounded-lg transition-colors border-none cursor-pointer"'
        ),
        # Waterfall Effect No button
        (
            'class="flex-1 bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs py-2 rounded-lg transition-colors cursor-pointer border-none"',
            'class="flex-1 bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-bold text-xs py-2 rounded-lg transition-colors cursor-pointer border-none"'
        )
    ]
    
    modified_count = 0
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.astro'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                orig = content
                for target, replacement in replacements:
                    content = content.replace(target, replacement)
                
                if content != orig:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Fixed secondary buttons in: {os.path.relpath(path, src_dir)}")
                    modified_count += 1
                    
    print(f"Total files modified: {modified_count}")

if __name__ == '__main__':
    fix_secondary_buttons()

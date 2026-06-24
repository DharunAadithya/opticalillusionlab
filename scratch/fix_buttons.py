import os

def fix_buttons():
    src_dir = 'c:/Users/Amrutha/Documents/opticalillusionlab/src'
    
    replacements = [
        # Share buttons
        (
            'class="relative shrink-0 flex items-center space-x-2 rounded-2xl bg-gradient-to-r from-pink-500 via-purple-600 to-indigo-600 hover:scale-105 text-white font-black text-sm px-6 py-3.5 transition-all shadow-lg shadow-purple-500/10"',
            'class="relative shrink-0 flex items-center space-x-2 rounded-lg bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-black text-sm px-6 py-3.5 transition-colors shadow-lg cursor-pointer border-none"'
        ),
        (
            'class="relative shrink-0 flex items-center space-x-2 rounded-2xl bg-gradient-to-r from-pink-500 via-purple-655 to-indigo-600 hover:scale-105 text-white font-black text-sm px-6 py-3.5 transition-all shadow-lg shadow-purple-500/10"',
            'class="relative shrink-0 flex items-center space-x-2 rounded-lg bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-black text-sm px-6 py-3.5 transition-colors shadow-lg cursor-pointer border-none"'
        ),
        (
            'class="relative shrink-0 flex items-center space-x-2 rounded-2xl bg-gradient-to-r from-pink-500 via-purple-600 to-indigo-600 hover:scale-105 text-white font-black text-sm px-6 py-3.5 transition-all shadow-lg shadow-purple-500/10 cursor-pointer border-none"',
            'class="relative shrink-0 flex items-center space-x-2 rounded-lg bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-black text-sm px-6 py-3.5 transition-colors shadow-lg cursor-pointer border-none"'
        ),
        (
            'class="relative shrink-0 flex items-center space-x-2 rounded-2xl bg-gradient-to-r from-pink-500 via-purple-600 to-indigo-600 hover:scale-105 text-white font-black text-sm px-6 py-3.5 transition-all shadow-lg"',
            'class="relative shrink-0 flex items-center space-x-2 rounded-lg bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-black text-sm px-6 py-3.5 transition-colors shadow-lg cursor-pointer border-none"'
        ),
        (
            'class="relative shrink-0 flex items-center space-x-2 rounded-2xl bg-gradient-to-r from-pink-500 via-purple-600 to-indigo-600 hover:scale-105 text-white font-black text-sm px-6 py-3.5 transition-all shadow-lg shadow-purple-500/10 z-20"',
            'class="relative shrink-0 flex items-center space-x-2 rounded-lg bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-black text-sm px-6 py-3.5 transition-colors shadow-lg cursor-pointer border-none z-20"'
        ),
        (
            'class="share-btn absolute top-6 right-6 p-2 rounded-lg bg-slate-50 hover:bg-slate-100 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-400 hover:text-slate-200 border border-slate-500/5 transition-colors z-20"',
            'class="share-btn absolute top-6 right-6 p-2 rounded-lg bg-[#7C3AED] hover:bg-[#6D28D9] text-white border-none transition-colors z-20 cursor-pointer"'
        ),
        (
            'class="share-btn absolute top-6 right-6 p-2 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-400 hover:text-slate-200 border border-slate-500/10 transition-colors"',
            'class="share-btn absolute top-6 right-6 p-2 rounded-lg bg-[#7C3AED] hover:bg-[#6D28D9] text-white border-none transition-colors cursor-pointer"'
        ),
        # Test page buttons
        (
            'class="rounded-2xl bg-gradient-to-r from-pink-500 via-purple-600 to-indigo-600 px-8 py-4 text-base font-black text-white shadow-xl hover:scale-105 transition-all"',
            'class="rounded-lg bg-[#7C3AED] hover:bg-[#6D28D9] px-8 py-4 text-base font-black text-white shadow-xl transition-all border-none cursor-pointer"'
        ),
        (
            'class="w-full sm:w-auto rounded-2xl bg-gradient-to-r from-pink-500 via-purple-600 to-indigo-600 px-8 py-3.5 text-base font-black text-white shadow-xl hover:scale-105 transition-all"',
            'class="w-full sm:w-auto rounded-lg bg-[#7C3AED] hover:bg-[#6D28D9] px-8 py-3.5 text-base font-black text-white shadow-xl transition-all border-none cursor-pointer"'
        ),
        # Reveal and option buttons
        (
            'class="text-xs font-bold px-3 py-1.5 rounded-lg bg-indigo-950 text-slate-350 hover:bg-slate-800 transition-all"',
            'class="text-xs font-bold px-3 py-1.5 rounded-lg bg-[#7C3AED] hover:bg-[#6D28D9] text-white transition-all border-none cursor-pointer"'
        ),
        (
            'class="flex-1 bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs py-2.5 rounded-xl transition-all active:scale-95 shadow"',
            'class="flex-1 bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-bold text-xs py-2.5 rounded-lg transition-all active:scale-95 shadow border-none cursor-pointer"'
        ),
        (
            'class="flex-1 border border-blue-500/30 text-blue-400 hover:bg-blue-500/10 font-bold text-[10px] py-2 rounded-xl transition-all"',
            'class="flex-1 bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-bold text-[10px] py-2 rounded-lg transition-all border-none cursor-pointer"'
        ),
        (
            'class="flex-1 border border-rose-500/30 text-rose-400 hover:bg-rose-500/10 font-bold text-[10px] py-2 rounded-xl transition-all"',
            'class="flex-1 bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-bold text-[10px] py-2 rounded-lg transition-all border-none cursor-pointer"'
        ),
        (
            'class="text-sm font-semibold px-4 py-2 rounded-xl bg-purple-600 hover:bg-purple-500 text-white transition-colors"',
            'class="text-sm font-semibold px-4 py-2 rounded-lg bg-[#7C3AED] hover:bg-[#6D28D9] text-white transition-colors border-none cursor-pointer"'
        ),
        (
            'class="btn-contrast-reveal text-sm font-semibold px-4 py-2 rounded-xl bg-purple-600 hover:bg-purple-500 text-white transition-colors"',
            'class="btn-contrast-reveal text-sm font-semibold px-4 py-2 rounded-lg bg-[#7C3AED] hover:bg-[#6D28D9] text-white transition-colors border-none cursor-pointer"'
        ),
        # Play/pause buttons
        (
            'class="play-pause-btn text-xs font-bold px-4 py-2 rounded-xl bg-purple-600 hover:bg-purple-500 text-white shadow-md transition-colors flex items-center justify-center space-x-1 shrink-0"',
            'class="play-pause-btn text-xs font-bold px-4 py-2 rounded-lg bg-[#7C3AED] hover:bg-[#6D28D9] text-white shadow-md transition-colors flex items-center justify-center space-x-1 shrink-0 border-none cursor-pointer"'
        ),
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
                    print(f"Fixed buttons in: {os.path.relpath(path, src_dir)}")
                    modified_count += 1
                    
    print(f"Total files modified: {modified_count}")

if __name__ == '__main__':
    fix_buttons()

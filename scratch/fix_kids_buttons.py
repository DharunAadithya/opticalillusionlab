import os

def fix_kids_buttons():
    path = 'c:/Users/Amrutha/Documents/opticalillusionlab/src/pages/for-kids.astro'
    
    replacements = [
        (
            'class="kids-action-btn bg-gradient-to-r from-pink-600 to-pink-500 hover:from-pink-500 hover:to-pink-400 text-white font-black text-base px-6 py-3.5 rounded-2xl shadow-xl transition-all hover:scale-105 active:scale-95"',
            'class="kids-action-btn bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-black text-base px-6 py-3.5 rounded-lg shadow-xl transition-all border-none cursor-pointer"'
        ),
        (
            'class="kids-action-btn bg-gradient-to-r from-yellow-600 to-yellow-500 hover:from-yellow-500 hover:to-yellow-400 text-white font-black text-base px-6 py-3.5 rounded-2xl shadow-xl transition-all hover:scale-105 active:scale-95"',
            'class="kids-action-btn bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-black text-base px-6 py-3.5 rounded-lg shadow-xl transition-all border-none cursor-pointer"'
        ),
        (
            'class="poll-btn-tilted bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white font-black text-base px-6 py-3 rounded-2xl flex-1 shadow-md transition-all hover:scale-105 active:scale-95"',
            'class="poll-btn-tilted bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-black text-base px-6 py-3 rounded-lg flex-1 shadow-md transition-all border-none cursor-pointer"'
        ),
        (
            'class="poll-btn-straight bg-gradient-to-r from-cyan-600 to-cyan-500 hover:from-cyan-500 hover:to-cyan-400 text-white font-black text-base px-6 py-3 rounded-2xl flex-1 shadow-md transition-all hover:scale-105 active:scale-95"',
            'class="poll-btn-straight bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-black text-base px-6 py-3 rounded-lg flex-1 shadow-md transition-all border-none cursor-pointer"'
        ),
        (
            'class="kids-submit-dots bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white font-black text-base px-6 py-3 rounded-2xl shadow-lg transition-transform active:scale-95"',
            'class="kids-submit-dots bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-black text-base px-6 py-3 rounded-lg shadow-lg transition-transform border-none cursor-pointer"'
        ),
        (
            'class="kids-start-troxler bg-gradient-to-r from-cyan-600 to-cyan-500 hover:from-cyan-500 hover:to-cyan-400 text-white font-black text-base px-6 py-3.5 rounded-2xl shadow-xl transition-all hover:scale-105 active:scale-95"',
            'class="kids-start-troxler bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-black text-base px-6 py-3.5 rounded-lg shadow-xl transition-all border-none cursor-pointer"'
        ),
        (
            'id="btn-spin-thaumatrope" class="flex-1 bg-gradient-to-r from-pink-600 to-pink-500 hover:from-pink-500 hover:to-pink-400 text-white font-black text-xs py-2 rounded-xl shadow-md transition-all active:scale-95"',
            'id="btn-spin-thaumatrope" class="flex-1 bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-black text-xs py-2 rounded-lg shadow-md transition-all border-none cursor-pointer"'
        ),
        (
            'id="btn-flip-thaumatrope" class="bg-slate-800 hover:bg-slate-700 text-slate-350 font-black text-xs px-3 py-2 rounded-xl border border-slate-700 transition-colors"',
            'id="btn-flip-thaumatrope" class="bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-black text-xs px-3 py-2 rounded-lg border-none transition-colors cursor-pointer"'
        ),
        (
            'id="btn-stare-afterimage" class="w-full bg-gradient-to-r from-purple-600 to-purple-500 hover:from-purple-500 hover:to-purple-400 text-white font-black text-xs py-2 rounded-xl shadow-md transition-all active:scale-95"',
            'id="btn-stare-afterimage" class="w-full bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-black text-xs py-2 rounded-lg shadow-md transition-all border-none cursor-pointer"'
        ),
        (
            'id="restart-quiz-btn" class="bg-gradient-to-r from-pink-500 via-purple-600 to-indigo-600 text-white font-black text-base px-8 py-3.5 rounded-2xl shadow-xl transition-all hover:scale-105 active:scale-95"',
            'id="restart-quiz-btn" class="bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-black text-base px-8 py-3.5 rounded-lg shadow-xl transition-all border-none cursor-pointer"'
        ),
        (
            'class="retry-btn mt-3 bg-slate-800 text-white font-bold text-xs px-3 py-1.5 rounded-lg border border-slate-700"',
            'class="retry-btn mt-3 bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-bold text-xs px-3 py-1.5 rounded-lg border-none cursor-pointer"'
        ),
        (
            'class="retry-btn mt-3 bg-slate-800 text-white font-bold text-xs px-3 py-1.5 rounded-lg border border-slate-700 shadow-sm"',
            'class="retry-btn mt-3 bg-[#7C3AED] hover:bg-[#6D28D9] text-white font-bold text-xs px-3 py-1.5 rounded-lg border-none cursor-pointer shadow-sm"'
        )
    ]
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig = content
    for target, replacement in replacements:
        content = content.replace(target, replacement)
        
    if content != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully fixed kids buttons!")
    else:
        print("No changes needed in for-kids.astro")

if __name__ == '__main__':
    fix_kids_buttons()

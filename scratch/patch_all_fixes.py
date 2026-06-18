import os
import re

workspace_dir = "c:/Users/Amrutha/Documents/opticalillusionlab"
pages_dir = os.path.join(workspace_dir, "src/pages")
illusions_dir = os.path.join(pages_dir, "illusions")

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Starting global updates...")

# ==========================================
# FIX: Double Asterisks in Detail Pages
# ==========================================
files_to_fix_asterisks = [
    "vertical-horizontal.astro",
    "shepard-tables.astro",
    "penrose-stairs.astro",
    "ishihara-test.astro",
    "coffer-illusion.astro"
]

for filename in files_to_fix_asterisks:
    filepath = os.path.join(illusions_dir, filename)
    if os.path.exists(filepath):
        content = read_file(filepath)
        # Replace **something** with <strong>something</strong>
        new_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
        if new_content != content:
            write_file(filepath, new_content)
            print(f"Fixed double asterisks in {filename}")

# ==========================================
# FIX: Timer Fix in for-kids.astro
# ==========================================
kids_path = os.path.join(pages_dir, "for-kids.astro")
if os.path.exists(kids_path):
    content = read_file(kids_path)
    
    # 1. Staring countdown timer in for-kids.astro (Troxler)
    # Target lines: lines 1348-1368
    old_troxler_timer = """        countdownInterval = setInterval(() => {
          secondsLeft--;
          if (troxlerCountdown) {
            troxlerCountdown.textContent = `${secondsLeft}s`;
          }
          
          if (secondsLeft <= 0) {
            clearInterval(countdownInterval);
            troxlerCountdown.classList.add('hidden');
            staringActive = false;
            
            setTimeout(() => {
              troxlerWow?.classList.remove('hidden');
            }, 300);

            if (startTroxlerBtn) {
              startTroxlerBtn.removeAttribute('disabled');
              startTroxlerBtn.textContent = 'Restart';
            }
          }
        }, 1000);"""

    new_troxler_timer = """        const duration = 15000; // 15 seconds
        const startTime = Date.now();
        countdownInterval = setInterval(() => {
          const elapsed = Date.now() - startTime;
          const remaining = Math.max(0, duration - elapsed);
          const secondsLeft = (remaining / 1000).toFixed(1);
          if (troxlerCountdown) {
            troxlerCountdown.textContent = `${secondsLeft}s`;
          }
          
          if (remaining <= 0) {
            clearInterval(countdownInterval);
            troxlerCountdown.classList.add('hidden');
            staringActive = false;
            
            setTimeout(() => {
              troxlerWow?.classList.remove('hidden');
            }, 300);

            if (startTroxlerBtn) {
              startTroxlerBtn.removeAttribute('disabled');
              startTroxlerBtn.textContent = 'Restart';
            }
          }
        }, 100);"""

    # 2. Afterimage countdown timer in for-kids.astro (Kids card 7 / dizzy dots)
    # Target lines: lines 1527-1539
    old_afterimage_timer = """          intervalId = setInterval(() => {
            timerVal--;
            timerBadge.textContent = `${timerVal}s`;
            
            if (timerVal <= 0) {
              clearInterval(intervalId);
              timerBadge.classList.add('hidden');
              svgStar.style.opacity = '0';
              screen.classList.remove('hidden');
              btnStare.textContent = 'Try Stare Again 🔄';
              isStaring = false;
            }
          }, 1000);"""

    new_afterimage_timer = """          const duration = 20000; // 20 seconds
          const startTime = Date.now();
          intervalId = setInterval(() => {
            const elapsed = Date.now() - startTime;
            const remaining = Math.max(0, duration - elapsed);
            const secondsLeft = (remaining / 1000).toFixed(1);
            timerBadge.textContent = `${secondsLeft}s`;
            
            if (remaining <= 0) {
              clearInterval(intervalId);
              timerBadge.classList.add('hidden');
              svgStar.style.opacity = '0';
              screen.classList.remove('hidden');
              btnStare.textContent = 'Try Stare Again 🔄';
              isStaring = false;
            }
          }, 100);"""

    if old_troxler_timer in content:
        content = content.replace(old_troxler_timer, new_troxler_timer)
        print("Patched Troxler timer in for-kids.astro")
    else:
        # Fallback replacement if whitespace differs slightly
        content = re.sub(r'countdownInterval\s*=\s*setInterval\(\(\)\s*=>\s*\{\s*secondsLeft--;.*?\},\s*1000\);', new_troxler_timer, content, flags=re.DOTALL)
        print("Fallback patched Troxler timer in for-kids.astro")

    if old_afterimage_timer in content:
        content = content.replace(old_afterimage_timer, new_afterimage_timer)
        print("Patched dizzy dots timer in for-kids.astro")
    else:
        # Fallback
        content = re.sub(r'intervalId\s*=\s*setInterval\(\(\)\s*=>\s*\{\s*timerVal--;.*?\},\s*1000\);', new_afterimage_timer, content, flags=re.DOTALL)
        print("Fallback patched dizzy dots timer in for-kids.astro")

    write_file(kids_path, content)

print("Timer patches for kids done.")

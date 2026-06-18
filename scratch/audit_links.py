import re
import os

pages_dir = "c:/Users/Amrutha/Documents/opticalillusionlab/src/pages"
report_path = "c:/Users/Amrutha/Documents/opticalillusionlab/scratch/link_audit_report.txt"

files_to_audit = [
    "index.astro",
    "famous.astro",
    "moving.astro",
    "hidden.astro",
    "color.astro",
    "for-kids.astro",
    "test.astro",
    "what-do-you-see.astro"
]

report = []
report.append("=== DETAILED PLATFORM LINK AUDIT REPORT ===\n")

for filename in files_to_audit:
    filepath = os.path.join(pages_dir, filename)
    if not os.path.exists(filepath):
        report.append(f"File not found: {filepath}\n")
        continue
    
    report.append(f"\n--- Auditing file: {filename} ---\n")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Let's find all <a href=...> tags and their close tags </a>
    # We want to capture the tag itself, the href, and some text content
    a_matches = re.finditer(r'<a\s+([^>]*href=["\']([^"\']+)["\'][^>]*)>(.*?)</a>', content, re.DOTALL | re.IGNORECASE)
    
    link_idx = 1
    for match in a_matches:
        full_match = match.group(0)
        attrs = match.group(1)
        href = match.group(2)
        inner_html = match.group(3)
        
        # Clean text
        text = re.sub(r'<[^>]+>', ' ', inner_html).strip()
        text = ' '.join(text.split())
        if len(text) > 80:
            text = text[:80] + "..."
            
        report.append(f"Link {link_idx}: Href = '{href}' | Text = '{text}'\n")
        link_idx += 1

with open(report_path, "w", encoding="utf-8") as f:
    f.writelines(report)

print("Audit completed. Report written to:", report_path)

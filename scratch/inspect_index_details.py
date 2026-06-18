import os

def check(file_path):
    if not os.path.exists(file_path):
        print(f"{file_path} not found")
        return
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"\nOccurrences in {file_path}:")
    print("'Instructions':", content.count("Instructions") or content.count("instructions"))
    print("'details':", content.count("<details"))
    print("'Reveal':", content.count("Reveal") or content.count("reveal"))

check("src/pages/index.astro")
check("src/pages/famous.astro")

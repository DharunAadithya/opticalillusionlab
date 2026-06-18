import os

filepath = "src/pages/index.astro"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for script code that handles ishihara
script_start = content.find("<script>")
if script_start != -1:
    script_content = content[script_start:]
    # Find occurrences of 'ishihara' inside the script
    idx = 0
    while True:
        idx = script_content.lower().find("ishihara", idx)
        if idx == -1:
            break
        print(f"Script match at index {idx}:")
        print(script_content[idx:idx+400].encode('ascii', errors='replace').decode('ascii'))
        idx += len("ishihara")
else:
    print("No script tags found")

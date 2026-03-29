import os

files = ['about.html', 'events.html', 'projects.html', 'units.html', 'newspaper.html', 'blood.html', 'nss-camp.html']

for filename in files:
    path = os.path.join(r"c:\Users\pc\Documents\NSS\NSS Website", filename)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    # Replace potentially obscure grey/dark bootstrap text classes
    content = content.replace('text-secondary', 'text-light opacity-90')
    content = content.replace('text-dark', 'text-white')
    content = content.replace('bg-white', 'cinematic-section')

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed contrast in {filename}")

print("Finish contrast check.")

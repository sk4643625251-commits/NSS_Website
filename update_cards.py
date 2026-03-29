import os

def update_file(filename, replacements):
    path = os.path.join(r"c:\Users\pc\Documents\NSS\NSS Website", filename)
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for old, new in replacements:
        content = content.replace(old, new)
        
    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

# about.html
update_file('about.html', [
    ('background-color: #f8f9fa;', 'background-color: #040F28; color: #fff;'),
    ('background: #fff;', 'background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); color: #fff; border: 1px solid rgba(255,255,255,0.15);'),
    ('<div class="container-fluid py-5 bg-white">', '<div class="container-fluid py-5 cinematic-section">'),
    ('bg-white rounded-4', 'rounded-4 glass-card'),
    ('text-muted', 'text-light opacity-75'),
    ('text-dark', 'text-white'),
    ('bg-light', 'cinematic-section')
])

# events.html
update_file('events.html', [
    ('background-color: #f8f9fa;', 'background-color: #040F28; color: #fff;'),
    ('background: #fff;', 'background: rgba(255, 255, 255, 0.05) !important; backdrop-filter: blur(10px) !important; color: #fff !important; border: 1px solid rgba(255,255,255,0.15) !important;'),
    ('text-muted', 'text-light opacity-75'),
    ('text-dark', 'text-white')
])

# projects.html
update_file('projects.html', [
    ('background-color: #f8fafc;', 'background-color: #040F28; color: #fff;'),
    ('background: #fff;', 'background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); color: #fff; border: 1px solid rgba(255,255,255,0.15);'),
    ('background: #fff !important;', 'background: rgba(255, 255, 255, 0.05) !important; backdrop-filter: blur(10px) !important; color: #fff !important; border: 1px solid rgba(255,255,255,0.15) !important;'),
    ('<div class="p-4 p-md-5 bg-white shadow-sm"', '<div class="p-4 p-md-5 cinematic-section shadow-sm glass-card"'),
    ('text-muted', 'text-light opacity-75'),
    ('text-dark', 'text-white'),
    ('bg-light', 'cinematic-section')
])

# units.html
update_file('units.html', [
    ('background-color: #f8f9fa;', 'background-color: #040F28; color: #fff;'),
    ('<div class="container-fluid bg-white py-6">', '<div class="container-fluid cinematic-section py-6">'),
    ('bg-white', 'cinematic-section'),
    ('bg-light', 'glass-card'),
    ('text-muted', 'text-light opacity-75'),
    ('text-dark', 'text-white')
])

# newspaper.html
update_file('newspaper.html', [
    ('background-color: #f8f9fa;', 'background-color: #040F28; color: #fff;'),
    ('background: white;', 'background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); color: #fff; border: 1px solid rgba(255,255,255,0.15);'),
    ('text-muted', 'text-light opacity-75'),
    ('text-dark', 'text-white'),
    ('bg-light', 'cinematic-section'),
    ('bg-white', 'cinematic-section')
])

# blood.html
update_file('blood.html', [
    ('background-color: #f8f9fa;', 'background-color: #040F28; color: #fff;'),
    ('background: #fff;', 'background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); color: #fff; border: 1px solid rgba(255,255,255,0.15);'),
    ('text-muted', 'text-light opacity-75'),
    ('text-dark', 'text-white'),
    ('bg-white', 'cinematic-section')
])

# nss-camp.html
update_file('nss-camp.html', [
    ('background-color: #f8f9fa;', 'background-color: #040F28; color: #fff;'),
    ('background: #fff;', 'background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); color: #fff; border: 1px solid rgba(255,255,255,0.15);'),
    ('text-muted', 'text-light opacity-75'),
    ('text-dark', 'text-white'),
    ('bg-white', 'cinematic-section')
])

print("Finished applying structural cinematic updates.")

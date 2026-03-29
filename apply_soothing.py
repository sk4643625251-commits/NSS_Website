import os

def apply_soothing(filepath, bg_gradient):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Body Background
    content = content.replace('background-color: #040F28; color: #fff;', f'background: {bg_gradient}; color: #334155;')
    
    # 2. Revert text classes inside cards
    content = content.replace('text-light opacity-75', 'text-muted')
    content = content.replace('text-light opacity-90', 'text-secondary')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated soothing theme for {filepath}")

# Newspaper -> Soothing Lavender/Grey Blue
apply_soothing(
    r"c:\Users\pc\Documents\NSS\NSS Website\newspaper.html", 
    "linear-gradient(135deg, #e8f0fe 0%, #fcfdff 100%)"
)

# NSS Camp -> Soothing Mint
apply_soothing(
    r"c:\Users\pc\Documents\NSS\NSS Website\nss-camp.html", 
    "linear-gradient(135deg, #edf7f0 0%, #fefcfb 100%)"
)

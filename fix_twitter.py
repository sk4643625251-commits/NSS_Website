import os, re

files = [
    'units.html', 'Team.html', 'projects.html', 'nss-camp.html', 
    'nss-camp-2026.html', 'newspaper.html', 'index.html', 
    'events.html', 'blood.html', 'about.html', 'contact.html'
]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace Font Awesome CDN with 6.5.1
    content = re.sub(
        r'<link[^>]*font-awesome/[56]\.\d+\.\d+/css/all\.min\.css[^>]*>', 
        '<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" rel="stylesheet" />', 
        content
    )
    
    # Replace twitter icon and link in the footer
    content = re.sub(
        r'<a class="social-icon" href="[^"]*"><i class="fab fa-twitter"></i></a>', 
        '<a class="social-icon" href="https://x.com/nss_nitkkr" target="_blank"><i class="fa-brands fa-x-twitter"></i></a>', 
        content
    )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Updated all files.")

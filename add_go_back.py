import glob

html_files = glob.glob(r'c:\Users\pc\Documents\NSS\NSS_Website\*.html')
processed_count = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already added
    if 'go-back.css' in content or 'universal-go-back-btn' in content:
        continue

    # Add CSS before </head>
    if '</head>' in content:
        content = content.replace('</head>', '  <!-- Go Back CSS -->\n  <link href="css/go-back.css" rel="stylesheet" />\n</head>')
    
    # Add JS before </body>
    if '</body>' in content:
        content = content.replace('</body>', '  <!-- Go Back JS -->\n  <script src="js/go-back.js"></script>\n</body>')
    
    # Add Button right after <body>
    if '<body' in content:
        # Find end of body tag
        body_end = content.find('>', content.find('<body')) + 1
        button_html = '\n  <!-- Universal Go Back Button -->\n  <button onclick="goBack()" class="universal-go-back-btn"><i class="fa fa-arrow-left"></i> Go back</button>\n'
        content = content[:body_end] + button_html + content[body_end:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    processed_count += 1

print(f"Processed {processed_count} HTML files out of {len(html_files)}.")

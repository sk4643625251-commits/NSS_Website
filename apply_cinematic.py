import os
import re

directory = r"c:\Users\pc\Documents\NSS\NSS Website"

# The new cinematic navbar block
navbar_style = """
  <style>
    /* Cinematic Navbar Upgrade */
    .navbar-glass {
      background: rgba(4, 15, 40, 0.7) !important;
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
      border-bottom: 1px solid rgba(255,255,255,0.1);
      transition: all 0.4s ease;
    }
    .navbar-glass .nav-link { color: #ffffff !important; font-family: 'Inter', sans-serif; font-weight: 500; }
    .navbar-glass .nav-link:hover, .navbar-glass .nav-link.active { color: #0d47a1 !important; }
    .navbar-glass .navbar-brand h2 { color: #ffffff !important; }
    .navbar-glass .navbar-brand p { color: #bbbbbb !important; }
    .navbar-glass .navbar-toggler-icon { filter: invert(1); }
  </style>
"""

navbar_template = navbar_style + """  <nav class="navbar navbar-expand-lg navbar-glass shadow-sm sticky-top py-3 px-4 px-lg-5">
    <a href="index.html" class="navbar-brand d-flex align-items-center">
      <img src="img/home/NSS_Logo.png" alt="NSS Logo" width="45" height="45" class="me-2" onerror="this.src='img/NSS_Logo.png'" />
      <div class="d-flex flex-column text-start justify-content-center">
        <h2 class="m-0 text-dark fs-5 fw-bold" style="font-family: 'Poppins', sans-serif; line-height: 1.2;">National Service Scheme</h2>
        <p class="m-0 text-secondary" style="font-size: 0.85rem; letter-spacing: 0.5px; line-height: 1; font-family: 'Inter', sans-serif;">Kurukshetra</p>
      </div>
    </a>
    <button type="button" class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarCollapse">
      <div class="navbar-nav ms-auto py-0 fw-bold align-items-center">
        <a href="index.html" class="nav-item nav-link">Home</a>
        <a href="about.html" class="nav-item nav-link">About</a>
        <a href="units.html" class="nav-item nav-link">Units</a>
        <a href="events.html" class="nav-item nav-link">Events</a>
        <a href="Team.html" class="nav-item nav-link">Team</a>
        <a href="nss-camp.html" class="nav-item nav-link">NSS Camp</a>
        <a href="projects.html" class="nav-item nav-link">Projects</a>
        <a href="newspaper.html" class="nav-item nav-link">Newspaper</a>
      </div>
      <a href="contact.html#contact" class="btn btn-primary py-2 px-4 ms-lg-3 d-none d-lg-block modern-solid-btn" style="background-color: #0d47a1; border: none; border-radius: 50px;">Contact</a>
      <a href="contact.html#contact" class="btn btn-primary py-2 px-4 mt-2 mb-2 d-lg-none w-100 modern-solid-btn" style="background-color: #0d47a1; border: none; border-radius: 50px;">Contact</a>
    </div>
  </nav>"""

global_styles = """
    <!-- Global Cinematic Variables -->
    <style>
        .cinematic-section {
            background-color: #040F28; /* Deep Navy */
            color: #ffffff;
        }
        .cinematic-heading {
            font-family: 'Poppins', sans-serif;
            color: #ffffff;
            font-weight: 800;
            letter-spacing: 1px;
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.05) !important;
            backdrop-filter: blur(10px) !important;
            -webkit-backdrop-filter: blur(10px) !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            border-radius: 20px !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            color: #fff !important;
        }
        .glass-card:hover {
            transform: translateY(-8px) scale(1.02) !important;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5), 0 0 20px rgba(13, 71, 161, 0.4) !important;
            background: rgba(255, 255, 255, 0.08) !important;
            border: 1px solid rgba(255, 255, 255, 0.3) !important;
        }
    </style>
"""

nav_regex = re.compile(r'<nav class="navbar .*?</nav>', re.DOTALL)
exclude_files = ["index.html", "Team.html"]

for filename in os.listdir(directory):
    if filename.endswith(".html") and filename not in exclude_files:
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update Navbar
        if nav_regex.search(content):
            # Formulate the correct active class for the current file
            new_nav = navbar_template
            target_link = f'href="{filename}" class="nav-item nav-link"'
            active_link = f'href="{filename}" class="nav-item nav-link active"'
            new_nav = new_nav.replace(target_link, active_link)
            content = nav_regex.sub(new_nav, content)
            
        # Inject Global Styles before </head> if not already there
        if "cinematic-section" not in content and "</head>" in content:
            content = content.replace("</head>", global_styles + "\n</head>")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated Navigation and Global Styles for {filename}")

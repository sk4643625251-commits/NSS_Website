import re

with open('index.html', 'r', encoding='utf-8-sig') as f:
    content = f.read()

# Find the Dean slide closing and insert a third slide before the owl carousel closes
# We look for the Dean text which is unique
dean_marker = "I urge students to participate actively and contribute towards nation-building."

third_slide = '''

        <!-- Contributor 3 - loop filler -->
        <div class="item">
          <div class="glass-card p-4 mx-2">
            <div class="row align-items-center justify-content-center">
              <div class="col-md-4 text-center mb-4 mb-md-0">
                <img src="img/home/brahmjit.jpeg" class="img-fluid rounded-circle shadow-lg" alt="Prof. Brahmjit Singh"
                  onerror="this.src=\'img/NSS_Logo.png\'"
                  style="width: 180px; height: 180px; object-fit: cover; object-position: top center; border: 4px solid rgba(255,255,255,0.15); margin: 0 auto; box-shadow: 0 10px 25px rgba(0,0,0,0.5);">
              </div>
              <div class="col-md-8 text-center text-md-start cinematic-body">
                <h5 class="post-holder-name mb-1" style="font-size: 1.5rem;">Prof. Brahmjit Singh</h5>
                <p class="post-holder-role mb-3 text-info" style="font-size: 1.05rem;">Officiating Director | NIT Kurukshetra</p>
                <p class="text-light" style="font-size: 0.95rem; line-height: 1.6;">
                  Welcome to NSS. Our aim is to develop the personality of students through community service and build leadership skills at NIT Kurukshetra.
                </p>
              </div>
            </div>
          </div>
        </div>'''

# Find position of dean marker, then find next closing </div> sequence for the item
idx = content.find(dean_marker)
if idx == -1:
    print("ERROR: Dean marker not found!")
else:
    # Find the </div> chain that closes: </p> </div> </div> </div> </div> (owl-carousel close)
    # After the dean marker, we close: </p>, col-md-8, row, glass-card, item, then owl div
    # Insert before the owl-carousel closing div
    # Find the pattern: last </div>\n      </div>\n    </div>\n  </div> after dean marker
    after_dean = content[idx:]
    
    # The owl carousel closes with </div>\n      </div>  (owl div), then </div> (container), then </div> (section)
    # We want to insert before the 5th closing div after the dean marker
    # Let's find the sequence of closing divs
    # After dean text: </p>\n              </div>\n            </div>\n          </div>\n        </div>\n      </div>
    pattern = '</p>\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n      </div>'
    if pattern in after_dean:
        insert_point = idx + after_dean.index(pattern) + len(pattern) - len('\r\n      </div>')
        content = content[:insert_point] + third_slide + content[insert_point:]
        print("SUCCESS (CRLF): Third contributor slide added!")
    else:
        # Try LF only
        pattern2 = '</p>\n              </div>\n            </div>\n          </div>\n        </div>\n      </div>'
        if pattern2 in after_dean:
            insert_point = idx + after_dean.index(pattern2) + len(pattern2) - len('\n      </div>')
            content = content[:insert_point] + third_slide + content[insert_point:]
            print("SUCCESS (LF): Third contributor slide added!")
        else:
            # Show what's after dean marker
            print("Pattern not found. Content after dean marker:")
            print(repr(after_dean[:300]))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("File saved.")

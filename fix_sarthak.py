import re

# Read the file
with open('about.html', 'r') as f:
    content = f.read()

# Replace Sarthak Singh's icon with image
pattern = r'(<div class="member-avatar">\s*<i class="fas fa-user"></i>\s*</div>\s*<h3>Sarthak Singh</h3>)'
replacement = r'<div class="member-avatar">\n                        <img src="images/sarthak-singh.jpg" alt="Sarthak Singh" class="member-photo">\n                    </div>\n                    <h3>Sarthak Singh</h3>'

content = re.sub(pattern, replacement, content)

# Write back to file
with open('about.html', 'w') as f:
    f.write(content)

print("Sarthak Singh's image added successfully!")

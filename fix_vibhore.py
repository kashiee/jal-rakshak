import re

# Read the file
with open('about.html', 'r') as f:
    content = f.read()

# Replace Vibhore Sharma's icon with image
pattern = r'(<div class="member-avatar">\s*<i class="fas fa-user"></i>\s*</div>\s*<h3>Vibhore Sharma</h3>)'
replacement = r'<div class="member-avatar">\n                        <img src="images/vibhore.jpeg" alt="Vibhore Sharma" class="member-photo">\n                    </div>\n                    <h3>Vibhore Sharma</h3>'

content = re.sub(pattern, replacement, content)

# Write back to file
with open('about.html', 'w') as f:
    f.write(content)

print("Vibhore Sharma's image added successfully!")

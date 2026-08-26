import os

for root, _, files in os.walk('.'):
    if '.git' in root: continue
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            with open(path, 'w', encoding='utf-8') as file:
                for line in lines:
                    if 'data-filter="uiux"' not in line:
                        file.write(line)

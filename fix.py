import os
import glob

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    char = chr(0xFFFD)
    content = content.replace('I' + char + 've', 'I\\'ve')
    content = content.replace('I' + char + 'm', 'I\\'m')
    content = content.replace('don' + char + 't', 'don\\'t')
    content = content.replace('it' + char + 's', 'it\\'s')
    content = content.replace('Designer ' + char + ' Creative', 'Designer | Creative')
    content = content.replace(char + ' 2026', '&copy; 2026')
    content = content.replace(' ' + char + ' ', ' - ')
    content = content.replace(char, '') # remove any remaining
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

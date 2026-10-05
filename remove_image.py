with open('home2.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
c = re.sub(r'<!-- Small floating image top-right -->.*?</div>\s*</div>', '</div>', c, flags=re.DOTALL)

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Removed top right floating image.')

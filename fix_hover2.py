with open('testimonials.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
c = re.sub(r'(\.border-border \{ border-color: var\(--color-border\); \})', 
           r'\1\n            .border-primary-text { border-color: var(--color-primary-text); }\n            .hover\\:bg-primary-text:hover { background-color: var(--color-primary-text); }', 
           c)

with open('testimonials.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed hover CSS with regex')

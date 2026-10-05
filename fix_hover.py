with open('testimonials.html', 'r', encoding='utf-8') as f:
    c = f.read()

style_insert = '''            .text-accent { color: var(--color-accent); }
            .text-accent-light { color: var(--color-accent-light); }
            .bg-background { background-color: var(--color-background); }
            .bg-hover { background-color: var(--color-hover); }
            .bg-accent { background-color: var(--color-accent); }
            .border-primary-text { border-color: var(--color-primary-text); }
            .hover\\:bg-primary-text:hover { background-color: var(--color-primary-text); }'''

if '.border-primary-text' not in c:
    c = c.replace('''            .text-accent { color: var(--color-accent); }
            .text-accent-light { color: var(--color-accent-light); }
            .bg-background { background-color: var(--color-background); }
            .bg-hover { background-color: var(--color-hover); }
            .bg-accent { background-color: var(--color-accent); }''', style_insert)

with open('testimonials.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed hover CSS')

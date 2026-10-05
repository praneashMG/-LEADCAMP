import re

with open('about.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix outer containers
c = c.replace(
    'class="group rounded-2xl overflow-hidden border border-border bg-background shadow-sm hover:shadow-xl transition-all duration-300 hover:-translate-y-2"',
    'class="group rounded-2xl overflow-hidden border border-border bg-background shadow-sm hover:shadow-xl transition-all duration-300 hover:-translate-y-2 flex flex-col h-full"'
)

# Replace the inner block using regex.
# We want to find:
# <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent"></div>
# <div class="absolute bottom-4 left-4 right-4">
#     <p class="text-white font-bold text-base">(.*)</p>
#     <p class="text-accent text-xs font-semibold uppercase tracking-wider">(.*)</p>
# </div>
# </div>
# <div class="p-5">

pattern = r'<div class="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent"></div>\s*<div class="absolute bottom-4 left-4 right-4">\s*<p class="text-white font-bold text-base">(.*?)</p>\s*<p class="text-accent text-xs font-semibold uppercase tracking-wider">(.*?)</p>\s*</div>\s*</div>\s*<div class="p-5">'

replacement = r'''</div>
                <div class="p-5 flex flex-col flex-1">
                    <h3 class="text-primary-text font-bold text-lg mb-1">\1</h3>
                    <p class="text-accent text-xs font-bold uppercase tracking-wider mb-3">\2</p>'''

c = re.sub(pattern, replacement, c)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed team cards in about.html')

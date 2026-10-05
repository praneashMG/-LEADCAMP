with open('contact.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Add flex flex-col h-full to the outer cards
target_outer = 'class="rounded-2xl border border-border bg-background p-6 sm:p-8 shadow-sm hover:shadow-xl transition-all duration-300"'
rep_outer = 'class="rounded-2xl border border-border bg-background p-6 sm:p-8 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col h-full"'
c = c.replace(target_outer, rep_outer)

# Add mt-auto to the bottom contact container
target_bottom = 'class="space-y-3 pt-5 border-t border-border"'
rep_bottom = 'class="space-y-3 pt-5 border-t border-border mt-auto"'
c = c.replace(target_bottom, rep_bottom)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed contact cards in contact.html')

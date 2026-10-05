with open('programs.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('class="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8"', 'class="grid grid-cols-1 lg:grid-cols-3 gap-6 lg:gap-8"')
c = c.replace('class="hidden grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8"', 'class="hidden grid-cols-1 lg:grid-cols-3 gap-6 lg:gap-8"')
c = c.replace('id="seasonal-plans" class="hidden grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8"', 'id="seasonal-plans" class="hidden grid-cols-1 lg:grid-cols-3 gap-6 lg:gap-8"')

c = c.replace('1-on-1 coaching sessions', '1-on-1 coaching')
c = c.replace('Recorded speech reviews', 'Video speech reviews')
c = c.replace('Priority showcase slot', 'Priority showcase')
c = c.replace('Professional photos & video', 'Pro photos & video')

c = c.replace('3 private coaching sessions', '3 private sessions')
c = c.replace('Post-camp follow-up call', 'Post-camp follow-up')

with open('programs.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed programs.html grids and strings')

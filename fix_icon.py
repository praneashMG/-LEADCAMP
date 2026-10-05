with open('home2.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('<i class="fa-solid fa-waveform text-white text-sm"></i>', '<i class="fa-solid fa-volume-high text-white text-sm"></i>')

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed icon')

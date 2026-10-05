with open('testimonials.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('class="flex gap-5 mb-5 animate-marquee"', 'class="flex gap-5 mb-5 animate-marquee w-max"')
c = c.replace('class="flex gap-5 animate-marquee-reverse"', 'class="flex gap-5 animate-marquee-reverse w-max"')

with open('testimonials.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed marquee')

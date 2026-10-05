with open('testimonials.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Remove overflow-hidden from the section
c = c.replace('<section class="relative w-full overflow-hidden bg-background pt-32 pb-12 lg:pb-20">', '<section class="relative w-full bg-background pt-32 pb-12 lg:pb-20">')

# 2. Wrap the decorative blurs in their own absolute full-size container with overflow-hidden
blurs_original = '''    <!-- Decorative blurs -->
    <div class="absolute top-24 -left-40 w-[500px] h-[500px] rounded-full opacity-15 blur-3xl pointer-events-none" style="background: var(--color-accent);"></div>
    <div class="absolute -bottom-32 -right-32 w-[400px] h-[400px] rounded-full opacity-10 blur-3xl pointer-events-none" style="background: var(--color-accent-light);"></div>'''

blurs_fixed = '''    <!-- Decorative blurs -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
        <div class="absolute top-24 -left-40 w-[500px] h-[500px] rounded-full opacity-15 blur-3xl" style="background: var(--color-accent);"></div>
        <div class="absolute -bottom-32 -right-32 w-[400px] h-[400px] rounded-full opacity-10 blur-3xl" style="background: var(--color-accent-light);"></div>
    </div>'''

c = c.replace(blurs_original, blurs_fixed)

# 3. Change grid to flex in the hero container just to be absolutely bulletproof on mobile Safari
grid_original = '<div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-8 items-center">'
grid_fixed = '<div class="flex flex-col lg:flex-row gap-10 lg:gap-8 items-center">'

c = c.replace(grid_original, grid_fixed)

c = c.replace('<div class="lg:col-span-7 text-center lg:text-left">', '<div class="w-full lg:w-7/12 text-center lg:text-left">')
c = c.replace('<div class="lg:col-span-5 relative h-[360px] sm:h-[460px] lg:h-[560px] flex items-center justify-center mt-10 lg:mt-0">', '<div class="w-full lg:w-5/12 relative h-[360px] sm:h-[460px] lg:h-[560px] flex items-center justify-center mt-10 lg:mt-0">')

with open('testimonials.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed hero section')

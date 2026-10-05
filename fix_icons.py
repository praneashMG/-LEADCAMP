with open('programs.html', 'r', encoding='utf-8') as f:
    c = f.read()

starter_target = '''<div class="w-12 h-12 rounded-xl bg-accent/10 flex items-center justify-center mb-5">
                    <i class="fa-solid fa-seedling text-accent text-lg"></i>
                </div>'''
starter_rep = '<img src="https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?w=100&q=80" alt="Starter" class="w-12 h-12 rounded-xl object-cover mb-5 shadow-sm">'

standard_target = '''<div class="w-12 h-12 rounded-xl bg-accent/10 flex items-center justify-center mb-5">
                    <i class="fa-solid fa-star text-accent text-lg"></i>
                </div>'''
standard_rep = '<img src="https://images.unsplash.com/photo-1543269865-cbf427effbad?w=100&q=80" alt="Standard" class="w-12 h-12 rounded-xl object-cover mb-5 shadow-sm">'

premium_target = '''<div class="w-12 h-12 rounded-xl bg-accent/10 flex items-center justify-center mb-5">
                    <i class="fa-solid fa-crown text-accent text-lg"></i>
                </div>'''
premium_rep = '<img src="https://images.unsplash.com/photo-1475721027785-f74eccf877e2?w=100&q=80" alt="Premium" class="w-12 h-12 rounded-xl object-cover mb-5 shadow-sm">'

c = c.replace(starter_target, starter_rep)
c = c.replace(standard_target, standard_rep)
c = c.replace(premium_target, premium_rep)

with open('programs.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Replaced pricing icons with images in programs.html')

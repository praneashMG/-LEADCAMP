import re

with open('home2.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Fix the image cropping for Camper Spotlight
c = c.replace('class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"', 'class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500"')

# 2. Add another testimonial to the right column
new_testimonial = '''                <!-- Testimonial 1 -->
                <div class="rounded-2xl border border-border bg-background p-6 sm:p-7 shadow-sm hover:shadow-lg transition-all duration-300">
                    <div class="flex items-center gap-1 mb-4">
                        <i class="fa-solid fa-star text-accent text-xs"></i>
                        <i class="fa-solid fa-star text-accent text-xs"></i>
                        <i class="fa-solid fa-star text-accent text-xs"></i>
                        <i class="fa-solid fa-star text-accent text-xs"></i>
                        <i class="fa-solid fa-star text-accent text-xs"></i>
                    </div>
                    <p class="text-secondary-text text-sm leading-relaxed italic mb-5">
                        "The coaches are phenomenal. They don't just teach speaking; they build real self-esteem. My daughter came back glowing with pride after her showcase."
                    </p>
                    <div class="flex items-center gap-3">
                        <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=100&q=80" 
                             alt="Parent testimonial" 
                             class="w-10 h-10 rounded-full object-cover">
                        <div>
                            <p class="font-bold text-primary-text text-sm">Elena Roberts</p>
                            <p class="text-secondary-text text-xs">Parent of Camper</p>
                        </div>
                    </div>
                </div>'''

# We want to replace the first testimonial to inject the second one below it.
# Notice I'll also remove the lex-1 from the David Park one since we're adding more content to fill the space naturally.
old_testimonial_start = '''                <!-- Testimonial 1 -->
                <div class="flex-1 rounded-2xl border border-border bg-background p-6 sm:p-7 shadow-sm hover:shadow-lg transition-all duration-300">'''

new_testimonial_start = '''                <!-- Testimonial 1 -->
                <div class="rounded-2xl border border-border bg-background p-6 sm:p-7 shadow-sm hover:shadow-lg transition-all duration-300">'''

if old_testimonial_start in c:
    c = c.replace(old_testimonial_start, new_testimonial_start)
    
    # Now find the end of Testimonial 1 and insert Testimonial 2
    # The end of Testimonial 1 is before <!-- Stats card -->
    split_point = '                <!-- Stats card -->'
    parts = c.split(split_point)
    if len(parts) == 2:
        c = parts[0] + new_testimonial + '\n\n' + split_point + parts[1]
    
with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed spotlight image and added content.')

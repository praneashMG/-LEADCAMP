with open('home2.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update the section classes to remove min-h-screen and just use regular padding or use min-h-[90vh]
c = c.replace(
    '<section class="relative w-full min-h-screen flex items-center overflow-hidden bg-background pt-24">',
    '<section class="relative w-full min-h-[90vh] flex items-center overflow-hidden bg-background pt-28">'
)

# 2. Update the inner container classes to remove the huge pt-32 lg:pt-40 which double-pads the top
c = c.replace(
    '<div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10 pt-32 pb-20 lg:pt-40 lg:pb-28">',
    '<div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10 pb-16 lg:pb-20">'
)

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed home2.html hero section padding')

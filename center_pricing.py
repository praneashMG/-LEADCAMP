with open('programs.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Add text-center to the card wrappers
c = c.replace('transition-all duration-300 flex flex-col h-full"', 'transition-all duration-300 flex flex-col h-full text-center"')
c = c.replace('transition-all duration-300 flex flex-col h-full relative"', 'transition-all duration-300 flex flex-col h-full relative text-center"')

# Add mx-auto to the images (only the pricing images, which have w-12 h-12)
c = c.replace('class="w-12 h-12 rounded-xl object-cover mb-5 shadow-sm"', 'class="w-12 h-12 mx-auto rounded-xl object-cover mb-5 shadow-sm"')

# Update the ul to be inline-block text-left
c = c.replace('class="space-y-3 mb-8 flex-grow"', 'class="space-y-3 mb-8 flex-grow inline-block text-left mx-auto w-max"')

with open('programs.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Centered pricing cards')

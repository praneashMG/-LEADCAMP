with open('home2.html', 'r', encoding='utf-8') as f:
    c = f.read()

bottom_left = '''
                <!-- Small floating image bottom-left -->
                <div class="hidden sm:block absolute -bottom-8 -left-8 w-32 h-32 lg:w-40 lg:h-40 rounded-2xl overflow-hidden shadow-xl border-4 border-background -rotate-6">
                    <img src="https://images.unsplash.com/photo-1544717297-fa95b6ee9643?w=400&q=80" 
                         alt="Group of young speakers" 
                         class="w-full h-full object-cover">
                </div>
'''

c = c.replace('                </div>\n        </div>\n    </div>\n</section>', bottom_left + '            </div>\n        </div>\n    </div>\n</section>')

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Restored left image')

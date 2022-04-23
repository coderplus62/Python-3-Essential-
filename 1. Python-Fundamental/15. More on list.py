school_stuff = ['pen','pencil','eraser','spidol','ruler','correction']
print(school_stuff)

# Manipulate list
# data = 'test'
# for i in data:
#     print(i)

'''
Adding Data
'''
school_stuff.append('book')
print(school_stuff)

school_stuff.extend('bag')
print(school_stuff)

school_stuff.insert(5,'book')
print(school_stuff)

'''
Counting Data
'''
totalBook = school_stuff.count('book')
print('Total book in the list is', totalBook)

'''
Remove Data
'''
school_stuff.remove('book')
print(school_stuff)

'''
Reverse Data
'''

school_stuff.reverse()
print(school_stuff)

'''
Copy Data without changing origin
'''
print(100*'#')
stuff_copy = school_stuff.copy()
stuff_copy.append('laptop')
print(stuff_copy)
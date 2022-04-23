i = 0

# String as iteration
'''
f = 'orange'

for x in f:
    print(x)
    i = i+1
    print(i)
'''

# List as iteration
'''
fruit = ['strawberry','blueberry','melon','banana','apple','mango']

for f in fruit:
    print(f)
    print(len(f))
'''

# For in For

fruit = ['strawberry','blueberry','melon','banana','apple','mango']
color = ['red','blue','green','yellow','maroon','violet']
taste = ['good','bad']

summary = [fruit,color,taste]

for x in summary:
    # print(x)          #print all as lists
    for y in x:
        print(y)      #print all as word
        # for z in y:
            # print(z)  #print all as character


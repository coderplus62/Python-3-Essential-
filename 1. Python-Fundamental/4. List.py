lists =[1,2,3,4,5,6,7,8,9,10]

# access list
sublists1 = lists[3]
sublists2 = lists[-4]

# slice list
sublists3 = lists[1:3]
sublists4 = lists[2:7]

# add sublists
addlist = sublists3 + sublists4

# change content list
#lists[4] = 10
#lists[5:7] = [21,22]
#a = lists

# associate or copy data, not change the original data
a = lists[:]
a[4] = 10

# list on the list
x = [sublists3,sublists4]
y = x[0]
y1 = x[0][1]

# append methode (adding member)
color = ['red', 'green', 'blue']
#print(color)

color.append('violet')
#print(color)

# count the length of the list
length = len(color)
print(length)
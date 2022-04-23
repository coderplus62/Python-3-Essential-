init = 0
print('\n '+10*'#'+' Stack Data '+10*'#'+'\n')

'''
Stack data, last data will appear at first
'''

stack_data = [1,2,3,4,5,6,7]
print('Current data is:', stack_data)

# adding new data
for i in range(8,11):
    stack_data.append(i)
    print(f'Data {i} is recorded')
print('Latest data is:', stack_data)

# remove the last data
'''Using Manual'''
# out = stack_data.pop()
# print('After pop, data is:', stack_data)
# print('Removed data is:', out)

'''Using Loop'''
for i in range(4):
    out = stack_data.pop()
    print(f'Data {out} is removed')
print('\n '+10*'#'+' Queue Data '+10*'#'+'\n')

'''
Queues data, first data will appear at first
'''

from collections import deque

queue = deque([1,2,3,4,5])
print('Queue data is:', queue)

# adding new data
for i in range(6,11):
    queue.append(i)
    print(f'Data {i} is recorded')
print('Latest data is:', queue)

# remove the last data
'''Using Manual'''
# out = queue.popleft()
# print('After popleft, data is:', queue)
# print('Removed data is:', out)

'''Using Loop'''
for i in range(4):
    out = queue.popleft()
    print(f'Data {out} is removed')
print('Latest data is:', queue)
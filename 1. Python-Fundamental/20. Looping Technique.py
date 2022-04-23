init = 0
'''List Name'''

country_name = ['Indonesia',
                'USA',
                'UK',
                'Canada',
                'Germany']
continent_name = ['Asia',
                  'America',
                  'Europe',
                  'America',
                  'Europe']

# using enumerate
print('\n '+10*'#'+' Print country with index '+10*'#'+'\n')

for i,country in enumerate(country_name):   # i = index, country = value
    print(i,'country name:',country)

# zip => join list
print('\n '+10*'#'+' Print country with continent '+10*'#'+'\n')

for country,continent in zip(country_name,continent_name):
    print(country,'is located in continent:',continent)

'''Set Looping'''

profession = {'farmer','army','police','youtuber','tiktoker','lecturer'}

print('\n '+10*'#'+' Print profession in Set '+10*'#'+'\n')

for job in profession:
    print(job)

print('\n '+10*'#'+' Print profession in Set with sorted string '+10*'#'+'\n')

for job in sorted(profession):
    print(job)

'''Dictionary Looping'''
country_data = {'Indonesia':'Asia',
                'USA':'America',
                'UK':'Europe',
                'Canada':'America',
                'Germany':'Europe'}

print('\n '+10*'#'+' Print country in Dictionary '+10*'#'+'\n')
for i in country_data.keys():
    print(i)
print('\n')
for i in country_data.values():
    print(i)
print('\n')
for i in country_data.items():
    print(i)
print('\n')
for i,j in country_data.items():
    print(f'Country {i} in {j} continent')
print('\n')
for i,j in reversed(country_data.items()):
    print(f'Country {i} in {j} continent')

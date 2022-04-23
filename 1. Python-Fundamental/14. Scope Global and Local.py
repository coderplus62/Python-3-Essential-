# Scope variable: Local
# not changing the original data
address = 'Bali'
district = 'Panbar'

'''
def changeAddress(newAddress):
    address = newAddress
    print('My new address is', address)

changeAddress('Jakarta')
print('My address is', address)
print('\n '+10*'#'+' Transition '+10*'#')
'''

# Scope variable: Global
# changing the original data

def changeAddress(newAddress):
    global address
    address = newAddress # Global variable
    old = newAddress     # local variable
    #print('My new address is', address)

def changeDistrict(prov,dist):
    global address,district
    address = prov
    district = dist

changeAddress('Jakarta')
changeDistrict(address, 'Pantim')
print('My new address is located in', address,'spesifically in', district)


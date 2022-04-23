class Ultraman():
    pass

u1 = Ultraman()
u2 = Ultraman()
u3 = Ultraman()

u1.name = 'Nexus'
u1.hp = 125

u2.name = 'Gaia'
u2.hp = 120

u3.name = 'Zero'
u3.hp = 130

print(u1)
print(u1.__dict__)
print(u1.name)
print(u1.hp)

print(u2)
print(u2.__dict__)
print(u2.name)
print(u2.hp)

print(u3)
print(u3.__dict__)
print(u3.name)
print(u3.hp)
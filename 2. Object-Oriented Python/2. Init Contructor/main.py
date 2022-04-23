class Ultraman():
    def __init__(self,in_name,in_hp,in_defense,in_attack):
        self.name = in_name
        self.hp = in_hp
        self.defense = in_defense
        self.attack = in_attack

u1 = Ultraman('Nexus',125,40,70)  
u2 = Ultraman('Gaia',130,60,75)  
u3 = Ultraman('Zero',120,35,90)  

heroes = [u1,u2,u3]

for i in heroes:
    print(i)
    print(i.__dict__)
    print(i.name)
    print(i.hp)

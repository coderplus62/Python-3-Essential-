class Ultraman():
    class_var = 0
    def __init__(self,in_name,in_hp,in_defense,in_attack):
        self.name = in_name
        self.hp = in_hp
        self.defense = in_defense
        self.attack = in_attack
        Ultraman.class_var += 1
        print("Ultraman",in_name,'has been born')

u1 = Ultraman('Nexus',125,40,70)  
print('Number of Ultraman:',Ultraman.class_var)
u2 = Ultraman('Gaia',130,60,75)
print('Number of Ultraman:',Ultraman.class_var)
u3 = Ultraman('Zero',120,35,90)  
print('Number of Ultraman:',Ultraman.class_var)




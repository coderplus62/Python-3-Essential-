class Ultraman:
    #class variable
    class_var = 0

    def __init__(self,in_name,in_hp,in_defense,in_attack):
        self.name = in_name
        self.hp = in_hp
        self.defense = in_defense
        self.attack = in_attack
        Ultraman.class_var += 1

    # void function, method without arg and return
    def identity(self):
        print(self.name)
        print(self.hp)
        print(self.defense)
        print(self.attack)

    # method with arg
    def hp_booster(self,hp):
        self.hp += hp
        print(self.name, 'get extra hp:',hp)
   
    # method with return
    def hp_info(self):
        print('total hp:',self.hp)

u1 = Ultraman('Nexus',125,40,70) 
u2 = Ultraman('Gaia',130,60,75)
u3 = Ultraman('Zero',120,35,90)

heroes = [u1,u2,u3]

for i in heroes:
    i.identity()
    i.hp_booster(50)
    i.hp_info()

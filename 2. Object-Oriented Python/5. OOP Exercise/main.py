class Ultraman:

    def __init__(self,name,in_hp,in_attack,in_defense):
        self.name = name
        self.hp = in_hp
        self.attack_power = in_attack
        self.defense_power = in_defense
    
    def attack(self, enemy):
        print(self.name, 'is attacking', enemy.name)
        enemy.attacked(self, self.attack_power)

    def attacked(self, enemy, attack_power_enemy): 
        print(self.name, 'is attacked by',enemy.name)
        get_attack = attack_power_enemy/self.defense_power
        self.hp -= get_attack    
        print('Get attact:', str(get_attack)) 
        print(self.name, 'has hp:', self.hp,'\n')

Nexus = Ultraman('Nexus',150,80,50)
Gaia = Ultraman('Gaia',145,85,40)
Zero = Ultraman('Zero',155,70,40)

# Nexus.attack(Gaia)
while Gaia.hp > 0 or Nexus.hp >0:
    Gaia.attack(Nexus)
    Nexus.attack(Gaia)
if Nexus.hp > Gaia.hp:
    print('Nexus is win')
else:
    print('Gaia is win')


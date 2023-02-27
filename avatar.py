class Avatar():
    def __init__(self):
        self.name = str
        self.life = int
        self.strength = int
        self.defense = int
        self.weapon = None
        self.armor = None
        
    def get_life(self):
        return self.life
    
    def set_life(self, inputLife):
        self.life = inputLife    
    
    def get_name(self):
        return self.name
    
    def set_name(self, inputName):
        self.name = inputName

    def get_strength(self):
        return self.strength

    def set_strength(self, inputStrength):
        self.strength = inputStrength
    
    def get_defense(self):
        return self.defense

    def set_defense(self, inputDefense):
        self.defense = inputDefense

    def get_weapon(self):
        return self.weapon
    
    def get_armor(self):
        return self.armor

    def set_armor(self, inputArmor):
        self.armor = inputArmor
        
    def attack(self):
        print() #TODO
        
    def defend(self):
        print() #TODO

class Melee():
    print()# TODO
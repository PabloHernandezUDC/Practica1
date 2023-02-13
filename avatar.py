class avatar():
    def __init__(self):
        self.name = str
        self.life = int
        self.strength = int
        self.defense = int
        # TODO. prueba
        self.weapon = {'Weapon': None}
        self.armor = {'Armor': None}
        
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

    # TODO: acabar las subclases weapon y covering
    def get_weapon(self):
        return self.weapon
    
    def get_armor(self):
        return self.armor


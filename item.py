class Item():
    def __init__(self, name):
        self.name = name
        
class Weapon(Item):
    def __init__(self, name):
        super().__init__(name)
        self.power = int
    def get_power(self):
        return self.power
    def set_power(self, inputPower):
        self.get_power = inputPower
    
class Sword(Weapon):
    def __init__(self, name, power):
        super().__init__(name, power)

class Wand(Weapon):
    def __init__(self, name, power):
        super().__init__(name, power)
        
class Covering(Item):
    def __init__(self, name, protection = None):
        super().__init__(name)
        if protection != None:
            self.protection = protection
        else:
            self.protection = None
    def get_protection(self):
        return self.protection
    def set_protection(self, inputProtection):
        self.protection = inputProtection
    
class Armor(Covering):
    def __init__(self, name, protection):
        super().__init__(name, protection)
        
class Shield(Covering):
    def __init__(self, name, protection):
        super().__init__(name, protection)
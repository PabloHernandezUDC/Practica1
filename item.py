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
    def __init__(self, power):
        super().__init__(power)

class Wand(Weapon):
    def __init__(self, power):
        super().__init__(power)
        
class Covering(Item):
    def __init__(self, name):
        super().__init__(name)
        self.protection = int
    def get_protection(self):
        return self.protection
    def set_protection(self, inputProtection):
        self.protection = inputProtection
    
class Armor(Covering):
    def __init__(self, protection):
        super().__init__(protection)
        
class Shield(Covering):
    def __init__(self, protection):
        super().__init__(protection)
class item():
    def __init__(self, name):
        self.name = name
        
class weapon(item):
    def __init__(self, name):
        super().__init__(name)
        self.power = int
    def get_power(self):
        return self.power
    def set_power(self, inputPower):
        self.get_power = inputPower
    
class sword(weapon):
    def __init__(self, power):
        super().__init__(power)

class wand(weapon):
    def __init__(self, power):
        super().__init__(power)
        
class covering(item):
    def __init__(self, name):
        super().__init__(name)
        self.protection = int
    def get_protection(self):
        return self.protection
    def set_protection(self, inputProtection):
        self.protection = inputProtection
    
class armor(covering):
    def __init__(self, protection):
        super().__init__(protection)
        
class shield(covering):
    def __init__(self, protection):
        super().__init__(protection)
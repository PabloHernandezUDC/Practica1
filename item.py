class item():
    class weapon():
        def __init__(self):
            self.power = int
            
        def get_power(self):
            return self.power
        
        def set_power(self, inputPower):
            self.get_power = inputPower
        
        class sword():
            def __init__(self):
                self.name = str
            def get_name(self):
                return self.name
            def set_name(self, inputName):
                self.name = inputName

        class wand():
            def __init__(self):
                self.name = str
            def get_name(self):
                return self.name
            def set_name(self, inputName):
                self.name = inputName

    class covering():
        def __init__(self):
            self.protection = int
            
        def get_protection(self):
            return self.protection
        
        def set_protection(self, inputProtection):
            self.protection = inputProtection
        
        class armor():
            def __init__(self):
                self.name = str
            def get_name(self):
                return self.name
            def set_name(self, inputName):
                self.name = inputName

        class shield():
            def __init__(self):
                self.name = str
            def get_name(self):
                return self.name
            def set_name(self, inputName):
                self.name = inputName    
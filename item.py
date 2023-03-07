class Item():
    '''
    This class serves as a parent class for Weapon and Covering subclasses.
    
    Attributes
    ----------
    name: str
        Indicates the name of the object.   
    
   Methods
   -------
   __init__(self, name):
        Initializes the values for all attributes considering the arguments given.
    '''
    def __init__(self, name):
        '''
        This method initializes the attributes based on the arguments given.
        
        Parameters
        ----------
        name: str
            States the name of the object.
        
        Return
        ------
        None
        '''
        self.name = name
        
class Weapon(Item):
    '''
    This is an Item subclass which introduces new attributes related to damage.
    
    Attributes
    ----------
    name: str
        Indicates the name of the object.
    power: int
        Indicates the power of the weapon. This is used in damage calculations.   
    
   Methods
   -------
   __init__(self, name, power):
        Initializes the values for all attributes considering the arguments given.
        name is inherited from the parent class.
        
    get_power(self):
        Returns the current value of the power attribute.
        
    set_power(self, inputPower):
        Sets the value of power to inputPower.      
    '''
    def __init__(self, name, power = None):
        '''
        This method initializes the attributes based on the arguments given.
        
        Parameters
        ----------
        name: str
            States the name of the object.
        power: int
            States the object's power, used for damage calculations.
        
        Return
        ------
        None
        '''
        super().__init__(name)
        if power != None:
            self.power = power
        else:
            self.power = int
    def get_power(self):
        '''
        Returns the current value of the power attribute.
        
        Parameters
        ----------
        self
        
        Return
        ------
        power: int
            Current value of power.
        '''
        return self.power
    def set_power(self, inputPower):
        '''
        Sets the value of power to inputPower.      
        
        Parameters
        ----------
        self
        inputPower:
            This argument will be used to set the new value for power.
        
        Return
        ------
        None
        '''
        self.power = inputPower
    
class Sword(Weapon):
    '''
    This is a Weapon subclass.
    
    Attributes
    ----------
    name: str
        Indicates the name of the object.
    power: int
        Indicates the power of the weapon. This is used in damage calculations.   
    
   Methods
   -------
   __init__(self, name, power):
        Initializes the values for all attributes considering the arguments given.
        name and power are inherited from the parent class.   
    '''
    def __init__(self, name, power):
        '''
        This method initializes the attributes based on the arguments given.
        
        Parameters
        ----------
        self
        name: str
            States the name of the object.
        power: int
            States the object's power, used for damage calculations.
        
        Return
        ------
        None
        '''
        super().__init__(name, power)

class Wand(Weapon):
    '''
    This is a Weapon subclass.
    
    Attributes
    ----------
    name: str
        Indicates the name of the object.
    power: int
        Indicates the power of the weapon. This is used in damage calculations.   
    
   Methods
   -------
   __init__(self, name, power):
        Initializes the values for all attributes considering the arguments given.
        name and power are inherited from the parent class.   
    '''

    def __init__(self, name, power):
        '''
        This method initializes the attributes based on the arguments given.
        power is inherited from the parent class.
        
        Parameters
        ----------
        self
        name: str
            States the name of the object.
        power: int
            States the object's power, used for damage calculations.
        
        Return
        ------
        None
        '''
        super().__init__(name, power)
        
class Covering(Item):
    '''
    This is an Item subclass which introduces new attributes related to protection.
    
    Attributes
    ----------
    name: str
        Indicates the name of the object.
    protection: int
        Indicates the protection of the covering. This is used in damage calculations.   
    
   Methods
   -------
   __init__(self, name, protection):
        Initializes the values for all attributes considering the arguments given.
        name is inherited from the parent class.
        
    get_protection(self):
        Returns the current value of the protection attribute.
        
    set_protection(self, inputProtection):
        Sets the value of protection to inputProtection.      
    '''
    def __init__(self, name, protection = None):
        '''
        This method initializes the attributes based on the arguments given.
        
        Parameters
        ----------
        self
        name: str
            States the name of the object.
        protection: int
            States the object's protection, used for damage calculations.
        
        Return
        ------
        None
        '''
        super().__init__(name)
        if protection != None:
            self.protection = protection
        else:
            self.protection = None
    def get_protection(self):
        '''
        Returns the current value of the protection attribute.
        
        Parameters
        ----------
        self
        protection: int
            States the object's protection, used for damage calculations.
        
        Return
        ------
        int
            Current value of protection.
        '''
        return self.protection
    def set_protection(self, inputProtection):
        '''
        Sets the value of protection to inputProtection.      
        
        Parameters
        ----------
        self
        inputProtection:
            This argument will be used to set the new value for protection.
        
        Return
        ------
        None
        '''
        self.protection = inputProtection
    
class Armor(Covering):
    '''
    This is a Covering subclass.
    
    Attributes
    ----------
    name: str
        Indicates the name of the object.
    protection: int
        Indicates the protection of the Covering. This is used in damage calculations.   
    
   Methods
   -------
   __init__(self, name, protection):
        Initializes the values for all attributes considering the arguments given.
        name and protection are inherited from the parent class.   
    '''
    def __init__(self, name, protection):
        '''
        This method initializes the attributes based on the arguments given.
        
        Parameters
        ----------
        self
        name: str
            States the name of the object.
        protection: int
            States the object's protection, used for damage calculations.
        
        Return
        ------
        None
        '''
        super().__init__(name, protection)
        
class Shield(Covering):
    '''
    This is a Covering subclass.
    
    Attributes
    ----------
    name: str
        Indicates the name of the object.
    protection: int
        Indicates the protection of the object. This is used in damage calculations.   
    
   Methods
   -------
   __init__(self, name, protection):
        Initializes the values for all attributes considering the arguments given.
        name and protection are inherited from the parent class.   
    '''

    def __init__(self, name, protection):
        '''
        This method initializes the attributes based on the arguments given.
        
        Parameters
        ----------
        self
        name: str
            States the name of the object.
        protection: int
            States the object's protection, used for damage calculations.
        
        Return
        ------
        None
        '''
        super().__init__(name, protection)
import random as rd

from item import *

class Avatar():
    """
    This class serves as a parent of the melee and caster subclasses.

    Attributes
    ----------
    name: str
    It stores the name of the character.

    life: float
    Reflects the remaining health of the character.

    strength: int
    Reflects the strength attribute of the character.

    defense: int
    Tells the value of the defense attribute of the character.

    weapon: Weapon
    Determines the weapon that the character is carrying.

    armor: Armor
    Determines the armor that the character is wearing.

    Methods
    -------
    get_life():
    Returns the life value of the character.

    set_life(inputLife):
    Sets the life value of the character a certain number.

    get_name():
    Returns the name of the character.

    set_name(inputName):
    Sets the name of the character to a certain string.

    get_strength():
    Returns the strength value of the character.

    set_strength(inputStrength):
    Sets the strength of the character to a certain value.

    get_defense():
    Returns the defense value of the character.

    set_defense(inputDefense):
    Sets the defense stat of the character to a certain value

    get_weapon():
    Returns the weapon that the character is using.

    set_weapon(Weapon):
    Assigns a weapon to the character.

    get_armor():
    Returns the armor that the character is equipped with.

    set_armor(Armor):
    Assigns an armor to the character.

    attack().
    This method is defined in a lower subclass.

    defend().
    This method is defined in a lower subclass.
    """

    def __init__(self, name, life, strength, defense, weapon = None, armor = None):
        '''
        This method initializes the attributes based on the arguments given.
        
        Parameters
        ----------
        name: str
            States the name of the character.
        life: int
            States the life attribute of the character, later used in combat.

        strength : int
            States the strenght attribute of the character, used for damage calculations in combat.
        defense : int
            States the defense attribute of the character, used for damage calculations in combat.

        weapon : Weapon
            States the weapon that the character is carrying, used for damage calculations in combat.
        armor : Armor
            States the armor that the character is wearing, used for damage calculations in combat.
        
        Returns
        -------
        None    
        '''
        self.name = name
        self.life = life
        self.strength = strength
        self.defense = defense
        if weapon != None:
            self.weapon = weapon
        else:
            self.weapon = Weapon
        if armor != None:
            self.armor = armor
        else:
            self.armor = Armor
        
    def get_life(self):
        '''
        Returns the life value of the character.
        
        Parameters
        ----------
        self

        Returns
        ----------
        float
            Current value of life.
        '''
        return self.life
    
    def set_life(self, inputLife):
        '''
        Sets the life attribute to a certain value.
        
        Parameters
        ----------
        self
        inputLife: float
            This is the new value to which the life has to be set.

        Returns
        ----------
        None
        
        '''
        self.life = inputLife          
    
    def get_name(self):
        '''
        Returns the name of the character.
        
        Parameters
        ----------
        self
 
        Returns
        ----------
        str
            Returns name.
        
        '''
        return self.name
    
    def set_name(self, inputName):
        '''
        Changes the name of the character.
        
        Parameters
        ----------
        self
        inputName: str
            This is the name which we want to give to the character.
            
        Returns
        -------
        None
        '''
        self.name = inputName
        
    def get_strength(self):
        '''
        Returns the strength value of the character.
        
        Parameters
        ----------
        self
    
        Returns
        -------
        int
            This is the strength value of the character.
        '''
        return self.strength

    def set_strength(self, inputStrength):
        '''
        Changes the strength value of the character.
        
        Parameters
        ----------
        self
        inputStrength: int
            This is the strength which we want to give to the character.
            
        Returns
        -------
        None
        '''
        self.strength = inputStrength
    
    def get_defense(self):
        '''
        Returns the defense value of the character.
        
        Parameters
        ----------
        self
        
        Returns
        -------
        int
            This is the defense value of the character.
        '''
        return self.defense

    def set_defense(self, inputDefense):
        '''
        Changes the defense value of the character.
        
        Parameters
        ----------
        self
        inputDefense: int
            This is the defense value which we want to give to the character.

        Returns
        --------
        None
        '''
        self.defense = inputDefense

    def get_weapon(self):
        ''' get_weapon(self):
        Returns the character's weapon.
        
        Parameters
        ----------
        self
        
        Returns
        ----------
        Weapon
            This is the weapon which the character is carrying.
        '''
        return self.weapon
    
    def get_armor(self):
        ''' get_armor(self):
        Returns the Armor of the character.
        
        Parameters
        ----------
        self
        
        Returns
        ----------
        Armor
            This is the Armor which the character is wearing.
        '''

        return self.armor

    def set_armor(self, inputArmor):
        '''
        Equips a certain armor piece to the character.
        
        Parameters
        ----------
        self
        inputArmor : Armor
            This is the new armor that the character will be wearing.
        
        Returns
        ----------
        None
        
        '''
        self.armor = inputArmor
        
    def attack(self):
        '''
        Explained in another subclass
        '''
        pass
        
        
    def defend(self):
        '''
        Explained in another subclass
        '''
        pass

class Melee(Avatar):
    """
    This class serves as a parent of the Warrior subclass.

    Attributes
    ----------
    name: str
    It stores the name of the character.

    life: float
    Reflects the remaining health of the character.

    strength: int
    Reflects the strength attribute of the character.

    defense: int
    Tells the value of the defense attribute of the character.

    weapon: Weapon
    Determines the weapon that the character is carrying.

    armor: Armor
    Determines the armor that the character is wearing.
    
    shield: Shield
    This represents the Shield object that the character is using. Otherwise, it defaults to Shield.

    Methods
    -------
    get_shield():
    Returns the Shield of the character.

    set_shield(inputShield):
    Sets the Shield of the character to a certain object.
    """

    def __init__(self, name, life, strength, defense, weapon = None, armor = None, shield = None):
        '''
        This method initializes the attributes based on the arguments given.
        
        Parameters
        ----------
        name: str
            States the name of the character.
        life: int
            States the life attribute of the character, later used in combat.

        strength : int
            States the strenght attribute of the character, used for damage calculations in combat.
        defense : int
            States the defense attribute of the character, used for damage calculations in combat.

        weapon : Weapon
            States the weapon that the character is carrying, used for damage calculations in combat.
        armor : Armor
            States the armor that the character is wearing, used for damage calculations in combat.
        shield : Shield
            States the shield that the character is carrying, used for damage calculations in combat.
        
        Returns
        -------
        None    
        '''
        super().__init__(name, life, strength, defense, weapon, armor)
        if shield != None:
            self.shield = shield
        else:
            self.shield = Shield
    
    def get_shield(self):
        ''' get_shield(self):
        Returns the Armor of the character.
        
        Parameters
        ----------
        Self : Shield
        
    



        Returns
        ----------
        Shield
            This is the shield which the character is carrying.
        
        '''


        return self.shield
    
    def set_shield(self, inputShield):
        ''' set_shield(self, inputShield):
        Sets a shield to the character.
        
        Parameters
        ----------
        Self : Shield

        inputShield : Shield
            This is the new shield that the character will be equipped with.
        
    



        Returns
        ----------
        None
        
        '''
        self.shield = inputShield

    

    
    def set_weapon(self, inputWeapon):
        ''' set_weapon(self, inputWeapon):
        Sets a weapon to the character.
        
        Parameters
        ----------
        Self : Weapon

        inputWeapon : Weapon
            This is the new weapon that the character will be equipped with.
        
    



        Returns
        ----------
        None
        
        '''
        self.weapon = inputWeapon

class Warrior(Melee):
    def __init__(self, name, life, strength, defense, weapon = None, armor = None, shield = None, fury = None):
        '''
        This method initializes the attributes based on the arguments given.
        
        Parameters
        ----------
        name: str
            States the name of the character.
        life: int
            States the life attribute of the character, later used in combat.

        strength : int
            States the strenght attribute of the character, used for damage calculations in combat.
        defense : int
            States the defense attribute of the character, used for damage calculations in combat.

        weapon : Weapon
            States the weapon that the character is carrying, used for damage calculations in combat.
        armor : Armor
            States the armor that the character is wearing, used for damage calculations in combat.
        shield : Shield
            States the shield that the character is carrying, used for damage calculations in combat.
        fury : int
            States the fury value of the character, later used for damage calculations in combat.
        
        Returns
        -------
        None    
        '''
        super().__init__(name, life, strength, defense, weapon, armor, shield)

        if fury != None:
            self.fury = fury
        else:
            self.fury = int
        
    def get_fury(self):
        ''' get_fury(self):
        Returns the fury value of the character.
        
        Parameters
        ----------
        Self : int
        
    



        Returns
        ----------
        int
            This is the fury value of the character.
        
        '''
        return self.fury

    
    def set_fury(self, inputFury):
        ''' set_weapon(self, inputWeapon):
        Sets a weapon to the character.
        
        Parameters
        ----------
        Self : Weapon

        inputWeapon : Weapon
            This is the new weapon that the character will be equipped with.
        
    



        Returns
        ----------
        None
        
        '''
        self.fury = inputFury
        
    def attack(self):
        if self.get_weapon() != Weapon:
            return self.strength + self.get_weapon().get_power() + rd.randint(0, self.fury)
        else:
            return self.strength + rd.randint(0, self.fury)
            
    def defend(self):
        result = 0
        if self.get_armor() != Armor:
            result += self.get_armor().get_protection()
        elif self.get_shield() != Shield:
            result += self.get_shield().get_protection()
        return result + self.get_defense()

class Caster(Avatar):
    def __init__(self, name, life, strength, defense, weapon, armor, mana = None):
        super().__init__(name, life, strength, defense, weapon, armor)
        self.mana = mana
    
    def get_mana(self):
        return self.mana
    
    def set_mana(self, inputMana):
        self.mana = inputMana
    
    def set_weapon(self, inputWeapon):
        self.weapon = inputWeapon
        
class Mage(Caster):
    def __init__(self, name, life, strength, defense, weapon, armor, mana):
        super().__init__(name, life, strength, defense, weapon, armor, mana)
        
    def attack(self):
        # 50% de las veces añade 2 de mana
        # 50% de las veces no añade mana
        coinFlip = rd.randint(0, 1)
        if coinFlip == 0:
            self.mana += 2
                
        if self.mana > 0 and self.get_weapon() != Weapon:   
            dmg = self.strength + self.get_weapon().get_power()
            self.mana -= 1
        else:
            dmg = self.strength + 1
        return dmg

    def defend(self):
        if self.get_armor() != Armor:
            return self.get_defense() + self.get_armor().get_protection()
        else:
            return self.get_defense()
        
class Priest(Caster):
    def __init__(self, name, life, strength, defense, weapon, armor, mana):
        super().__init__(name, life, strength, defense, weapon, armor, mana)
        
    def attack(self):
        coinFlip = rd.randint(0, 1)
        if coinFlip == 0:
            self.mana += 2
                
        if self.mana > 0 and self.get_weapon() != Weapon:   
            dmg = self.strength + self.get_weapon().get_power()
            self.mana -= 1
        else:
            dmg = self.strength + 1
        return dmg

    def defend(self):
        if self.get_armor() != Armor:
            return self.get_defense() + self.get_armor().get_protection()
        else:
            return self.get_defense()
        
    def heal(self):
        coinFlip = rd.randint(0, 1)
        if coinFlip == 0:
            self.mana += 2
                
        if self.mana > 2 and self.get_weapon() != Weapon:   
            heal = (self.strength + self.get_weapon().get_power()) / 2
            self.mana -= 2
        else:
            heal = 0
        
        self.set_life(self.life + heal)
        
        return heal
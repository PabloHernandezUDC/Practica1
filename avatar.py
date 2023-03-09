# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
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
        -------
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
        -------
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
        -------
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
        -------
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
        -------
        Weapon
            Returns self.weapon.
        '''
        return self.weapon
    
    def get_armor(self):
        ''' get_armor(self):
        Returns the Armor of the character.
        
        Parameters
        ----------
        self
        
        Returns
        -------
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
        Abstract method. Implemented in a lower subclass.
        '''
        pass
          
    def defend(self):
        '''
        Abstract method. Implemented in a lower subclass.
        '''
        pass

class Melee(Avatar):
    '''
    This class serves as a parent for the Warrior subclass.

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
    Sets the shield of the character to a certain Shield object.
    '''

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
        '''
        Returns the Shield of the character.
        
        Parameters
        ----------
        self
        
        Returns
        -------
        Shield
            This is the shield which the character is carrying.
        '''
        return self.shield
    
    def set_shield(self, inputShield):
        '''
        Changes the equipped shield of the character.
        
        Parameters
        ----------
        self        
        inputShield : Shield
            This is the new shield that the character will be equipped with.
        
        Returns
        -------
        None
        '''
        self.shield = inputShield

    def set_weapon(self, inputWeapon):
        '''
        Equips a weapon to the character.
        
        Parameters
        ----------
        self

        inputWeapon : Weapon
            This is the new weapon that the character will be equipped with.
        
        Returns
        -------
        None
        '''
        self.weapon = inputWeapon

class Warrior(Melee):
    '''
    This class implements combat mechanics exclusive to the Warrior class.

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
    
    fury: int
    This is used in combat calculations, and is passed as an argument.

    Methods
    -------
    get_fury():
    Returns the current fury value of the character.

    set_fury(inputFury):
    Sets the shield of the character to a certain Shield object.
    
    attack():
    Calculates and returns the damage that the Warrior would deal in the combat simulation.
    
    defend():
    Calculates and returns the defense points that the Warrior would have in the combat simulation.
    '''

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
        '''
        Returns the fury value of the character.
        
        Parameters
        ----------
        self
        
        Returns
        -------
        int
            This is the fury value of the character.
        '''
        return self.fury

    def set_fury(self, inputFury):
        '''
        Sets the character's fury value to inputFury.
        
        Parameters
        ----------
        self
        inputFury : int
            This is the new value for fury.
        
        Returns
        -------
        None
        '''
        self.fury = inputFury
        
    def attack(self):
        '''
        Returns the attack points of the character.
        This is calculated using current strength and fury values;
        if the Warrior currently has a Weapon equipped, that will be added too.
        
        Parameters
        ----------
        self
        
        Returns
        -------
        int
            Returns the attack points of the character.
        '''
        if self.get_weapon() != Weapon:
            return self.strength + self.get_weapon().get_power() + rd.randint(0, self.fury)
        else:
            return self.strength + rd.randint(0, self.fury)
            
    def defend(self):
        '''
        Returns the defense points of the character.
        This is calculated using the current defense value;
        if the Warrior currently has an Armor equipped, that will be added too.
        if the Warrior currently has a Shield equipped, that will be added too.
        
        Parameters
        ----------
        self
        
        Returns
        -------
        int
            Returns the defense points of the character.
        '''
        result = 0
        if self.get_armor() != Armor:
            result += self.get_armor().get_protection()
        if self.get_shield() != Shield:
            result += self.get_shield().get_protection()
        return result + self.get_defense()

class Caster(Avatar):
    '''
    This class serves as a parent for the Mage and Priest subclasses.

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
    
    mana: int
    This is a dynamic value used in combat calculations.
    
    Methods
    -------
    get_shield():
    Returns the Shield of the character.

    set_shield(inputShield):
    Sets the shield of the character to a certain Shield object.
    '''

    def __init__(self, name, life, strength, defense, weapon, armor, mana = None):
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
        mana: int
            Used in combat calculations.
        
        Returns
        -------
        None    
        '''
        super().__init__(name, life, strength, defense, weapon, armor)
        self.mana = mana
    
    def get_mana(self):
        '''
        Returns the mana value of the character.
        
        Parameters
        ----------
        self
        
        Returns
        -------
        int
            This is the mana value of the character.
        '''

        return self.mana
    
    def set_mana(self, inputMana):
        '''
        Sets the character's mana value to inputMana.
        
        Parameters
        ----------
        self
        inputMana : int
            This is the new value for mana.
        
        Returns
        -------
        None
        '''
        self.mana = inputMana
    
    def set_weapon(self, inputWeapon):
        '''
        Equips a weapon to the character.
        
        Parameters
        ----------
        self

        inputWeapon : Weapon
            This is the new weapon that the character will be equipped with.
        
        Returns
        -------
        None
        '''
        self.weapon = inputWeapon
        
class Mage(Caster):
    '''
    This class implements combat mechanics exclusive to the Mage class.

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
    
    mana: int
    This is used in combat calculations, and is passed as an argument.

    Methods
    -------    
    attack():
    Calculates and returns the damage that the Warrior would deal in the combat simulation.
    
    defend():
    Calculates and returns the defense points that the Warrior would have in the combat simulation.
    '''
    
    def __init__(self, name, life, strength, defense, weapon, armor, mana):
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
        mana : int
            States the mana value of the character, later used for damage calculations in combat.
        
        Returns
        -------
        None    
        '''
        super().__init__(name, life, strength, defense, weapon, armor, mana)
        
    def attack(self):
        '''
        Returns the attack points of the character.
        At the start, there's a 50% chance for 2 mana to be generated. No mana is generated otherwise.
        Then if enough mana is available, the damage will be equal to strength + weapon power. One mana is spent
        Otherwise, damage will equal strength plus one.
        
        Parameters
        ----------
        self
        
        Returns
        -------
        int
            Returns the attack points of the character.
        '''
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
        '''
        Returns the defense points of the character.
        This is calculated using the current defense value;
        if the character currently has an Armor equipped, that will be added too.
        
        Parameters
        ----------
        self
        
        Returns
        -------
        int
            Returns the defense points of the character.
        '''
        if self.get_armor() != Armor:
            return self.get_defense() + self.get_armor().get_protection()
        else:
            return self.get_defense()
        
class Priest(Caster):
    '''
    This class implements combat mechanics exclusive to the Priest class.

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
    
    mana: int
    This is used in combat calculations, and is passed as an argument.

    Methods
    -------    
    attack():
    Calculates and returns the damage that the Warrior would deal in the combat simulation.
    
    defend():
    Calculates and returns the defense points that the Warrior would have in the combat simulation.
    
    heal():
    Calculates how much the Priest would heal, and adds that amount to the current life value.
    '''

    def __init__(self, name, life, strength, defense, weapon, armor, mana):
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
        super().__init__(name, life, strength, defense, weapon, armor, mana)
        
    def attack(self):
        '''
        Returns the attack points of the character.
        At the start, there's a 50% chance for 2 mana to be generated. No mana is generated otherwise.
        Then if enough mana is available, the damage will be equal to strength + weapon power. One mana is spent
        Otherwise, damage will equal strength plus one.
        
        Parameters
        ----------
        self
        
        Returns
        -------
        int
            Returns the attack points of the character.
        '''

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
        '''
        Returns the defense points of the character.
        This is calculated using the current defense value;
        if the character currently has an Armor equipped, that will be added too.
        
        Parameters
        ----------
        self
        
        Returns
        -------
        int
            Returns the defense points of the character.
        '''
        if self.get_armor() != Armor:
            return self.get_defense() + self.get_armor().get_protection()
        else:
            return self.get_defense()
        
    def heal(self):
        '''
        Calculates how much the Priest would heal, and adds that amount to the current life value.
        At the start, there's a 50% chance for 2 mana to be generated. No mana is generated otherwise.
        Then if enough mana is available, the heal will be equal to (strength + weapon power) divided by 2. 2 mana is spent.
        Otherwise, heal will equal zero.
        Finally, life value will be set to the current value plus the heal that we just calculated.
        
        Parameters
        ----------
        self
        
        Returns
        -------
        int
            Returns how much the character healed.
        '''

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
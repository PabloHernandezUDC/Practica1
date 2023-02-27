from item import *
import random as rd

class Avatar():
    def __init__(self):
        self.name = str
        self.life = int
        self.strength = int
        self.defense = int
        self.weapon = Weapon
        self.armor = Armor
        
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
        pass
        
    def defend(self):
        pass

class Melee(Avatar):
    def __init__(self, name, life, strength, defense, weapon, armor):
        super().__init__(name, life, strength, defense, weapon, armor)
        self.shield = None
    
    def get_shield(self):
        return self.shield
    
    def set_shield(self, inputShield):
        if isinstance(inputShield, Item.Covering.Shield):
            self.shield = inputShield
        else:
            print('a donde vas eso no es un escudo')
    
    def set_weapon(self, inputWeapon):
        if isinstance(inputWeapon, Item.Weapon.Sword):
            self.weapon = inputWeapon
        else:
            print('a donde vas eso no es una espada')

class Warrior(Melee):
    def __init__(self, name, life, strength, defense, weapon, armor, shield):
        super().__init__(name, life, strength, defense, weapon, armor, shield)
        self.fury = int
        
    def get_fury(self):
        return self.fury
    
    def set_fury(self, inputFury):
        self.fury = inputFury
        
    def attack(self):
        return self.strength + Weapon.get_power() + rd.randint(0, self.fury)

    def defend(self):
        print() # TODO

class Caster(Avatar):
    def __init__(self, name, life, strength, defense, weapon, armor):
        super().__init__(name, life, strength, defense, weapon, armor)
        self.mana = int
    
    def get_mana(self):
        return self.mana
    
    def set_mana(self, inputMana):
        self.mana = inputMana
    
    def set_weapon(self, inputWeapon):
        if isinstance(inputWeapon, Item.Weapon.Wand):
            self.weapon = inputWeapon
        else:
            print('a donde vas eso no es una varita')
        
class Mage(Caster):
    def __init__(self, name, life, strength, defense, weapon, armor, mana):
        super().__init__(name, life, strength, defense, weapon, armor, mana)
        
    def attack(self):
        # 50% de las veces añade 2 de mana
        # 50% de las veces no añade mana
        coinFlip = rd.randint(0, 1)
        if coinFlip == 0:
            self.mana += 2
                
        if self.mana > 0:   
            dmg = self.strength + self.get_weapon().get_power()
            self.mana -= 1
        else:
            dmg = self.strength + 1
    
        return dmg

    def defend(self):
        print() # TODO
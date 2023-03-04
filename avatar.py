from item import *
import random as rd

class Avatar():
    def __init__(self, name, life, strength, defense, weapon = None, armor = None):
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
    def __init__(self, name, life, strength, defense, weapon = None, armor = None, shield = None):
        super().__init__(name, life, strength, defense, weapon, armor)
        if shield != None:
            self.shield = shield
        else:
            self.shield = Shield
    
    def get_shield(self):
        return self.shield
    
    def set_shield(self, inputShield):
        self.shield = inputShield
    
    def set_weapon(self, inputWeapon):
        self.weapon = inputWeapon

class Warrior(Melee):
    def __init__(self, name, life, strength, defense, weapon = None, armor = None, shield = None, fury = None):
        super().__init__(name, life, strength, defense, weapon, armor, shield)
        if fury != None:
            self.fury = fury
        else:
            self.fury = int
        
    def get_fury(self):
        return self.fury
    
    def set_fury(self, inputFury):
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

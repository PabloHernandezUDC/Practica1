import sys
from avatar import *
import random as rd

def run(path):
    with open(path) as f:
        pjs = f.readlines()
        fighters = []
        for pj in pjs:
            fighters.append(parse_params(pj.split()))
        # aquí la lista fighters ya ha leído el archivo en cuestión y todos los objetos están creados
        while len(fighters) > 1:
            # selección de personajes
            roll1 = rd.randint(0, len(fighters) - 1)
            roll2 = rd.randint(0, len(fighters) - 1)
            while roll2 == roll1:
                roll2 = rd.randint(0, len(fighters) - 1)

            attacker = fighters[roll1]
            defender = fighters[roll2]
        
            # combate                        
            remainingDefenderLife = defender.get_life() + defender.defend() - attacker.attack()

            if remainingDefenderLife <= 0:
                fighters.pop(roll2)
                print('Quedan {} personas.'.format(len(fighters)))
            else:
                defender.set_life(remainingDefenderLife)
             
            # creación de items
            # coinflip entre sword (0) y wand (1) 
            coinFlip = rd.randint(0,1)
            if coinFlip == 0:
                newWeapon = Sword('Espada', rd.randint(1, 5))
            else:
                newWeapon = Wand('Varita', rd.randint(1, 5))
            
            # coinflip entre shield (0) y armor (1) 
            coinFlip = rd.randint(0,1)
            if coinFlip == 0:
                newCovering = Shield('Escudo', rd.randint(1, 5))
            else:
                newCovering = Armor('Armadura', rd.randint(1, 5))
            
            # ahora a equipárselos al atacante
            if isinstance(attacker, Warrior) and isinstance(newWeapon, Sword) and newWeapon.get_power() > attacker.get_weapon().get_power():
                attacker.set_weapon(newWeapon)
            elif isinstance(attacker, Mage) and isinstance(newWeapon, Wand) and newWeapon.get_power() > attacker.get_weapon().get_power():
                attacker.set_weapon(newWeapon)
                
            if isinstance(attacker, Warrior) and isinstance(newWeapon, Shield) and newCovering.get_protection() > attacker.get_shield().get_protection():
                attacker.set_shield(newCovering)
            elif isinstance(attacker, Mage) and isinstance(newWeapon, Armor) and newCovering.get_protection() > attacker.get_armor().get_protection():
                attacker.set_armor(newCovering)
                      
        print('El último superviviente es', fighters[0].get_name())

def parse_params(params):
    name, life, strength, defense = params[1], int(params[2]), int(params[3]), int(params[4])
    if params[0].lower() == "warrior":
        fury = int(params[5])
        currentFighter = Warrior(name, life, strength, defense, None, None, None, fury)
        
    elif params[0].lower() == "mage":
        mana = int(params[5])
        currentFighter = Mage(name, life, strength, defense, None, None, mana)
        
    elif params[0].lower() == "priest":
        mana = int(params[5])
        print ("Create Priest")
        #TODO: crear la clase Priest
        
    else:
        raise ValueError("Avatar '{}' is not valid".format(params[0]))
    
    return currentFighter

if __name__ == "__main__":
    run(sys.argv[1])
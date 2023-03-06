import sys
from avatar import *
import random as rd

# Al final de las 30 simulaciones, se pide indicar por pantalla, en orden descendente: (i) el número total 
# de veces que ha ganado cada PJ, (ii) el daño medio causado por cada PJ y su  desviación típica, (iii) el 
# número de veces que ha ganado cada clase y (iv) el daño medio por cada clase y su desviación típica.

def run(path):
    with open(path) as f:
        pjs = f.readlines()
        initial_fighters = []
        for pj in pjs:
            initial_fighters.append(parse_params(pj.split()))
        # aquí la lista fighters ya ha leído el archivo en cuestión y todos los objetos están creados
        # ahora se realiza la simulación hasta que solo quede un personaje
        fighters =  initial_fighters.copy()
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
            else:
                defender.set_life(remainingDefenderLife)
             
            # creación de items
            # decidimos entre sword (0) y wand (1) 
            coinFlip = rd.randint(0,1)
            if coinFlip == 0:
                newWeapon = Sword('Espada', rd.randint(1, 5))
            else:
                newWeapon = Wand('Varita', rd.randint(1, 5))
            
            # decidimos entre shield (0) y armor (1) 
            coinFlip = rd.randint(0,1)
            if coinFlip == 0:
                newCovering = Shield('Escudo', rd.randint(1, 5))
            else:
                newCovering = Armor('Armadura', rd.randint(1, 5))
                            
            # ahora se las equipamos al atacante
            if attacker.get_weapon() is Weapon or newWeapon.get_power() > attacker.get_weapon().get_power():
                if isinstance(attacker, Warrior) and isinstance(newWeapon, Sword):
                    attacker.set_weapon(newWeapon)
                elif isinstance(attacker, Mage) and isinstance(newWeapon, Wand):
                    attacker.set_weapon(newWeapon)
            else:
                pass
            
            if isinstance(newCovering, Armor):
                if attacker.get_armor() is Armor or newCovering.get_protection() > attacker.get_armor().get_protection():
                    attacker.set_armor(newCovering)
            elif isinstance(newCovering, Shield) and isinstance(attacker, Warrior):
                if attacker.get_shield() is Shield or newCovering.get_protection() > attacker.get_shield().get_protection():
                    attacker.set_shield(newCovering)
            else:
                pass
   
        winner = fighters[0]
        return initial_fighters, winner

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
    n_of_simulations = 30
    list_of_characters = run(sys.argv[1])[0]
    winners = {}
    
    for element in list_of_characters:
        winners[element.get_name()] = 0
    
    for i in range(n_of_simulations):
        winners[run(sys.argv[1])[1].get_name()] += 1
        
    descendingWinners = sorted(winners.items(), key=lambda x:x[1], reverse=True)
    for i in descendingWinners:
        if i[1] != 0:
            print('El personaje {one} ha ganado {two} veces.'.format(one = i[0], two = i[1]))
    print('El resto no han ganado nunca.')
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
        # ahora toca generar las parejas
        n_of_simulations = 30
        # selección de personajes
        for i in range(n_of_simulations):
            roll1 = rd.randint(0, len(fighters) - 1)
            roll2 = rd.randint(0, len(fighters) - 1)
            while roll2 == roll1:
                roll2 = rd.randint(0, len(fighters))
            attacker = fighters[roll1]
            defender = fighters[roll2]
            # combate
            # vida defensor final = vida defensor inicial - (attack - defend)
            #print(attacker.attack())
            
            print(defender.defend())

            # creación de items
    
    #TODO: Implement simulation here

def parse_params(params):
    name, life, strength, protection = params[1], int(params[2]), int(params[3]), int(params[4])
    if params[0].lower() == "warrior":
        fury = int(params[5])
        currentFighter = Warrior(name, life, strength, protection, None, None, None, fury)
        
    elif params[0].lower() == "mage":
        mana = int(params[5])
        currentFighter = Mage(name, life, strength, protection, None, None, mana)
        
    elif params[0].lower() == "priest":
        mana = int(params[5])
        print ("Create Priest")
        #TODO: crear la clase Priest
        
    else:
        raise ValueError("Avatar '{}' is not valid".format(params[0]))
    
    return currentFighter

if __name__ == "__main__":
    run(sys.argv[1])
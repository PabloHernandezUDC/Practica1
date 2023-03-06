import sys, statistics
from avatar import *
import random as rd

def run(path):
    with open(path) as f:
        pjs = f.readlines()
        initial_fighters = []
        for pj in pjs:
            initial_fighters.append(parse_params(pj.split()))
        # aquí la lista fighters ya ha leído el archivo en cuestión y todos los objetos están creados
        # ahora se realiza la simulación hasta que solo quede un personaje
        fighters =  initial_fighters.copy()
        playerNames = []
        for i in initial_fighters:
            playerNames.append(i.get_name())
        playerStats = {player: [] for player in playerNames}

        while len(fighters) > 1:
            # selección de personajes
            roll1 = rd.randint(0, len(fighters) - 1)
            roll2 = rd.randint(0, len(fighters) - 1)
            while roll2 == roll1:
                roll2 = rd.randint(0, len(fighters) - 1)
            attacker = fighters[roll1]
            defender = fighters[roll2]
        
            # combate
            daño = attacker.attack()
            defensa = defender.defend()
            remainingDefenderLife = defender.get_life() + defensa - daño
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
            
            playerStats[attacker.get_name()].append(daño)
            
        winner = fighters[0]
        return initial_fighters, winner, playerStats

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
    # creamos las variables
    n_of_simulations = 1000
    list_of_characters = run(sys.argv[1])[0]
    winners, finalPlayerStats = {}, {}
    usingPriest = False
    winsPerClass = {
        'Warrior': 0,
        'Mage': 0,
        'Priest': 0
    }    
    
    finalClassStats = {
        'Warrior': [],
        'Mage': [],
    }
    if usingPriest:
        finalClassStats['Priest'] = []

    # creamos un diccionario con los nombres de todos los personajes y su número de victorias (empieza en cero)
    for element in list_of_characters:
        winners[element.get_name()] = 0
        finalPlayerStats[element.get_name()] = []
    
    # realizamos las simulaciones correspondientes y modificamos el diccionario
    for i in range(n_of_simulations):
        winnerName, ps = run(sys.argv[1])[1].get_name(), run(sys.argv[1])[2]
        winners[winnerName] += 1
        if 'Warrior' in winnerName:
            winsPerClass['Warrior'] += 1
        elif 'Mage' in winnerName:
            winsPerClass['Mage'] += 1
        elif 'Priest' in winnerName:
            winsPerClass['Priest'] += 1
                
        for i in ps:
            finalPlayerStats[i] += ps[i]
            if 'Warrior' in i:
                finalClassStats['Warrior'] += ps[i]
            if 'Mage' in i:
                finalClassStats['Mage'] += ps[i]
            if 'Priest' in i  and usingPriest:
                finalClassStats['Priest'] += ps[i]

    for i in finalPlayerStats:
        dañoMedio = statistics.mean(finalPlayerStats[i])
        desviacion = statistics.stdev(finalPlayerStats[i], dañoMedio)
        finalPlayerStats[i] = [dañoMedio, desviacion]
        
    for i in finalClassStats:
        print(i)
        dañoMedio = statistics.mean(finalClassStats[i])
        desviacion = statistics.stdev(finalClassStats[i], dañoMedio)
        finalClassStats[i] = [dañoMedio, desviacion]

    # ordenamos los diccionarios en orden descendente y los imprimimos
    sortedWinners = sorted(winners.items(), key=lambda x:x[1], reverse=True)
    for i in sortedWinners:
        if i[1] != 0:
            print('El personaje {one} ha ganado {two} veces.'.format(one = i[0], two = i[1]))
    print('El resto no han ganado nunca.\n')
    
    for i in finalPlayerStats:
            print('El personaje {one} ha tenido una media de año de {two}  y una desviación típica de {three}.'.format(one = i, two = finalPlayerStats[i][0], three = finalPlayerStats[i][1]))
    print()
    
    sortedWinsPerClass = sorted(winsPerClass.items(), key=lambda x:x[1], reverse=True)
    for i in sortedWinsPerClass:
        if i[1] != 0:
            print('La clase {one} ha ganado {two} veces.'.format(one = i[0], two = i[1]))
    print()

    for i in finalClassStats:
            print('La clase {one} ha tenido una media de año de {two}  y una desviación típica de {three}.'.format(one = i, two = finalClassStats[i][0], three = finalClassStats[i][1]))
    print()
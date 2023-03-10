# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
import random as rd
import statistics
import sys

from avatar import *

def run(path):
    '''
    This function runs one iteration of the combat simulation based on a given text file with a certain format.
    If the file meets the format criteria, it will be read correctly and characters will be created from the parse_params function.

    Parameters 
    ---------- 
    path: str 
        File path for the file that will be used. 
 
    Returns 
    ------- 
    list
        List with all fighter objects that may be used in some other calculations. (initial_fighters)
    Avatar
        The object (winner) for the character who won the current iteration of the simulation.
    dict
        Dictionary where the keys are the names of all characters involved in the simulation,
        and the values are lists where each element represents how much damage they dealt in a given combat. (playerStats)
    dict
        Dictionary where the keys are the names of all characters involved in the simulation,
        and the values are lists where each element represents how much they healed in a given combat. (healStats)
    '''
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
        healStats = {player: [] for player in playerNames}

        while len(fighters) > 1:
            # selección de personajes
            roll1 = rd.randint(0, len(fighters) - 1)
            roll2 = rd.randint(0, len(fighters) - 1)
            while roll2 == roll1:
                roll2 = rd.randint(0, len(fighters) - 1)
            attacker = fighters[roll1]
            defender = fighters[roll2]
        
            # combate
            roll = rd.randint(1, 4)
            if isinstance(attacker, Priest) and roll == 4:
                healing = attacker.heal()
                healStats[attacker.get_name()].append(healing)
                daño = 0
            else:
                daño = attacker.attack()
                defensa = defender.defend()
                remainingDefenderLife = defender.get_life() + defensa - daño
                if remainingDefenderLife <= 0:
                    fighters.pop(roll2)
                else:
                    defender.set_life(remainingDefenderLife)
             
            # 50% de generar un item y 50% de que sea de cada uno de los tipos
            itemRoll = rd.randint(0,3)
            if itemRoll == 2:
                newWeapon = Sword('Espada', rd.randint(1, 5))
            elif itemRoll == 3:
                newWeapon = Wand('Varita', rd.randint(1, 5))
            else:
                newWeapon = None
            
            # 50% de generar un item y 50% de que sea de cada uno de los tipos
            itemRoll = rd.randint(0,3)
            if itemRoll == 2:
                newCovering = Shield('Escudo', rd.randint(1, 5))
            elif itemRoll == 3:
                newCovering = Armor('Armadura', rd.randint(1, 5))
            else:
                newCovering = None

            if newWeapon is not None:
                if attacker.get_weapon() is Weapon or newWeapon.get_power() > attacker.get_weapon().get_power():
                    if isinstance(attacker, Warrior) and isinstance(newWeapon, Sword):
                        attacker.set_weapon(newWeapon)
                    elif isinstance(attacker, Caster) and isinstance(newWeapon, Wand):
                        attacker.set_weapon(newWeapon)
            
            if newCovering is not None:
                if isinstance(newCovering, Armor):
                    if attacker.get_armor() is Armor or newCovering.get_protection() > attacker.get_armor().get_protection():
                        attacker.set_armor(newCovering)
                elif isinstance(newCovering, Shield) and isinstance(attacker, Warrior):
                    if attacker.get_shield() is Shield or newCovering.get_protection() > attacker.get_shield().get_protection():
                        attacker.set_shield(newCovering)
            
            if daño > 0:
                playerStats[attacker.get_name()].append(daño)
            
        winner = fighters[0]
        return initial_fighters, winner, playerStats, healStats

def parse_params(params):
    '''
    This function reads a text line with a certain format and creates and Avatar object accordingly.
 
    Parameters 
    ---------- 
    params: list
        List of strings that will be interpreted for Avatar object creation.
 
    Returns 
    ------- 
    Avatar
        Returns an Avatar object (currentFighter) where the elements from params are used as attributes.
    '''
    name, life, strength, defense = params[1], int(params[2]), int(params[3]), int(params[4])
    if params[0].lower() == "warrior":
        fury = int(params[5])
        currentFighter = Warrior(name, life, strength, defense, None, None, None, fury)
        
    elif params[0].lower() == "mage":
        mana = int(params[5])
        currentFighter = Mage(name, life, strength, defense, None, None, mana)
        
    elif params[0].lower() == "priest":
        mana = int(params[5])
        currentFighter = Priest(name, life, strength, defense, None, None, mana)
        
    else:
        raise ValueError("Avatar '{}' is not valid".format(params[0]))
    
    return currentFighter

if __name__ == "__main__":
    # creamos las variables
    n_of_simulations = 30
    list_of_characters = run(sys.argv[1])[0]
    winners, finalPlayerStats, finalHealStats = {}, {}, {}
    winsPerClass = {
        'Warrior': 0,
        'Mage': 0,
        'Priest': 0
    }    
    
    finalClassStats = {
        'Warrior': [],
        'Mage': [],
    }
    
    for i in list_of_characters:
        if "Priest" in i.get_name():
            usingPriest = True
            finalClassStats['Priest'] = []
            break
        else:
            usingPriest = False

    finalClassHealStats = {
        'Warrior': [],
        'Mage': [],
        'Priest': []
    }

    # creamos un diccionario con los nombres de todos los personajes y su número de victorias (empieza en cero)
    for i in list_of_characters:
        winners[i.get_name()] = 0
        finalPlayerStats[i.get_name()] = []
        finalHealStats[i.get_name()] = []
    
    # realizamos las simulaciones correspondientes y modificamos el diccionario
    for i in range(n_of_simulations):
        winnerName, ps, hs = run(sys.argv[1])[1:]
        winnerName = winnerName.get_name()
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
                
        for i in hs:
            finalHealStats[i] += hs[i]
            if 'Warrior' in i:
                finalClassHealStats['Warrior'] += hs[i]
            if 'Mage' in i:
                finalClassHealStats['Mage'] += hs[i]
            if 'Priest' in i  and usingPriest:
                finalClassHealStats['Priest'] += hs[i]

    for i in finalPlayerStats:
        dañoMedio = statistics.mean(finalPlayerStats[i])
        desviacion = statistics.stdev(finalPlayerStats[i], dañoMedio)
        finalPlayerStats[i] = [dañoMedio, desviacion]
        
    for i in finalClassStats:
        dañoMedio = statistics.mean(finalClassStats[i])
        desviacion = statistics.stdev(finalClassStats[i], dañoMedio)
        finalClassStats[i] = [dañoMedio, desviacion]

    for i in finalHealStats:
        if len(finalHealStats[i]) > 0:
            healMedio = statistics.mean(finalHealStats[i])
            desviacion = statistics.stdev(finalHealStats[i], healMedio)
            finalHealStats[i] = [healMedio, desviacion]
        
    for i in finalClassHealStats:
        if len(finalClassHealStats[i]) > 0:
            healMedio = statistics.mean(finalClassHealStats[i])
            desviacion = statistics.stdev(finalClassHealStats[i], healMedio)
            finalClassHealStats[i] = [healMedio, desviacion]

    # se imprimen los datos obtenidos en un formato de "tablas"
    print('\nNº de victorias por personaje:')
    print('--------------------------------------------')
    sortedWinners = sorted(winners.items(), key=lambda x:x[1], reverse=True)
    for i in sortedWinners:
        if i[1] != 0:
            print('Nombre: {one}   \t| nº de victorias: {two}'.format(one = i[0], two = i[1]))
    print('El resto no han ganado nunca.')
    
    print('\nEstadísticas de daño por personaje:')
    print('--------------------------------------------------------------------------')
    for i in finalPlayerStats:
            print('Nombre: {one}   \t| Daño medio: {two}   \t| Desviación típica: {three}'.format(one = i, two = round(finalPlayerStats[i][0], 2), three = round(finalPlayerStats[i][1], 2)))
    
    print('\nNº de victorias por clase:')
    print('--------------------------------------')
    sortedWinsPerClass = sorted(winsPerClass.items(), key=lambda x:x[1], reverse=True)
    for i in sortedWinsPerClass:
        if i[1] != 0:
            print('Clase: {one}\t| nº de victorias: {two}'.format(one = i[0], two = i[1]))

    print('\nEstadísticas de daño por clase:')
    print('-----------------------------------------------------------------')
    for i in finalClassStats:
            print('Clase: {one}\t| Daño medio: {two}\t| Desviación típica: {three}'.format(one = i, two = round(finalClassStats[i][0], 2), three = round(finalClassStats[i][1], 2)))
    
    
    if usingPriest:
        print('\nEstadísticas de curación por personaje:')
        print('-------------------------------------------------------------------------')
        for i in finalHealStats:
            if len(finalHealStats[i]) > 0:
                print('Nombre: {one}   \t| Curación media: {two}\t| Desviación típica: {three}'.format(one = i, two = round(finalHealStats[i][0], 2), three = round(finalHealStats[i][1], 2)))

        print('\nEstadísticas de curación por clase:')
        print('-----------------------------------------------------------------')
        for i in finalClassHealStats:
            if len(finalClassHealStats[i]) > 0:
                print('Clase: {one}\t| Curación media: {two}\t| Desviación típica: {three}'.format(one = i, two = round(finalClassHealStats[i][0], 2), three = round(finalClassHealStats[i][1], 2)))
    print()
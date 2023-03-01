import sys
from avatar import *
import random as rd

def run(path):
    with open(path) as f:
        pjs = f.readlines()
        for pj in pjs:
            parse_params(pj.split())
    #TODO: Implement simulation here

def parse_params(params):
    name, life, strength, protection = params[1], int(params[2]), int(params[3]), int(params[4])
    if params[0].lower() == "warrior":
        fury = int(params[5])
        #print ("Create Warrior  [todo]")        
        currentWarrior = Avatar(name, life, strength, protection)
        print(currentWarrior.get_life())
        
        currentWarrior = Melee(currentWarrior.get_name()) # TODO: poner aqui todos los atributos para intentar pasarlo a warrior
        

        
    elif params[0].lower() == "mage":
        mana = int(params[5])
        print ("Create Mage [todo]")
    elif params[0].lower() == "priest":
        mana = int(params[5])
        print ("Create Priest [todo]")
    else:
        raise ValueError("Avatar '{}' is not valid".format(params[0]))

if __name__ == "__main__":
    run(sys.argv[1])
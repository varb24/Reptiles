import Reptile
import Slimes
import Tiles
import random
from datetime import datetime
import pdb


Reptiles_On = True
gametimer = 0
unit_actions = [1, 1, 1, 1, 1, 1]  # filled with attacks for now
endgame_number = 100000000000000
list_of_tiles = []  #contains all tile objects
list_of_reptiles = [] #contains reptiles
tile_index = 0  #This should be global?
start_tile = False #Tracks if tile has been generated

#creates test reptile
rep1 = Reptile.Reptile(1, 1, 1)

def unit_attack(reptile, unit2): #consider making unit 1 and unit 2 locations in an array, unit 1 is reptile unit 2 is animal
    # causes units from a tile to fight
    print(reptile.name + " " + str(reptile.health) + " Is fighting:" + unit2.name)
    if unit_actions[0] == 1:
        #list_of_tiles[tile..] should refer to a reptile object, mb create a seperate list and add my reptiles objects to the list???!!!

        unit2.health -= reptile.attack
        reptile.health -= unit2.attack
        if unit2.health <= 0:
            reptile.exp += 1
            list_of_tiles[tile_index].add_item(unit2.drops)
            return "Victory!"
        if reptile.health <= 0:
            print("Egg created " + "Enemy health is " + str(unit2.health) )

            return "Battle ended"
        return "Battle continues"

def time_tracker():
    #this function returns the current time in seconds
    dt = datetime.now()
    current_second = datetime.timestamp(dt)
    return current_second



#This is the core game loop
while Reptiles_On == True:
    gametimer += 1

    # use seconds to calculate turns
    if gametimer == endgame_number:
        # below closes the game
        Reptiles_On == False
        break

    if not start_tile:
        #adds the first tile to list of tiles array, This creates a tile
        rep1 = Reptile.Reptile(1, 1, 1)
        rep1.name = "Prototile"
        list_of_tiles.append(Tiles.Tiles(rep1))
        start_tile = True

    #list_of_tiles[0].spawn_reptile()

    for tile in list_of_tiles:  #Iterates through all tiles and checks if a reptile needs to be spawned from an egg
        if not tile.reptilestate:
            tile.spawn_reptile()

    slime1 = Slimes.Slime()
    slime1.add_drop('stone')


    # chooses each creature's action

    # Calls reptile mind to decide what action a reptile takes (zero is currently being used for reptile 1, unit 1)

    unit_actions.append(rep1.mind)

    # perform unit_action(1 is attack)
    # battle of rep1 and slime
    if list_of_tiles[0].reptile.health>0:
        print("Battle Start")
        print(unit_attack(rep1, list_of_tiles[0].animals_in_tile[random.randrange(1000)])) #TODO make this into generic unit attacks
    else:
        list_of_tiles[0].spawn_reptile()
    #print(list_of_tiles[0].reptile.health>0)

#Tiles are the basic building blocks of the game, they contains biomes, where creature stocks are kept. Units, reptiles are kept in tiles.
from datetime import datetime, timedelta
import random
import time
import Slimes


class Tiles:
    def __init__(self,  reptile , reptilestate= False):
        self.reptilestate = reptilestate
        self.reptile = reptile;
        self.tile_inventory = [] #Stores all items.
        self.animals_in_tile = []
        self.slime_count = 0
        self.red_slime_count = 0
        self.time_since_last_spawn = 0;

        number_of_slimes = 1000
        #spawn all starting animals in init.
        red_slimes_spawn = random.randrange(number_of_slimes)
        #adds slimes
        for i in range(number_of_slimes - red_slimes_spawn ):
            slimei = Slimes.Slime()
            self.animals_in_tile.append(slimei)
            self.slime_count+=1
            print("Slimes i: ",self.animals_in_tile[i].name)

        #adds red_slimes
        print(self.slime_count)
        for i in range(red_slimes_spawn):
            slimei = Slimes.Red_Slime()
            self.animals_in_tile.append(slimei)
            self.red_slime_count+=1
            print("Red i: ", self.animals_in_tile[i+self.slime_count].name)

        print(self.red_slime_count)

    def time_tracker(self):
        dt = datetime.now()
        current_second = datetime.timestamp(dt)
        return current_second

    def spawn_reptile(self):
        #Changes reptile status to true
        rep_incubation = 1  # How long it takes for a reptile to spawn
        self.time_since_last_spawn += self.time_tracker()  # tracks current seconds when func is called
        print(self.time_since_last_spawn)
        if (self.time_since_last_spawn >= rep_incubation):
            print("Reptile has spawned")
            self.reptilestate = True
            self.time_since_last_spawn = 0
            self.reptile.revive()
            print(self.reptile.health)

    def add_item(self, item):
        self.tile_inventory.append(item)
        print("added : ", item)

    def print_inv(self):
        print(self.tile_inventory)


print(timedelta(seconds= 15, minutes = 1, milliseconds= 198098))
dt = datetime.now()
print(int(dt.strftime('%S'))) # This will print out the current seconds!!
print(datetime.timestamp(dt) )

#tile1 = Tiles() Testing tiles generation

print(time.time())


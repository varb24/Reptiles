
# use this to store reptile's individual stats


class Reptile:
    max_health = 10
    def __init__(self, claw = 1, body =1, mind=1, exp=0, health = max_health, name ="", tile = 0):
        self.claw = claw
        self.body = body
        self.mind = mind
        self.exp = exp
        self.action = 0
        self.health = health
        self.name = name
        self.tile = tile
        self.attack = claw

    def rep_mind(self):
        #selects reptile action
        if (self.mind <= 1):
            #uses action 1 which is attack
            self.action = 1
            return self.action

    def revive(self):
        self.health = Reptile.max_health
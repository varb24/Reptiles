#mob's stats

class Creatures:
    def __init__(self,health =1, attack =1, exp = 0, drops='', name = ""):
        self.health = health
        self.attack = attack
        self.exp = exp
        self.drops = drops
        self.name = name

    def add_drop(self, added_drop):
        self.drops = self.drops + " and " + added_drop
        return self.drops
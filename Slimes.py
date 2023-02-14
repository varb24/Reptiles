import Creatures

class Slime(Creatures.Creatures):
    def __init__(self,health = 0, attack = 0, exp = 0, drops= 'goop', name = "Regular Slime"):
        super().__init__(health = 4, attack = 1, exp= 2, drops ='goop',name = "Regular Slime" )

class Red_Slime(Creatures.Creatures):
    def __init__(self,health = 0, attack = 0, exp = 0, drops= 'goop', name = "Red Slime"):
        super().__init__(health = 20, attack = 4, exp= 10, drops ='red goop', name = "Red Slime")


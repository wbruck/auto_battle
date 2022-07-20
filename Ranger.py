from Unit import Unit

class Ranger(Unit):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)
        self.attack_range = 3
        self.vision = 5
        self.movement = 2
        self.symbol = 'R'

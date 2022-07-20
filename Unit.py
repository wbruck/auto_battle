from helpers import distance
class Unit(object): # mixin here

    def __init__(self, name:str, hp:int, damage:int):
        self.name = name
        self.hp = hp
        self.damage = damage  
        self.x = 0
        self.y = 0
        self.symbol = 'B'
        self.vision = 3
        self.attack_range = 1
        self.movement_impulse = [1,3,3,1] # u,d,l,r each number corresponds to a direction
        self.current_target = None # TODO make this chosen by logic in the unit

        # ---not used yet
        self.faction = 'Red'
        self.movement = 1

    def __str__(self):
        return f"{self.name} HP: {self.hp} Damage: {self.damage}, [{self.x},{self.y}] "
        
    def is_alive(self):
        return self.hp > 0
        
    def take_damage(self, damage_points:int):
        self.hp -= damage_points
        if self.hp < 0:
            self.hp = 0
            self.symbol = self.symbol.lower()
            print(f"{self.name} died")
        # TODO: what to do once it dies
        return self.hp

    def attack(self, target):
        self.current_target = target
        target.take_damage(self.damage)
        return target.hp

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def choose_target(self, targets:list):
        if len(targets) == 0:
            return None

        #check distance
        # check alive
        # check range
        # TODO: create threat/agro level distance+hp+damage
        new_targets = []
        for target in targets:
            if target.is_alive():
                target_dict = {'distance': distance(self.x, self.y, target.x, target.y),
                                'target': target,
                                'hp': target.hp}
                new_targets.append(target_dict)

        sorted_targets = sorted(new_targets, key=lambda target: (target['hp'], target['distance']))
        # print(sorted_targets)
        for target_dict in sorted_targets:
            if target_dict.get('distance') <= self.attack_range:
                return target_dict.get('target')
            elif target_dict.get('distance') <= self.vision:
                return target_dict.get('target')

        return None

        # if closest and lowest HP choose
        # if hittable and lowest HP choose
  
      
    def choose_movement(self, movement_choices:list)-> tuple:
        """take list of possible moves and return 'best' move"""
        pass



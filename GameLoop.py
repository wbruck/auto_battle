
from Board import Board
from Unit import Unit


class GameLoop(object):
    def __init__(self, board, units):
        self.board = board
        self.units = units
        self.rounds = 0
        self.eliminated = []
        self.eliminated_units = []
        self.eliminated_units_names = []
        self.eliminated_units_hp = []
        self.eliminated_units_damage = []
        self.eliminated_units_rounds = []
        self.eliminated_units_dead_rounds = []
        self.eliminated_units_dead_rounds_total = []
        self.eliminated_units_dead_rounds_average = []
        self.eliminated_units_dead_rounds_average_round = []
        self.eliminated_units_dead_rounds_average_round_total = []
        self.eliminated_units_dead_rounds_average_round_average = []
        self.eliminated_units_dead_rounds_average_round_average_round = []
        self.eliminated_units_dead_rounds_average_round_average_round_total = []
        self.eliminated_units_dead_rounds_average_round_average_round_average = []
        self.eliminated_units_dead_rounds_average_round_average_round_average_round = []
        self.eliminated_units_dead_rounds_average_round_average_round_average_round_total = []
        self.eliminated_units_dead_rounds_average_round_average_round_average_round_average = []
        self.eliminated_units_dead_rounds_average_round_average_round_average_round_average_round = []
        self.eliminated_units_dead_rounds_average_round_average_round_average_round_average_round_total = []
        self.eliminated_units_dead_rounds_average_round_average_round_average_round_average_round_average = []


    def run(self, steps=2):
        for nn in range(steps):
            self.rounds += 1
            print("\n")
            print(f"Round {self.rounds}")
            self.board.print_board()
            if len(self.units) == 1:
                print(f"\n{self.units[0].name} wins!")
                break
            self.units = self.board.sort_units(self.units)
            for unit in self.units:
                
                if not unit.is_alive():
                    print(f"{unit.name} is dead")
                else:
                    print(f"Turn:----------- {unit.name}: {unit.symbol}")
                    print(f"{unit}")
                    targets = self.board.get_units_in_target_range(unit.x, unit.y, unit.vision)
                    
                    if unit in targets:
                        targets.remove(unit)
                    print(f"Targets: {len(targets)}")

                    target = unit.choose_target(targets)
                    
                    if not target:
                        # if no targets explore  board
                        unit_choice = self.board.move_unit_randomly(unit)
                        print(f"{unit.name} moves aimlessly {unit_choice} to [{unit.x}, {unit.y}]")
                        continue

                    distance_to_target = self.board.distance(unit.x, unit.y, target.x, target.y)
                    print(f"{target} is {distance_to_target} away")
                    if distance_to_target <= unit.attack_range:   
                        # if close enough attack
                        print(f"{unit.name} attacks {target.symbol} for {unit.damage} damage")
                        target_hp = unit.attack(target)
                        if target_hp <= 0:
                            self.eliminated_units.append(target)
                            self.units.remove(target)
                    else:
                        # if no units in range, move towards nearest unit
                        self.board.move_toward_target(unit, target)
                        print(f"{unit.name} moves towards {target.symbol} to [{unit.x}, {unit.y}]")
                        


                    
   
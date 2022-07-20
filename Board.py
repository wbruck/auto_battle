
from Unit import Unit
from random import choice
from helpers import distance

class Board(object):
    def __init__(self, size=10):
        self.size = size
        self.board = [[0 for x in range(size)] for y in range(size)]
        self.units = []
        self.rounds = 0
        self.taken_symbols = []

    def add_unit(self, unit):
        self.units.append(unit)
        self.board[unit.y][unit.x] = unit

    def add_unit_random_location(self,unit):
        x = choice(range(self.size))
        y = choice(range(self.size))
        while self.board[y][x] != 0:
            x = choice(range(self.size))
            y = choice(range(self.size))
        self.add_unit(unit)
        self.move_unit(unit, x, y)
        
    
    def remove_unit(self, unit):
        self.units.remove(unit)
        self.board[unit.y][unit.x] = 0

    def get_unit(self, x, y):
        return self.board[y][x]

    def get_units(self):
        return self.units

    def __str__(self):
        row_padding = " "
        board_str = " "+ " ".join([f" {x%10}" for x in range(self.size)]) + "\n"
        for row_num, row in enumerate(self.board):
            board_str += f"{row_num%10}"
            for unit in row:
                if unit == 0:
                    board_str += " . "
                else:
                    board_str += f" {unit.symbol} "
            board_str += "\n"
        return board_str

    def print_board(self):
        print(self)

    def get_units_in_target_range(self, x, y, target_range):
        units_in_range = []
        for i in range(x - target_range, x + target_range + 1):
            for j in range(y - target_range, y + target_range + 1):
                if i >= 0 and i < self.size and j >= 0 and j < self.size:
                    if self.board[j][i] != 0:
                        units_in_range.append(self.board[j][i])
        return units_in_range

    def sort_units(self, units):
        return sorted(units, key=lambda unit: unit.hp)

    def move_unit(self, unit, x, y):
        self.board[unit.y][unit.x] = 0
        unit.x = x
        unit.y = y
        self.board[y][x] = unit

    def distance(self, x, y, x2, y2):
        return distance(x, y, x2, y2)

    def check_movement(self, unit, x, y):
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return False
        if self.board[y][x] != 0:
            return False
        return True

    def move_toward_target(self, unit, target):
        # TODO: make this loopable if the unit has higher range of movement
        legal_move = False
        jitter = 0

        final_x, final_y = unit.x, unit.y
        # direct path to target x-first
        if unit.x < target.x:
            final_x += 1
        elif unit.x > target.x:
            final_x -= 1
        elif unit.y < target.y:
            final_y += 1
        elif unit.y > target.y:
            final_y -= 1

        # direct path to target y-first
        if self.check_movement(unit, final_x, final_y):
            legal_move = True
        else:
            print("x-path check failed")
            final_x, final_y = unit.x, unit.y
            if unit.y < target.y:
                final_y += 1
            elif unit.y > target.y:
                final_y -= 1
            elif unit.x > target.x:
                final_x -= 1
            elif unit.x < target.x:
                final_x += 1

        try_x, try_y = False, False
        while(not legal_move):
            jitter += 1
            if jitter > 10:
                print(f"move toward target failed for {unit.name}")
                break

            if self.check_movement(unit, final_x, final_y):
                legal_move = True
            else:
                print("y-path check failed")
                final_x, final_y = unit.x, unit.y
                # get random number to go random right or left
                choices = [1, -1]
                movement_choice = choice(choices)
                if not try_x:
                    final_x += movement_choice
                    try_x = True
                    try_y = False
                if try_x and not try_y:
                    final_y += movement_choice
                    try_y = True
                    try_x = False

                    final_y += movement_choice
                print("tried random x first, y second")

            legal_move = self.check_movement(unit, final_x, final_y)
            if not legal_move:
                final_x, final_y = unit.x, unit.y
                print("Unit can not move")
                if movement_choice > 0:
                    choices.append(-1)
                else:
                    choices.append(1)

            print(f"{legal_move=}")

        self.move_unit(unit, final_x, final_y)

    def move_unit_randomly(self, unit):
       # TODO: make this loopable if the unit has higher range of movement
       # TODO: make choice_list come from unit to provide preference for direction with % chance
        choices = ["up", "down", "left", "right"]

        choice_list = []
        for n, direction_preference in enumerate(unit.movement_impulse):
            for i in range(direction_preference):
                if n == 0 and unit.y != 0:
                    choice_list.append("up")
                elif n == 1 and unit.y != self.size - 1:
                    choice_list.append("down")
                elif n == 2 and unit.x != 0:
                    choice_list.append("left")
                elif n == 3 and unit.x != self.size - 1:
                    choice_list.append("right")

        legal_move = False
        q = 0
        while(not legal_move):
            final_x, final_y = unit.x, unit.y
            # break forever loop
            if q > 10:
                print(f"move randomly failed for {unit.name}")
                break
            unit_choice = choice(choice_list)
            if unit_choice == "up":
                final_y -= 1
            elif unit_choice == "down":
                final_y += 1
            elif unit_choice == "left":
                final_x -= 1
            elif unit_choice == "right":
                final_x += 1
            legal_move = self.check_movement(unit, final_x, final_y)

        self.move_unit(unit, final_x, final_y)

        return unit_choice
#%%
from GameLoop import GameLoop
from Board import Board
from Unit import Unit
from Ranger import Ranger

board_size = 20
num_units = 40

board = Board(20)

for nn in range(num_units):
    if nn % 3 == 0:
        board.add_unit_random_location(Ranger("Ranger" + str(nn), 4, 3))
    else:
        board.add_unit_random_location(Unit("Unit" + str(nn), 5, 2))

game = GameLoop(board, board.units)

print(game.board)
#%%
print(game.units)
#%%
#TODO : log handler to print to file and to set levels for console output
# TODO: add alies to units
# TODO: add factions?
# TODO: add more randomness to the movements and target finding

game.run(steps=10)
# %%
game.run(steps=10)
# %%

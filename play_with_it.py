from solve_grid import solve_grid
from parse_to_list import print_nicely
from testing_data import less_clues, complete_grid
from grid_status import illegal

starting_grid = [
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [1]
]

solved_grid = solve_grid(less_clues)
print_nicely(solved_grid['grid'])
print('-------------')
print_nicely(complete_grid)
print('illegal:')
print(illegal(solved_grid['grid']))

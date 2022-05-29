from solve_grid import solve_grid
from parse_to_list import print_nicely, add_commas_between

starting_grid = [
    ['000102000'],
    ['060000070'],
    ['008000900'],
    ['400000003'],
    ['050007000'],
    ['200080001'],
    ['009000805'],
    ['070000060'],
    ['000304000']
]
starting_grid = add_commas_between(starting_grid)

solved_grid = solve_grid(starting_grid)

print(solved_grid['status'])
print_nicely(solved_grid['grid'])

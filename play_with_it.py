from solve_grid import solve_grid
from parse_to_list import print_nicely, add_commas_between

__starting_grid = [
    ['100000000'],
    ['000000000'],
    ['000000000'],
    ['000304000'],
    ['000000000'],
    ['000000000'],
    ['070000000'],
    ['000000000'],
    ['004060009']
]
starting_grid = add_commas_between(__starting_grid)

solved_grid = solve_grid(starting_grid)

print(solved_grid['status'])
print_nicely(solved_grid['grid'])

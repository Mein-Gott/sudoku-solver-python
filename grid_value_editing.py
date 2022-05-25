from copy import deepcopy

def add_value(grid, coords, value):
    edited_grid = deepcopy(grid)
    edited_grid[coords['row']][coords['column']] = value
    return edited_grid

def delete_value(grid, coords):
    edited_grid = deepcopy(grid)
    edited_grid[coords['row']][coords['column']] = 0
    return edited_grid
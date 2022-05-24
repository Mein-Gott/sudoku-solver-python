from copy import deepcopy
from candidates_per_cell import candidates_per_cell
from coordinates_of_singles import coordinates_of_singles

def add_singles(grid):
    editable_grid = deepcopy(grid)

    candidates = candidates_per_cell(editable_grid)
    coordinates = coordinates_of_singles(candidates)

    while len(coordinates) > 0:
        for single_data in coordinates:
            editable_grid[single_data['row']][single_data['column']] = single_data['value']

        candidates = candidates_per_cell(editable_grid)
        coordinates = coordinates_of_singles(candidates)

    return editable_grid

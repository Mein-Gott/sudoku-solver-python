from copy import deepcopy 
from add_singles import add_singles
from candidates_per_cell import get_cell_with_least_candidates
from grid_status import *
from grid_value_editing import *
 
def solve_grid(grid):
    if illegal(grid): return {'status': 'illegal'}

    editable_grid = deepcopy(grid)
    editable_grid = add_singles(grid)

    if is_complete(editable_grid): 
        return {'status': 'complete', 'grid': editable_grid}
    if in_impossible_state(editable_grid): 
        return {'status': 'impossible'}


    # GUESSING STARTS

    least_candidate_cell = get_cell_with_least_candidates(editable_grid)

    for candidate in least_candidate_cell['candidates']:
        editable_grid = add_value(editable_grid, least_candidate_cell['coordinates'], candidate)
        
        solved_grid = solve_grid(editable_grid)
        if solved_grid['status'] == 'complete': 
            return {'status': 'complete', 'grid': solved_grid}

        editable_grid = delete_value(editable_grid, least_candidate_cell['coordinates'])

    return {'status': 'impossible'}

from copy import deepcopy 
from add_singles import add_singles
from grid_status import *
 
def solve_grid(grid):
    # if illegal(grid): return {'status': 'illegal'}

    editable_grid = deepcopy(grid)
    editable_grid = add_singles(grid)

    if is_complete(editable_grid): 
        return {'status': 'complete', 'grid': editable_grid}
    if in_impossible_state(editable_grid): 
        return {'status': 'impossible'}

"""
    # GUESSING STARTS

    least_candidate_cell = get_least_candidate_cell()
    candidates = get_candidates(least_candidate_cell)

    for candidate in candidates:
        add candidate to editable_grid
        
        solved_grid = solve_grid(editable_grid)
        if solved_grid['status'] = 'complete': return ['status': 'complete', 'grid': solved_grid]

        delete candidate from editable_grid

    return ['status': 'impossible'] 
"""

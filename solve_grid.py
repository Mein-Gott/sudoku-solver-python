from copy import deepcopy 
from add_singles import add_singles
from candidates_per_cell import get_cell_with_least_candidates
from grid_status import *
from grid_value_editing import *
 
def solve_grid(grid):
    editable_grid = deepcopy(grid)

    if illegal(editable_grid): return {'status': 'not solvable'}

    editable_grid = add_singles(grid)

    if illegal(editable_grid): return {'status': 'not solvable'}

    if is_complete(editable_grid): 
        return {'status': 'complete', 'grid': editable_grid}
    if in_impossible_state(editable_grid): 
        return {'status': 'not solvable'}


    # GUESSING STARTS

    least_candidate_cell = get_cell_with_least_candidates(editable_grid)

    for candidate in least_candidate_cell['candidates']:
        editable_grid = add_value(editable_grid, least_candidate_cell['coordinates'], candidate)
        
        solved_grid = solve_grid(editable_grid)
        if solved_grid['status'] == 'complete':
            return solved_grid

        editable_grid = delete_value(editable_grid, least_candidate_cell['coordinates'])

    return {'status': 'not solvable'}

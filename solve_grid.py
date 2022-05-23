def solve_grid(grid):
    editable_grid = grid.copy()

"""
    count num_of_singles
    while num_of_singles > 0:
        add singles to the editable_grid
        count num_of_singles

    if grid_complete(editable_grid): return ['status': 'complete', 'grid': editable_grid]
    if grid_impossible(editable_grid): return ['status': 'impossible']


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
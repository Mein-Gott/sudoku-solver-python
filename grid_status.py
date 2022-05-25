from candidates_per_cell import candidates_per_cell

def is_complete(grid):
    for row in grid:
        for cell in row:
            if cell == 0: return False

    return True

def in_impossible_state(grid):
    candidates = candidates_per_cell(grid)

    for candidate_row, row in zip(candidates, grid):
        for cell_candidates, cell in zip(candidate_row, row):
            if cell == 0 and len(cell_candidates) == 0:
                return True

    return False
    

def illegal(grid):
    pass
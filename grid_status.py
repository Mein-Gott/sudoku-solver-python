from candidates_per_cell import candidates_per_cell
from split_into_groups import split_into_groups

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
    groupsets = split_into_groups(grid)

    for groupset in groupsets:
        for group in groupset:
            if group_illegal(group): return True
    
    return False


def group_illegal(group):
    used_numbers = []
    for cell in group:
        if cell == 0: continue
        if cell in used_numbers: return True

        used_numbers.append(cell)
        
    return False
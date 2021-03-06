from split_into_groups import *
from copy import deepcopy

def candidates_per_cell(grid):
    candidates = __generate_default_candidates()
    candidates = no_candidates_in_clue_cells(candidates, grid)


    candidates = eliminate_groupset_candidates(candidates, grid)

    candidates_in_columns = split_into_columns(candidates)
    grid_in_columns = split_into_columns(grid)
    eliminated_candidates_in_columns = eliminate_groupset_candidates(candidates_in_columns, grid_in_columns)
    candidates = split_into_columns(eliminated_candidates_in_columns)

    candidates_in_regions = split_into_regions(candidates)
    grid_in_regions = split_into_regions(grid)
    eliminated_candidates_in_regions = eliminate_groupset_candidates(candidates_in_regions, grid_in_regions)
    candidates = split_into_regions(eliminated_candidates_in_regions)

    return candidates


def no_candidates_in_clue_cells(candidates, grid):
    edited_candidates = deepcopy(candidates)
    for row_index, row in enumerate(grid):
        edited_candidates[row_index] = no_candidates_in_clue_cell_row(candidates[row_index], row)

    return edited_candidates

def no_candidates_in_clue_cell_row(candidate_row, row):
    edited_candidate_row = deepcopy(candidate_row)

    for cell_index, cell in enumerate(row):
        if cell != 0: 
            edited_candidate_row[cell_index] = []

    return edited_candidate_row


def eliminate_groupset_candidates(groupset_candidates, groupset):
    edited_groupset_candidates = deepcopy(groupset_candidates)

    for group_index, group in enumerate(groupset):
        edited_groupset_candidates[group_index] = eliminate_group_candidates(groupset_candidates[group_index], group)

    return edited_groupset_candidates

def eliminate_group_candidates(group_candidates, group):
    edited_group_candidates = deepcopy(group_candidates)

    for cell in group:
        edited_group_candidates = delete_value_from_group_candidates(edited_group_candidates, cell)

    return edited_group_candidates

def delete_value_from_group_candidates(group_candidates, value):
    edited_group_candidates = deepcopy(group_candidates)

    for candidates_of_cell in edited_group_candidates:
        if value in candidates_of_cell:
            candidates_of_cell.remove(value)

    return edited_group_candidates



def get_cell_with_least_candidates(grid):
    candidates = candidates_per_cell(grid)

    current_minimum = 10
    data = {}

    for row_index, candidate_row in enumerate(candidates):
        for column_index, cell_candidates in enumerate(candidate_row):
            if len(cell_candidates) == 0: continue
            if len(cell_candidates) < current_minimum:
                current_minimum = len(cell_candidates)
                data = {
                    'coordinates': {
                        'row': row_index, 
                        'column': column_index, 
                    },
                    'candidates': cell_candidates
                }

    return data



def __generate_default_candidates():
    default_candidates = []
    for i in range(9):
        default_candidates.append(__generate_default_row_candidates())
    return default_candidates

def __generate_default_row_candidates():
    default_row = []
    for i in range(9):
        default_row.append(__generate_default_cell_candidates())
    return default_row

def __generate_default_cell_candidates():
    default_cell = []
    for i in range(1, 10):
        default_cell.append(i)
    return default_cell

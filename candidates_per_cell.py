from split_into_groups import *
from copy import deepcopy

def candidates_per_cell(grid):
    candidates = __generate_default_candidates()
    candidates = delete_candidates_from_clue_cells(candidates, grid)


    candidates = eliminate_candidates_checking_groupset(candidates, grid)

    candidates_in_columns = split_into_columns(candidates)
    grid_in_columns = split_into_columns(grid)
    eliminated_candidates_in_columns = eliminate_candidates_checking_groupset(candidates_in_columns, grid_in_columns)
    candidates = split_into_columns(eliminated_candidates_in_columns)

    candidates_in_regions = split_into_regions(candidates)
    grid_in_regions = split_into_regions(grid)
    eliminated_candidates_in_regions = eliminate_candidates_checking_groupset(candidates_in_regions, grid_in_regions)
    candidates = split_into_regions(eliminated_candidates_in_regions)

    return candidates


def delete_candidates_from_clue_cells(candidates, grid):
    edited_candidates = deepcopy(candidates)
    for row_index, row in enumerate(grid):
        edited_candidates[row_index] = delete_candidates_from_clue_cell_row(candidates[row_index], row)

    return edited_candidates

def delete_candidates_from_clue_cell_row(candidate_row, row):
    edited_candidate_row = deepcopy(candidate_row)

    for cell_index, cell in enumerate(row):
        if cell != 0: 
            edited_candidate_row[cell_index] = []

    return edited_candidate_row


def eliminate_candidates_checking_groupset(groupset_candidates, groupset):
    edited_groupset_candidates = deepcopy(groupset_candidates)

    for group_index, group in enumerate(groupset):
        edited_groupset_candidates[group_index] = eliminate_candidates_group(groupset_candidates[group_index], group)

    return edited_groupset_candidates

def eliminate_candidates_group(group_candidates, group):
    edited_group_candidates = deepcopy(group_candidates)

    for cell in group:
        edited_group_candidates = eliminate_value_from_group_candidates(edited_group_candidates, cell)

    return edited_group_candidates

def eliminate_value_from_group_candidates(group_candidates, value):
    edited_group_candidates = deepcopy(group_candidates)

    for candidates_of_cell in edited_group_candidates:
        if value in candidates_of_cell:
            candidates_of_cell.remove(value)

    return edited_group_candidates




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

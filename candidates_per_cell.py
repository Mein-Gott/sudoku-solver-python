from tokenize import group
from split_into_groups import split_into_groups

def candidates_per_cell(grid):
    candidates = __generate_default_candidates()

    groupsets = split_into_groups(grid)
    candidates_in_groupsets = split_into_groups(candidates)

    for (groupset, groupset_candidates) in zip(groupsets, candidates_in_groupsets):
        candidates = eliminate_candidates_checking_groupset(groupset_candidates, groupset)


def eliminate_candidates_checking_groupset(groupset_candidates, groupset):
    edited_groupset_candidates = groupset_candidates.copy()

    for group_index, group in enumerate(groupset):
        edited_groupset_candidates = eliminate_group_candidates(groupset_candidates[group_index], group)

    return edited_groupset_candidates

def eliminate_group_candidates(group_candidates, group):
    edited_group_candidates = group_candidates.copy()

    for cell in group:
        edited_group_candidates = eliminate_value_from_group_candidates(edited_group_candidates, cell)

    return edited_group_candidates

def eliminate_value_from_group_candidates(group_candidates, value):
    edited_group_candidates = group_candidates.copy()

    for candidates_of_cell in edited_group_candidates:
        if value in candidates_of_cell:
            candidates_of_cell.remove(value)

    return edited_group_candidates




def __generate_default_candidates():
    default_candidates = []
    for i in range(9):
        default_candidates.append(__generate_default_row())
    return default_candidates

def __generate_default_row():
    default_row = []
    for i in range(9):
        default_row.append(__generate_default_cell())
    return default_row

def __generate_default_cell():
    default_cell = []
    for i in range(1, 10):
        default_cell.append(i)
    return default_cell

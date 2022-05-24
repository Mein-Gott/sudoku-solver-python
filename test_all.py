from typing import Counter
import unittest
from testing_data import *
from split_into_groups import *
from parse_to_list import *
from candidates_per_cell import *


class SplitIntoGroups(unittest.TestCase):
    def test_split_into_columns(self):
        test_columns = split_into_columns(region_rows)
        self.assertEqual(test_columns, region_columns)
    
    def test_split_into_regions(self):
        test_regions = split_into_regions(fake_grid_rows)
        self.assertEqual(test_regions, fake_grid_regions)

class ParseToList(unittest.TestCase):
    def test_add_comma_between(self):
        without_commas = [['123'],['321']]
        with_commas = [[1,2,3],[3,2,1]]

        commas_with_function = add_commas_between(without_commas)
        self.assertEqual(commas_with_function, with_commas)

class CandidatesPerCell(unittest.TestCase):
    def test_eliminate_value_from_group_candidates(self):
        no_fours = eliminate_value_from_group_candidates(group_candidates, 4)
        self.assertEqual(no_fours, group_candidates_no_four)

    def test_eliminate_whole_group(self):
        desired_candidates = eliminate_candidates_group(group_candidates, group_values)
        self.assertEqual(desired_candidates, group_candidates_eliminated)

    def test_eliminate_groupset(self):
        desired_candidates = eliminate_candidates_checking_groupset(groupset_candidates, groupset_clues)
        self.assertEqual(desired_candidates, eliminated_groupset_candidates)

    def test_delete_candidates_from_clue_cell_row(self):
        desired_candidates = delete_candidates_from_clue_cell_row(groupset_candidates[0], groupset_clues[0])
        self.assertEqual(desired_candidates, no_candidates_for_clue_cells[0])

    def test_delete_candidates_from_clue_cells(self):
        desired_candidates = delete_candidates_from_clue_cells(groupset_candidates, groupset_clues)
        self.assertEqual(desired_candidates, no_candidates_for_clue_cells)

    def test_candidates_per_cell(self):
        desired_candidates = candidates_per_cell(incomplete_grid)
        for desired_row_candidates, correct_row_candidates in zip(desired_candidates, incomplete_grid_candidates):
            for desired_cell_candidates, correct_cell_candidates in zip(desired_row_candidates, correct_row_candidates):
                self.assertTrue(Counter(desired_cell_candidates) == Counter(correct_cell_candidates))

if __name__ == '__main__':
    unittest.main()
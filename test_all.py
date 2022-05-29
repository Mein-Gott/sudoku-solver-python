from typing import Counter
import unittest
from solve_grid import *
from testing_data import *
from split_into_groups import *
from parse_to_list import *
from candidates_per_cell import *
from coordinates_of_singles import *
from add_singles import add_singles
from grid_status import *


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
        no_fours = delete_value_from_group_candidates(group_candidates, 4)
        self.assertEqual(no_fours, group_candidates_no_four)

    def test_eliminate_whole_group(self):
        generated_candidates = eliminate_group_candidates(group_candidates, group_values)
        self.assertEqual(generated_candidates, group_candidates_eliminated)

    def test_eliminate_groupset(self):
        generated_candidates = eliminate_groupset_candidates(groupset_candidates, groupset_clues)
        self.assertEqual(generated_candidates, eliminated_groupset_candidates)

    def test_delete_candidates_from_clue_cell_row(self):
        generated_candidates = no_candidates_in_clue_cell_row(groupset_candidates[0], groupset_clues[0])
        self.assertEqual(generated_candidates, no_candidates_for_clue_cells[0])

    def test_delete_candidates_from_clue_cells(self):
        generated_candidates = no_candidates_in_clue_cells(groupset_candidates, groupset_clues)
        self.assertEqual(generated_candidates, no_candidates_for_clue_cells)

    def test_candidates_per_cell(self):
        generated_candidates = candidates_per_cell(incomplete_grid)
        for generated_row_candidates, correct_row_candidates in zip(generated_candidates, incomplete_grid_candidates):
            for generated_cell_candidates, correct_cell_candidates in zip(generated_row_candidates, correct_row_candidates):
                self.assertTrue(Counter(generated_cell_candidates) == Counter(correct_cell_candidates))

    def test_cell_with_least_candidates(self):
        generated_cell = get_cell_with_least_candidates(incomplete_grid)
        self.assertEqual(generated_cell, correct_least_candidate_cell)


class CoordinatesOfSingles(unittest.TestCase):
    def test_coordinates_of_singles(self):
        generated_single_coords = coordinates_of_singles(incomplete_grid_candidates)
        for generated_coords, correct_coords in zip(generated_single_coords, incomplete_grid_single_coords):
            self.assertEqual(generated_coords, correct_coords)

    def test_number_of_coords(self):
        generated_single_coords = coordinates_of_singles(incomplete_grid_candidates)
        self.assertEqual(len(generated_single_coords), 4)


class AddSingles(unittest.TestCase):
    def test_add_singles(self):
        generated_grid = add_singles(incomplete_grid)
        self.assertEqual(generated_grid, complete_grid)


class GridStatus(unittest.TestCase):
    def test_is_complete(self):
        self.assertFalse(is_complete(incomplete_grid))
        self.assertTrue(is_complete(complete_grid))

    def test_in_impossible_state(self):
        self.assertTrue(in_impossible_state(impossible_grid))
        self.assertFalse(in_impossible_state(incomplete_grid))

    def test_group_illegal(self):
        self.assertTrue(group_illegal(illegal_group))
        self.assertFalse(group_illegal(legal_group))

    def test_illegal(self):
        self.assertTrue(illegal(illegal_grid_region))
        self.assertTrue(illegal(illegal_grid_row))
        self.assertTrue(illegal(illegal_grid_column))

        self.assertFalse(illegal(incomplete_grid))


class SolveGrid(unittest.TestCase):
    def test_grid_with_no_guessing(self):
        solved_grid = solve_grid(incomplete_grid)
        self.assertEqual(solved_grid['status'], 'complete')
        self.assertEqual(solved_grid['grid'], complete_grid)

    def test_impossible_grid(self):
        solved_grid = solve_grid(impossible_grid)
        self.assertEqual(solved_grid['status'], 'not solvable')

    def test_illegal_grid(self):
        should_be_illegal = solve_grid(illegal_grid_region)
        self.assertEqual(should_be_illegal['status'], 'not solvable')

        should_be_legal = solve_grid(incomplete_grid)
        self.assertNotEqual(should_be_legal['status'], 'not solvable')

    def test_whole_algorithm(self):
        solved_grid = solve_grid(less_clues)
        self.assertEqual(solved_grid['status'], 'complete')
        self.assertEqual(solved_grid['grid'], complete_grid)


class GridValueEditing(unittest.TestCase):
    def test_add_value(self):
        coords = {'row': 1, 'column': 6}
        generated_grid = add_value(incomplete_grid, coords, 7)
        self.assertEqual(generated_grid, seven_added_1_6)

    def test_delete_value(self):
        coords = {'row': 1, 'column': 6}
        generated_grid = delete_value(seven_added_1_6, coords)
        self.assertEqual(generated_grid, incomplete_grid)



if __name__ == '__main__':
    unittest.main()
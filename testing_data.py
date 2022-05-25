from parse_to_list import *

region_rows = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
region_columns = [[1,4,7],[2,5,8],[3,6,9]]


fake_grid_rows = [
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9]
]
fake_grid_columns = [
    [1,1,1,1,1,1,1,1,1],
    [2,2,2,2,2,2,2,2,2],
    [3,3,3,3,3,3,3,3,3],
    [4,4,4,4,4,4,4,4,4],
    [5,5,5,5,5,5,5,5,5],
    [6,6,6,6,6,6,6,6,6],
    [7,7,7,7,7,7,7,7,7],
    [8,8,8,8,8,8,8,8,8],
    [9,9,9,9,9,9,9,9,9]
]
fake_grid_regions = [
    [1,2,3,1,2,3,1,2,3],
    [4,5,6,4,5,6,4,5,6],
    [7,8,9,7,8,9,7,8,9],
    [1,2,3,1,2,3,1,2,3],
    [4,5,6,4,5,6,4,5,6],
    [7,8,9,7,8,9,7,8,9],
    [1,2,3,1,2,3,1,2,3],
    [4,5,6,4,5,6,4,5,6],
    [7,8,9,7,8,9,7,8,9]
]

# This is the sudoku from the Notion page

__incomplete_grid = [
    ['530070000'],
    ['600195000'],
    ['098000060'],
    ['800060003'],
    ['400803001'],
    ['700020006'],
    ['060000280'],
    ['000419005'],
    ['000080079']
]
incomplete_grid = add_commas_between(__incomplete_grid)

incomplete_grid_candidates = [
    [
        [],
        [],
        [1,2,4],
        [2,6],
        [],
        [2,4,6,8],
        [1,4,8,9],
        [1,2,4,9],
        [2,4,8]
    ],
    [
        [],
        [2,4,7],
        [2,4,7],
        [],
        [],
        [],
        [3,4,7,8],
        [2,3,4],
        [2,4,7,8]
    ],
    [
        [1,2],
        [],
        [],
        [2,3],
        [3,4],
        [2,4],
        [1,3,4,5,7],
        [],
        [2,4,7]
    ],

    ####
    [
        [],
        [1,2,5],
        [1,2,5,9],
        [5,7,9],
        [],
        [1,4,7],
        [4,5,7,9],
        [2,4,5,9],
        []
    ],
    [
        [],
        [2,5],
        [2,5,6,9],
        [],
        [5],
        [],
        [5,7,9],
        [2,5,9],
        []
    ],
    [
        [],
        [1,5],
        [1,3,5,9],
        [5,9],
        [],
        [1,4],
        [4,5,8,9],
        [4,5,9],
        []
    ],

    ####
    [
        [1,3,9],
        [],
        [1,3,4,5,7,9],
        [3,5,7],
        [3,5],
        [7],
        [],
        [],
        [4]
    ],
    [
        [2,3],
        [2,7,8],
        [2,3,7],
        [],
        [],
        [],
        [3,6],
        [3],
        []
    ],
    [
        [1,2,3],
        [1,2,4,5],
        [1,2,3,4,5],
        [2,3,5,6],
        [],
        [2,6],
        [1,3,4,6],
        [],
        []
    ]
]

incomplete_grid_single_coords = [
    {'row': 4, 'column': 4, 'value': 5},
    {'row': 6, 'column': 5, 'value': 7},
    {'row': 6, 'column': 8, 'value': 4},
    {'row': 7, 'column': 7, 'value': 3}
]

correct_least_candidate_cell = {
    'coordinates': {
        'row': 4, 
        'column': 4, 
    },
    'candidates': [5]
}

__complete_grid = [
    ['534678912'],
    ['672195348'],
    ['198342567'],
    ['859761423'],
    ['426853791'],
    ['713924856'],
    ['961537284'],
    ['287419635'],
    ['345286179']
]
complete_grid = add_commas_between(__complete_grid)

__impossible_grid = [
    ['530070000'],
    ['600195000'],
    ['098000060'],
    ['800060003'],
    ['400803001'],
    ['700020006'],
    ['060000280'],
    ['000419305'],
    ['000080079']
]
impossible_grid = add_commas_between(__impossible_grid)


group_candidates = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
]
group_values = [1,3,0,0]
group_candidates_eliminated = [
    [2,4],
    [2,4],
    [2,4],
    [2,4]
]
group_candidates_no_four = [
    [1,2,3],
    [1,2,3],
    [1,2,3],
    [1,2,3]
]

groupset_candidates = [
    [[1,2,3],[1,2,3],[1,2,3]],
    [[2,3,4],[2,3,4],[2,3,4]],
    [[3,4,5],[3,4,5],[3,4,5]]
]
groupset_clues = [
    [1,0,0],
    [0,2,3],
    [0,0,4]
]
eliminated_groupset_candidates = [
    [[2,3],[2,3],[2,3]],
    [[4],[4],[4]],
    [[3,5],[3,5],[3,5]]
]
no_candidates_for_clue_cells = [
    [[],[1,2,3],[1,2,3]],
    [[2,3,4],[],[]],
    [[3,4,5],[3,4,5],[]]
]

illegal_group = [1,0,2,0,4,5,1,0,8]
legal_group = [1,0,3,4,0,6,7,8,0]

__illegal_grid_region = [
    ['530070000'],
    ['603195000'],
    ['098000060'],
    ['800060003'],
    ['400803001'],
    ['700020006'],
    ['060000280'],
    ['000419005'],
    ['000080079']
]
illegal_grid_region = add_commas_between(__illegal_grid_region)

__illegal_grid_row = [
    ['530070700'],
    ['600195000'],
    ['098000060'],
    ['800060003'],
    ['400803001'],
    ['700020006'],
    ['060000280'],
    ['000419005'],
    ['000080079']
]
illegal_grid_row = add_commas_between(__illegal_grid_row)

__illegal_grid_column = [
    ['530070000'],
    ['600195000'],
    ['098000060'],
    ['800060003'],
    ['400803201'],
    ['700020006'],
    ['060000280'],
    ['000419005'],
    ['000080079']
]
illegal_grid_column = add_commas_between(__illegal_grid_column)


__less_clues = [
    ['030000000'],
    ['000195000'],
    ['008000060'],
    ['800060000'],
    ['400800001'],
    ['000020000'],
    ['060000280'],
    ['000419005'],
    ['000000070']
]
less_clues = add_commas_between(__less_clues)


__seven_added_1_6 = [
    ['530070000'],
    ['600195700'],
    ['098000060'],
    ['800060003'],
    ['400803001'],
    ['700020006'],
    ['060000280'],
    ['000419005'],
    ['000080079']
]
seven_added_1_6 = add_commas_between(__seven_added_1_6)
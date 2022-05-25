from copy import deepcopy

def split_into_groups(grid):
    rows = deepcopy(grid)
    columns = split_into_columns(rows)
    regions = split_into_regions(grid)

    return [rows, columns, regions]

def split_into_columns(rows):
    columns = []
    for i in range(len(rows)):
        columns.append([])

    for row in rows:
        for column_index, cell_value in enumerate(row):
            columns[column_index].append(cell_value)

    return columns

def split_into_regions(grid):
    regions = []

    for add_to_row_i in range(0, 7, 3):
        for add_to_column_i in range(0, 7, 3):
            region = []

            for row_i in range(3):
                for column_i in range(3):
                    region.append(grid[row_i + add_to_row_i][column_i + add_to_column_i])

            regions.append(region)

    return regions
         
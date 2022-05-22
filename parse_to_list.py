
def add_commas_between(grid):
    comma_separated_grid = []
    for row in grid: comma_separated_grid.append(__separate_row(row))
    return comma_separated_grid

def __separate_row(row):
    separated_row = []
    actual_string = row[0]
    for str_number in actual_string: separated_row.append(int(str_number))
    return separated_row

def coordinates_of_singles(candidates):
    coordinates_of_singles = []

    for row_index, candidate_row in enumerate(candidates):
        for cell_index, cell_candidates in enumerate(candidate_row):
            if len(cell_candidates) == 1:
                coordinates = {
                    'row': row_index, 
                    'column': cell_index, 
                    'value': cell_candidates[0]
                }

                coordinates_of_singles.append(coordinates)

    return coordinates_of_singles


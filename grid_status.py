
def is_complete(grid):
    for row in grid:
        for cell in row:
            if cell == 0: return False

    return True
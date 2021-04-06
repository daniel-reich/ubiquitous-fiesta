
def crop_hydrated(field):
    rows, cols = len(field), len(field[0])
    for r in range(rows):
        for c in range(cols):
            if field[r][c] == 'c':
                found_water = False
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if (not (i == j == 0) and
                                0 <= r + i < rows and 0 <= c + j < cols
                                and field[r + i][c + j] == 'w'):
                            found_water = True
                            break
                    if found_water:
                        break
                if not found_water:
                    return False
    return True


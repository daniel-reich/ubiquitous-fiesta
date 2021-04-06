
def crop_hydrated(field):
    options_to_visit = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, -1), (1, 0)]
​
    for row_idx in range(0, len(field)):
        for col_idx in range(0, len(field[row_idx])):
            if field[row_idx][col_idx] == "c":
                for x, y in options_to_visit:
                    if 0 <= row_idx+x < len(field) and 0 <= col_idx+y < len(field[row_idx]):
                        if field[row_idx+x][col_idx+y] == 'w':
                            break
                else:
                    return False
    else:
        return True


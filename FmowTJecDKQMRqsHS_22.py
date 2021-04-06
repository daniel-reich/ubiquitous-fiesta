
def get_neighbours(r, c):
    return ((r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), 
            (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1))
​
def crop_hydrated(field):
    rows, cols = len(field), len(field[0])
    for r in range(rows):
        for c in range(cols):
            if field[r][c] == 'c' and not any(field[i][j] == 'w' for i, j in get_neighbours(r, c) \
                if 0 <= i < rows and 0 <= j < cols):
                return False
    return True


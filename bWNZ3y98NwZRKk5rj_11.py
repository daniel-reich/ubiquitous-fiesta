
def block_player(a, b):
    rows = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1, 4, 7,), (2,5,8),
            (0,4,8), (2,4,6)]
    row = get_row(a, b, rows)
    for x in row:
        if a != x and b != x:
            return x
​
def get_row(a, b, rows):
    for row in rows:
        if a in row and b in row:
            return row



def magic_square_game(alice, bob):
    (row, x), (col, y) = alice, bob
    return y[row-1] == x[col-1]


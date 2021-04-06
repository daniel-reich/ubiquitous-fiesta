
def chess_board(pole):
    col, row = "abcdefgh".index(pole[0]), int(pole[1]) - 1
    return ("black" if row % 2 and col % 2 or (not row % 2 and not col % 2)
            else "white")


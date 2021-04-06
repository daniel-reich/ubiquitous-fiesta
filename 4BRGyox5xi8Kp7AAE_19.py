
def chess_board(pole):
    line = pole[0]
    coll = int(pole[1])
    if (line in 'aceg' and coll in [1, 3, 5, 7]) or (line in 'bdfh' and coll in [2, 4, 6, 8]):
        return 'black'
    return 'white'


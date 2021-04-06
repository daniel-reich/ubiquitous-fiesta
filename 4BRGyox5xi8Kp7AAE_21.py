
def chess_board(pole):
    return ['black','white'][int((ord(pole[0]) + int(pole[1]))%2!=0)]



def chess_board(pole):
  a = 'abcdefgh'
  return 'black' if (a.index(pole[0])+int(pole[1]))%2 else 'white'


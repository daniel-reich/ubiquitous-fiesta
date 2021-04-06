
def chess_board(pole):
  A='abcdefgh'
  return ['black', 'white'][((A.index(pole[0])+1)+int(pole[1]))%2]


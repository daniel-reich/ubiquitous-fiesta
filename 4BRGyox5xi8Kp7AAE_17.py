
def chess_board(pole):
  hori = 'abcdefgh'
  return 'white' if hori.find(pole[0])%2==int(pole[1])%2 else 'black'


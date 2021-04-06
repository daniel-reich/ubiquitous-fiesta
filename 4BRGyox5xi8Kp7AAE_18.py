
def chess_board(pole):
  n = pole[0] in 'aceg'
  m = int(pole[1])
  if int(m)%2 == n:
    return 'black'
  return 'white'



def chess_board(pole):
  odds = 'aceg'
  cell = int(pole[1])
  if cell%2==0:
    if pole[0] in odds:
      return 'white'
    else:
      return 'black'
  else:
    if pole[0] in odds:
      return 'black'
    else:
      return 'white'


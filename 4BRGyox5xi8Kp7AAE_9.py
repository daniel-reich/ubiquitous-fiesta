
def chess_board(pole):
  x=pole[:1]
  y=pole[1:]
  if ord(x) % 2 == 1:
    if int(y) % 2 == 1:
      return('black')
    else:
      return('white')
  elif ord(x) % 2 == 0:
    if int(y) % 2 == 0:
      return('black')
    else:
      return('white')


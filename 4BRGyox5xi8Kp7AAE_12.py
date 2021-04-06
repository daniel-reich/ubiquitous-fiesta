
def chess_board(p):
  if ord(p[0]) % 2 == 1 and int(p[1]) % 2 == 1: return 'black'
  if ord(p[0]) % 2 == 0 and int(p[1]) % 2 == 0: return 'black'
  return 'white'


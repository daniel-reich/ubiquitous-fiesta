
def chess_board(p):
  b=['a','c','e','g']
  w=['d','c','f','h']
  if (p[0] in b and int(p[1])%2!=0) or (p[0] in w and int(p[1])%2==0):
    return 'black'
  else:
    return 'white'


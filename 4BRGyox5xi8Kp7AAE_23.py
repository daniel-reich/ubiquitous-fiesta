
def chess_board(p):
  return "black" if "abcdefgh".index(p[0])%2 ^ int(p[1])%2 else "white"


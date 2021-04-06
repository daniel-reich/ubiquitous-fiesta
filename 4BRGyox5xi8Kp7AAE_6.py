
def chess_board(pole):
  whiteEvens = pole[0] in "aceg"
  if int(pole[1]) % 2 == 0:
    return "white" if whiteEvens else "black"
  return "black" if whiteEvens else "white"


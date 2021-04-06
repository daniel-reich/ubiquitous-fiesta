
def chess_board(pole):
  return ["black","white"][sum(map(ord,pole))%2]


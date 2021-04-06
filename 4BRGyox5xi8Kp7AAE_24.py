
def chess_board(pole):
  letter = pole[0]
  digit = int(pole[1])
  if ord(letter) % 2 == digit % 2:
    return "black"
  else:
    return "white"


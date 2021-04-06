
def chess_board(pole):
  return ["black", "white"][(ord(pole[0]) + int(pole[1])) % 2];


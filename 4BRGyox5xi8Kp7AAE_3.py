
def chess_board(pole):
  column, row = pole
  code = ord(column) + int(row)
  return ['black', 'white'][code % 2]


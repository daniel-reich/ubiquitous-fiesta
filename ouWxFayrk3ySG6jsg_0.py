
def who_won(board):
  return 'X' if sum(sq == 'X' for row in board for sq in row) == 5 else 'O'


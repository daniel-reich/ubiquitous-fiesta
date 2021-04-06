
def x_and_o(board):
  board = [1 if j=="X" else -1 if j=="O" else 0 for i in board for j in i if j!="|"]
  for i in (
    # horizontal
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    # vertical
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    # diagonals
    (0, 4, 8),
    (2, 4, 6),
  ):
    if sum(board[j] for j in i)==2:
      for j in i:
        if board[j] == 0:
          return [j//3 + 1, j%3 + 1]
  return False


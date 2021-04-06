
def bingo_check(board):
  try:
    indices = list(map(lambda x: x.index("x"),board))
    if indices == [0,1,2,3,4]:
      return True
    elif indices == [4,3,2,1,0]:
      return True
    else:
      return len(set(indices)) == 1
  except ValueError:
    for i in range(0,len(board)):
      if board[i].count("x") == 5:
        return True
    return False


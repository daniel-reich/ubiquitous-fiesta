
def bingo_check(board):
  hori = any(True for i in range(5) if board[i] == ["x","x","x","x","x"])
  cols = [j for i in range(5) for j in range(5) if board[i][j] == "x"]
  vert = any([True for i in range(5) if cols.count(i) == 5])
  dia1 = all([True if board[i][i] == "x" else False for i in range(5)])
  dia2 = all([True if board[i][4-i] == "x" else False for i in range(5)])
  return hori or vert or dia1 or dia2


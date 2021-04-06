
def check_board(col, row):
  board = [[0 for _ in range(8)] for _ in range(8)]
  for i in range(8):
    board[i][ord(col)-97] = 1
    board[len(board)-(row)][i] = 1
    if ord(col)-97+i < 8 and row-1+i < 8:
      board[len(board)-(row+i)][(ord(col)-97+i)] = 1
    if ord(col)-97+i < 8 and 0 <= row-1-i:
      board[len(board)-(row-i)][(ord(col)-97+i)] = 1
    if 0 <= ord(col)-97-i and row-1+i < 8:
      board[len(board)-(row+i)][(ord(col)-97-i)] = 1
    if 0 <= ord(col)-97-i and 0 <= row-1-i:
      board[len(board)-(row-i)][(ord(col)-97-i)] = 1
  
  board[len(board)-row][ord(col)-97] = 0
​
  return board


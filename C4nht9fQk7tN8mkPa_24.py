
def cannot_capture(board):
  return all(check_place(board, i, row) for row in range(8) for i in range(8) if board[row][i] == 1)
        
def check_place(board, i, row):
  lst = [(2, 1),(2, -1),(-2, 1),(-2, -1)]
  for x,y in lst:
    try: 
      if board[abs(row + x)][abs(i + y)]: return False
    except: continue
  for x,y in lst:
    try: 
      if board[abs(row + y)][abs(i + x)] == 1: return False
    except: continue
  return True


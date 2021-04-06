
def can_traverse(board):
​
  cur_value = 0
  last_value = 0
​
  for i in range(len(board[0])):
    
    cur_value = (board[0][i]+board[1][i]+board[2][i]+board[3][i])
​
    if cur_value - last_value > 1:
      return False  
​
    if last_value - cur_value > 1:
      return False
​
    last_value = (board[0][i] + board[1][i] + board[2][i] + board[3][i])
    
​
  return True


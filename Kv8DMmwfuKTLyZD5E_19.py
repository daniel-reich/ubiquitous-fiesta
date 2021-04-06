
def make_dartboard(n):
  board = [[1]*n]
  
  for i in range(n//2):
    next_row = [board[-1][j]+1 if j in range(i+1,n-i-1) else board[-1][j] for j in range(len(board[-1]))]
    board.append(next_row)
  board += board[:n-len(board)][::-1]
  
  return [int(''.join(str(i) for i in row)) for row in board]


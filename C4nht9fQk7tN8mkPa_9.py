
def cannot_capture(board):
  positions = []
  
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 1:
        positions.append((i,j))
        
  for k in range(len(positions)):
    for l in range(k+1, len(positions)):
      delta_x_sqd = (positions[k][0] - positions[l][0])**2
      delta_y_sqd = (positions[k][1] - positions[l][1])**2
      
      if delta_x_sqd + delta_y_sqd == 5:
        return False
        
  return True


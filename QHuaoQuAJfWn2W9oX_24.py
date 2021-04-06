
def check_board(letter, number):
  board = [ [ 0 for i in range(8) ] for j in range(8) ]
  letters = 'abcdefgh'
  board[8 - number][letters.index(letter)] = 'Q'
  dist_left = letters.index(letter)   # the four "dist" variables tell how far the Queen is from the 4 edges of the board
  dist_right = 7 - dist_left
  dist_down = number - 1
  dist_up = 8 - number
  for i in range(8):    # put 1's in all squares that are in same row as Q
    if board[8 - number][i] == 0:
      board[8 - number][i] = 1
  for i in range(8):    # put 1's in all squares that are in same column as Q
    if board[i][letters.index(letter)] == 0:
      board[i][letters.index(letter)] = 1
      
    # now, want to fill in the diagonals:
    
    # start with quadrant 1: up and right
  limit = min(dist_up, dist_right)
  for i in range(1, limit+1):
    board[8 - number - i][letters.index(letter) + i] = 1
  
    # quadrant 2: up and left
  limit = min(dist_up, dist_left)
  for i in range(1, limit+1):
    board[8 - number - i][letters.index(letter) - i] = 1
  
    # quadrant 3: down and left
  limit = min(dist_down, dist_left)
  for i in range(1, limit+1):
    board[8 - number + i][letters.index(letter) - i] = 1
  
    # quadrant 4: down and right
  limit = min(dist_down, dist_right)
  for i in range(1, limit+1):
    board[8 - number + i][letters.index(letter) + i] = 1
  board[8 - number][letters.index(letter)] = 0
  return board


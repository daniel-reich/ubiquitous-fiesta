
class Sudoku:
​
  def __init__(self, raw_board):
    
    board = []
    row = []
​
    current_n = 0
    n = 0
    
    while current_n < len(raw_board):
      if n == 9:
        board.append(row)
        row = []
        n = 0
      
      row.append(int(raw_board[current_n]))
​
      current_n += 1
      n += 1
    
    board.append(row)
    self.board = board
​
    self.rows = {}
    for n in range(len(board)):
      self.rows[n] = board[n]
    
    self.cols = {}
    for n in range(len(board[0])):
      col = []
      for row in board:
        col.append(row[n])
      self.cols[n] = col
    
    s0 = []
    s0spots = []
    s1 = []
    s1spots = []
    s2 = []
    s2spots = []
​
    for num in range(0, 3):
      for n in range(0, 3):
        s0.append(board[num][n])
        s0spots.append('{},{}'.format(num,n))
      for n in range(3, 6):
        s1.append(board[num][n])
        s1spots.append('{},{}'.format(num,n))
      for n in range(6, 9):
        s2.append(board[num][n])
        s2spots.append('{},{}'.format(num,n))
    
    
    s3 = []
    s3spots = []
    s4 = []
    s4spots = []
    s5 = []
    s5spots = []
​
    for num in range(3, 6):
      for n in range(0, 3):
        s3.append(board[num][n])
        s3spots.append('{},{}'.format(num,n))
      for n in range(3, 6):
        s4.append(board[num][n])
        s4spots.append('{},{}'.format(num,n))
      for n in range(6, 9):
        s5.append(board[num][n])
        s5spots.append('{},{}'.format(num,n))
    
    s6 = []
    s6spots = []
    s7 = []
    s7spots = []
    s8 = []
    s8spots = []
​
    for num in range(6, 9):
      for n in range(0, 3):
        s6.append(board[num][n])
        s6spots.append('{},{}'.format(num,n))
        pass
      for n in range(3, 6):
        s7.append(board[num][n])
        s7spots.append('{},{}'.format(num,n))
        pass
      for n in range(6, 9):
        s8.append(board[num][n])
        s8spots.append('{},{}'.format(num,n))
        pass
    self.squares = {0: s0, 1: s1, 2: s2, 3: s3, 4: s4, 5: s5, 6: s6, 7: s7, 8: s8}
​
    self.spot_squares = {0: s0spots, 1: s1spots, 2: s2spots, 3: s3spots, 4: s4spots, 5: s5spots, 6: s6spots, 7: s7spots, 8: s8spots}
​
  def get_row(self, row):
    return self.rows[row]
  
  def get_col(self, col):
    return self.cols[col]
  
  def get_sqr(self, *inpts):
    if len(inpts) == 1:
      return self.squares[inpts[0]]
    elif len(inpts) == 2:
      goal = '{},{}'.format(inpts[0], inpts[1])
      for n in range(9):
        if goal in self.spot_squares[n]:
          return self.squares[n]
    else:
      return 'Incorrect length of Inputs! {}'.format(inpts)


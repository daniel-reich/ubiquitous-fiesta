
def bingo_check(board):
​
  class Board:
​
    def __init__(self, board):
​
      self.board = board
      self.cols = []
​
      for n in range(len(self.board[0])):
        col = []
        for row in self.board:
          col.append(row[n])
        self.cols.append(col)
      
      d1 = []
      d2 = []
​
      num = 0
​
      for n in range(len(self.board)):
        d1.append(self.board[n][num])
        num += 1
        d2.append(self.board[n][-num])
      
      self.diags = [d1, d2]
​
      self.bingo = False
​
      for row in self.board:
        if list(set(row)) == ['x']:
          self.bingo = True
          break
      
      for col in self.cols:
        if list(set(col)) == ['x']:
          self.bingo = True
          break
      
      for diag in self.diags:
        if list(set(diag)) == ['x']:
          self.bingo = True
          break
      
  board = Board(board)
​
  return board.bingo


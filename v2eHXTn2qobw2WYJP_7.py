
def minesweeper_numbers(board):
​
  class Board:
    class Space:
      
      def __init__(self, bomb, r, c, mr, mc, val = 9):
        self.bomb = bomb
        self.row  = r
        self.col = c
        self.maxrow = mr-1
        self.maxcol = mc-1
        self.val = val
      
        nearby_rows = [self.row]
        nearby_cols = [self.col]
​
        if self.row != 0:
          nearby_rows.append(self.row - 1)
        if self.row != self.maxrow:
          nearby_rows.append(self.row + 1)
        
        if self.col != 0:
          nearby_cols.append(self.col - 1)
        if self.col != self.maxcol:
          nearby_cols.append(self.col + 1)
        
        self.nearby = []
​
        for row in nearby_rows:
          for col in nearby_cols:
            space = '{},{}'.format(row, col)
            if space != '{},{}'.format(self.row, self.col):
              self.nearby.append(space)
      
      def nearby_mines(self, spaces):
        if self.bomb == False:
          mine_count = 0
​
          for space in self.nearby:
            if spaces[space].bomb == True:
              mine_count += 1
        
          self.val = mine_count
        
        return True
    
    def __init__(self, rawboard):
      
      self.raw = rawboard
      self.spaces = {}
​
      for r in range(len(rawboard)):
        for c in range(len(rawboard[0])):
          space = '{},{}'.format(r, c)
          bomb = rawboard[r][c] == 1
​
          self.spaces[space] = Board.Space(bomb, r, c, len(rawboard), len(rawboard[0]))
​
    def update(self):
      for space in self.spaces.values():
        space.nearby_mines(self.spaces)
      return True
​
    def display(self):
      tr = []
​
      for r in range(len(self.raw)):
        row = []
        for c in range(len(self.raw[0])):
          row.append(self.spaces['{},{}'.format(r,c)].val)
        tr.append(row)
      
      return tr
​
  board = Board(board)
  board.update()
  return board.display()


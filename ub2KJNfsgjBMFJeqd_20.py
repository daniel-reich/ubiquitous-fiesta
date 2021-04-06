
class Game:
  def __init__(self, rows=14, cols=18, mines=40):
    Cell.count = 0
    self.rows = rows
    self.cols = cols
    self.mines = mines
    self.board = [[Cell(r, c, mines) for c in range(cols)] for r in range(rows)]
    
    for row in self.board:
      for cell in row:
        around = []
        x = cell.row
        y = cell.col
        coords = [[x-1,y-1], [x-1,y], [x-1,y+1], [x,y-1], 
                  [x, y+1], [x+1,y-1], [x+1,y], [x+1,y+1]]
        for coord in coords:
          if coord[0] >= 0 and coord[1] >= 0:
            try:
              around.append(self.board[coord[0]][coord[1]].mine)
            except IndexError:
              pass
        cell.bombs_around(sum(around))
​
class Cell:
  count = 0
  def __init__(self, row, col, mines):
    self.row = row
    self.col = col
    
    self.mine = False
    if Cell.count < mines:
      self.mine = True
    Cell.count += 1
    
    self.flag = False
    self.open = False
    self.neighbors = None
    
  def bombs_around(self, the_sum):
    self.neighbors = the_sum


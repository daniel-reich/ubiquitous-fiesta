
class Game:
  def __init__(self, rows = 14, cols = 18, mines = 40):
    self.rows = rows
    self.cols = cols
    self.mines = mines
    self.__minecount__ = 0
    self.board = [[
      Cell(row, col, self.__lay_mine__(), self) for col in range(0, cols)
    ] for row in range(0, rows)]
​
  def __lay_mine__(self):
    if self.__minecount__ >= self.mines:
      return False
    self.__minecount__ += 1
    return True
    
  def __str__(self):
    return '\n'.join(['|'.join([str(cell) for cell in row]) for row in self.board])
      
​
class Cell:
  def __init__(self, row, col, mine, game):
    self.row = row
    self.col = col
    self.mine = mine
    self.game = game
    self.flag = False
    self.open = False
    
  @property
  def neighbors(self):
    top_index = max(self.row - 1, 0)
    bottom_index = min(self.row + 2, self.game.rows)
    left_index = max(self.col - 1, 0)
    rightIndex = min(self.col + 2, self.game.cols)
    mines = []
    for row in self.game.board[top_index:bottom_index]:
      mines += [1 if cell.mine else 0 for cell in row[left_index:rightIndex]]
    return sum(mines) - (1 if self.mine else 0)
      
  def __str__(self):
    return 'X' if self.mine else ' '


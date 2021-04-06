
import random
class Game:
  def __init__(self, rows = 14, cols = 18, mines = 40):
    self.rows = rows
    self.cols = cols
    self.mines = mines
    self.board = []
    self.init_board()
  def i_bomb(self, cl):
    surrounding = [
    (cl.col + 1, cl.row), (cl.col + 1, cl.row + 1), (cl.col, cl.row + 1), (cl.col - 1, cl.row + 1), 
    (cl.col - 1, cl.row), (cl.col - 1, cl.row - 1), (cl.col, cl.row - 1), (cl.col + 1, cl.row - 1),
    ]
    num_s = 0
    for coord in surrounding:
      if coord[0] < 0 or coord[0] >= self.cols or coord[1] < 0 or coord[1] >= self.rows:
        continue
      if self.board[coord[1]][coord[0]].mine:
        num_s += 1
    cl.neighbors = num_s
​
  def bomb_updater(self):
    for row in self.board:
      for c in row:
        self.i_bomb(c)
​
​
  def init_board(self):
    #generating bombs coords
    p_m_coord_ls = []
    if self.mines > self.rows * self.cols:
      raise ValueError('Number of mines exceed number of available cells.')
    i = 0
    while i < self.mines:
      y0 = random.randint(0, self.rows - 1)
      x0 = random.randint(0, self.cols - 1)
      if (x0, y0) in p_m_coord_ls:
        continue
      p_m_coord_ls.append((x0, y0))
      i += 1
    #placing everything by row
    for y in range(self.rows):
      row = []
      for x in range(self.cols):
        if (x, y) in p_m_coord_ls:
          row.append(Cell(y, x, True))
        else:
          row.append(Cell(y, x, False))
      self.board.append(row[:])
    #updating b
    self.bomb_updater()
​
​
class Cell:
  def __init__(self, row, col, mine):
    self.row = row
    self.col = col
    self.mine = mine
    self.flag = False
    self.open = False
    self.neighbors = 0


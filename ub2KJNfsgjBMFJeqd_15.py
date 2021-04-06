
import random
​
class Game:
  def __init__(self, rows=14, cols=18, mines=40):
    self.rows = rows
    self.cols = cols
    self.mines = mines
    self.board = []
    self.new_game()
    
  def new_game(self):
    # init mine positions
    mine_pos = [0]*(self.rows * self.cols)
    while sum(mine_pos) < self.mines:
      mine_pos[random.randint(0, len(mine_pos) - 1)] = 1
      
    # define Cells
    for i in range(self.rows):
      self.board.append([])
      for j in range(self.cols):
        # Check the neighbor chell values
        neighbor_values = 0
        for m in range(-1,2):
          x = i + m
          for n in range(-1,2):
            y = j + n
            if 0 <= x < self.rows and 0 <= y < self.cols and not (m == 0 and n == 0):
              neighbor_values += mine_pos[x * self.cols + y]
        self.board[i].append(Cell(i, j, mine_pos[i * self.cols + j], neighbor_values))  
  
  
class Cell:
  def __init__(self, row, col, mine, neighbors=0):
    self.row = row
    self.col = col
    self.mine = mine
    self.flag = False
    self.open = False
    self.neighbors = neighbors


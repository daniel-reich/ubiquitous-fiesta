
import random
​
def get_random_board_pos(board):
  return board[random.choice(range(len(board)))][random.choice(range(len(board[0])))]
​
​
class Game:
  def __init__(self, rows=14, cols=18, mines=40):
    self.rows = rows
    self.cols = cols
    self.mines = mines
    #mine_coords = [(random.choice(range(self.cols)), random.choice(range(self.rows))) for m in range(self.mines)]
    self.board = [[Cell(row=r,col=c)  for c in range(self.cols)] for r in range(self.rows)]
    for m in range(mines):
      cell = get_random_board_pos(self.board)
      while cell.mine:
        cell = get_random_board_pos(self.board)
      cell.set_mine(self)
      
  def get_cell(self, row, col):
    return self.board[row][col]
      
​
class Cell:
  def __init__(self, row, col, flag=False, o=False, mine=False):
    self.row = row
    self.col = col
    self.flag= flag
    self.open = o
    self.neighbors = 0
    self.mine = mine
    
  def get_neighbors(self):
    col = self.col
    row = self.row
    return [(row - 1,col - 1), (row, col - 1), (row + 1, col - 1), (row - 1, col), (row + 1, col), (row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]
    
  def set_mine(self, game):
    self.mine = True
    for r,c in self.get_neighbors():
      if r >= 0 and c >= 0 and r < game.rows and c < game.cols:
        game.get_cell(r,c).neighbors += 1


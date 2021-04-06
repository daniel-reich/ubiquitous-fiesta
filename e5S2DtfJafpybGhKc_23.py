
def rotate(mat):
  
  class Grid:
    
    def __init__(self, grid):
      self.grid = grid
      
      self.cols = {}
      for n in range(len(grid[0])):
        col = []
        for row in grid:
          col.append(row[n])
        self.cols[n] = col
      
      self.rows = {}
      for n in range(len(grid)):
        self.rows[n] = grid[n]
    
    def rotate(self, deg):
      
      if deg == 90:
        new_rows = []
        for n in sorted(list(self.cols.keys())):
          new_rows.append(list(reversed(self.cols[n])))
      elif deg == 180:
        new_rows = list(reversed(self.grid))
      elif deg == 270:
        new_rows = []
        for n in reversed(sorted(list(self.cols.keys()))):
          new_rows.append(self.cols[n])
      elif deg == 360:
        new_rows = self.grid
      else:
        return 'Incorrect Angle: {}'.format(deg)
      
      return new_rows
  
  grid = Grid(mat)
  
  return grid.rotate(90)


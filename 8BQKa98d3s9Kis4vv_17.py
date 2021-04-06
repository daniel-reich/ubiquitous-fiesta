
def final(r, c, i):
  def seperate_increment(inc):
    inc = list(inc)
​
    index = None
    row_or_col = None
​
    for item in inc:
      try:
        i = int(item)
        if index != None:
          index += str(i)
        else:
          index = str(i)
      except ValueError:
        row_or_col = item
    
    return [int(index), row_or_col]
  class Grid:
    class Space:
​
      def __init__(self, row, col, val=0):
        self.r = row
        self.c = col
        self.v = val
    
    def __init__(self, rows, cols):
      self.r = rows
      self.c = cols
    
      self.rows = {}
​
      for n in range(rows):
        row = []
        for c in range(cols):
          row.append(Grid.Space(n, c))
        self.rows[n] = row
      
      self.cols = {}
​
      for n in range(cols):
        col = []
        for r in self.rows.keys():
          for item in self.rows[r]:
            if item.c == n:
              col.append(item)
        self.cols[n] = col
​
    def increment_row(self, row):
      for item in self.rows[row]:
        item.v += 1
      return True
    
    def increment_col(self, col):
      for item in self.cols[col]:
        item.v += 1
      return True
    
    def display(self):
      grid = []
​
      for n in sorted(list(self.rows.keys())):
        row = self.rows[n]
        ordered_row = []
        nxt = 0
        found = False
        c = 0
​
        while found == False and c < 1000:
          c += 1
          f = True
          for item in row:
            if item.c == nxt:
              ordered_row.append(item.v)
              nxt += 1
              f = False
              break
          found = f
        
        grid.append(ordered_row)
      
      return grid
  
  grid = Grid(r, c)
​
  for increment in i:
    increment = seperate_increment(increment)
​
    ident = increment[0]
​
    if increment[1] == 'r':
      grid.increment_row(ident)
    elif increment[1] == 'c':
      grid.increment_col(ident)
    else:
      return 'Error: Incorrect increment value: {}'.format(increment)
  
  return grid.display()


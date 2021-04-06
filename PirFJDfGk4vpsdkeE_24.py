
def help_bobby(size):
​
  class Grid:
    class Space:
​
      def __init__(self, val, row, col):
        self.v = val
        self.r = row
        self.c = col
      
      def val_change(self, newval):
        self.v = newval
        return True
​
    def __init__(self, size):
​
      self.s = size
​
      self.spaces = {}
​
      for num in range(1, size + 1):
        for n in range(1, size + 1):
          self.spaces['{},{}'.format(num,n)] = Grid.Space(0, num, n)
    def turn_on_diags(self):
      lr = []
      rl = []
​
      n = 1
​
      for num in range(1, self.s+1):
        lr.append('{},{}'.format(num, n))
        rl.append('{},{}'.format(num, (self.s + 1) - n))
        n += 1
      
      for space in lr:
        self.spaces[space].val_change(1)
      
      for space in rl:
        self.spaces[space].val_change(1)
      
      return True
    def display(self):
​
      to_display = []
​
      for num in range(1, self.s + 1):
        row = []
        for n in range(1, self.s + 1):
          row.append(self.spaces['{},{}'.format(num, n)].v)
        to_display.append(row)
      
      return to_display
  
  grid = Grid(size)
  grid.turn_on_diags()
​
  return grid.display()



def is_magic(square):
  
  class Square:
    
    def __init__(self, square):
      self.s = square
    
    def magic_square(self):
      try:
        constant_goal = sum(self.s[0])
      except IndexError:
        return True
      #print(constant_goal)
        
      for r in self.s:
        if sum(r) != constant_goal:
          return False
      #print(18)
      cols = []
      
      for c in range(len(self.s)):
        col = [r[c] for r in self.s]
        cols.append(col)
      #print(20, cols)
      for col in cols:
        if sum(col) != constant_goal:
          #print(col, sum(col))
          return False
      #print(24)
      diag1 = [self.s[n][n] for n in range(len(self.s))]
      diag2 = []
      #print(32)
      n = 0
      
      while n != len(self.s):
        row = self.s[n]
      # print(row)
        n += 1
        diag2.append(row[-n])
        
      #print(26, diag2)
      diags = [diag1, diag2]
      for diag in diags:
        if sum(diag) != constant_goal:
      #   print(diag, diags, sum(diag))
          return False
      
      for num in range(1,len(self.s)**2 + 1):
        if num not in [i for r in self.s for i in r]:
          return False
       
      return True
      
      
  s = Square(square)
  
  return s.magic_square()


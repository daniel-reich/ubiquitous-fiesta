
class ones_threes_nines:
  def __init__ (self,n):
    self.threes = 0
    self.nines = 0
    self.ones = n
    if n % 3 == 0:
      self.threes = int(n/3)
    else:
      self.threes = int(n/3)
    if n % 9 == 0:
      self.nines = int(n/9)
    else:
      self.nines = int(n/9)


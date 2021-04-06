
class ones_threes_nines:
  
  def __init__(self, val):
    self.val = val
    
    if val >= 9:
      self.nines = int(val/9)
      val = val%9
    else:
      self.nines = 0
    
    if val >= 3:
      self.threes = int(val/3)
      val = val%3
    else:
      self.threes = 0
    
    self.ones = int(val)
    
    self.answer = 'nines:{}, threes:{}, ones:{}'.format(self.nines, self.threes, self.ones)



class ones_threes_nines:
  def __init__(self,val):
    self.val = val
    self.nines = int(self.val/9)
    self.threes = int((self.val-9*self.nines)/3)
    self.ones = self.val-9*self.nines-3*self.threes
    self.answer = ', '.join(['nines:'+str(self.nines),'threes:'+str(self.threes),'ones:'+str(self.ones)])


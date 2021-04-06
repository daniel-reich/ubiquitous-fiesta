
class ones_threes_nines:
  def __init__(self,num):
    self.nines = num // 9
    self.threes =  (num % 9) // 3
    self.ones =  (num % 3) // 1
    self.answer = "nines:{}, threes:{}, ones:{}".format(self.nines,self.threes,self.ones)


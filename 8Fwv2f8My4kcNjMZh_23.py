
class ones_threes_nines:
  def __init__(self,num):
    self.nine = num // 9
    self.threes = (num % 9) // 3
    self.ones = num % 9 % 3
    self.answer = "nines:{}, threes:{}, ones:{}".format(self.nine, self.threes, self.ones)


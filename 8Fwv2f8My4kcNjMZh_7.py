
class ones_threes_nines:
  def __init__(self, n):
    self.nines = n // 9
    n -= self.nines * 9
    self.threes = n // 3
    n -= self.threes * 3
    self.ones = n
    self.answer = "nines:{0}, threes:{1}, ones:{2}".format(self.nines, self.threes, self.ones)


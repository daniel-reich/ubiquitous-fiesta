
class ones_threes_nines:
  def __init__(self, n):
    self.nines = n // 9
    self.threes = (n - self.nines * 9) // 3
    self.ones = (n - self.nines * 9 - self.threes * 3)
    self.answer = 'nines:{}, threes:{}, ones:{}'.format(self.nines, self.threes, self.ones)


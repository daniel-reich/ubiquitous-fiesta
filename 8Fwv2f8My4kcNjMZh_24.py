
class ones_threes_nines:
  def __init__(self, number):
    self.number = number
    nines = self.number // 9
    nines_rem = self.number % 9
    threes = nines_rem // 3
    ones = nines_rem % 3
    self.answer = "nines:{}, threes:{}, ones:{}".format(nines, threes, ones)


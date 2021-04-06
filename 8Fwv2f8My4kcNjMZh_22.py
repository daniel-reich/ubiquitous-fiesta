
class ones_threes_nines:
  def __init__(self, num):
    nines = num // 9
    num = (num % 9)
    threes = num // 3
    num = (num % 3)
    ones = num
    self.answer = "nines:{}, threes:{}, ones:{}".format(nines, threes, ones)


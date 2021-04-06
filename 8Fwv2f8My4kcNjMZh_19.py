
class ones_threes_nines:
  def __init__(self, x):
    n = x // 9
    t = (x - 9*n) // 3
    o = x - 9*n - 3*t
    self.answer = 'nines:{}, threes:{}, ones:{}'.format(n, t, o)


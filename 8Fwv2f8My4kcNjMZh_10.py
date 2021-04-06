
class ones_threes_nines:
  def __init__(self,n):
    nines=n//9
    threes=(n-nines*9)//3
    ones=n-(nines*9+threes*3)
    self.answer='nines:{}, threes:{}, ones:{}'.format(nines,threes,ones)


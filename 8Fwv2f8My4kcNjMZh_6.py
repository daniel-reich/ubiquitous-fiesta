
class ones_threes_nines:
  def __init__(self,x):
    if x>=9:nines,x=divmod(x,9)
    else:nines=0
    if x>=3:threes,ones=divmod(x,3)
    else:threes,ones=0,x
    self.answer='nines:{}, threes:{}, ones:{}'.format(nines,threes,ones)


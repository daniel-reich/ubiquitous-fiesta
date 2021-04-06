
class ones_threes_nines:
  def __init__(self,n):
    self.answer = 'nines:{}, threes:{}, ones:{}'.format(n//9,(n%9)//3,n%3)


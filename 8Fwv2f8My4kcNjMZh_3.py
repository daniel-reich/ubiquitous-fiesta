
class ones_threes_nines:
  def __init__(self, n):
    self.answer="nines:"+str(n//9)+", threes:"+str(n%9//3)+", ones:"+str(n%9%3)


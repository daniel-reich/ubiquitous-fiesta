
class ones_threes_nines:
  def __init__(self,num):
    nines = num//9
    num -= nines*9
    threes = num//3
    num -= threes*3
    self.answer = "nines:"+str(nines)+", threes:"+str(threes)+", ones:"+str(num)


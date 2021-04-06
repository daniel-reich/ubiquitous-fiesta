
class Number(float):
  def __init__(self, num):
    self.numeral = num
    
  def __truediv__(self, other):
    if other == Number(0):
      return 'ZeroDivisionError'
    return Number(self.numeral / other.numeral)
    
  def __repr__(self):
    return 'Number({})'.format(self.numeral)


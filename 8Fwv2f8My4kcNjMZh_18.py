
class ones_threes_nines:
  def __init__(self, num):
    self.num = num
    
  @property
  def answer(self):
    times_nine, remainder = self._calculate_result_and_remainder(self.num, 9)
    times_three, remainder = self._calculate_result_and_remainder(remainder, 3)
    
    return 'nines:{}, threes:{}, ones:{}'.format(
      times_nine, 
      times_three, 
      remainder
    )
  
  def _calculate_result_and_remainder(self, divisor, dividend):
    return divisor // dividend, divisor % dividend


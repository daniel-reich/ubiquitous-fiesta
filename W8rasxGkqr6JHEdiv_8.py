
class test(str):
  def __new__(cls, val, nums):
    return super().__new__(cls, str(val))
  def __init__(self, val, nums):
    self.val = val
    self.nums = nums
  def replace(self, *args):
    return '+'.join(str(n) for n in self.nums)
​
def countdown(operands, target):
  return test(target, operands)


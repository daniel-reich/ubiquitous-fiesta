
def simple_check(*nums):
  
  x, y, = sorted(nums)
  result = 0
  
  while x:
    if not y % x:
      result += 1
    x -= 1
    y -= 1
  
  return result


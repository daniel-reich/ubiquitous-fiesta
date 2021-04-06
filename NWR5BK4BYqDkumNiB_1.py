
from functools import reduce
def digital_division(n):
  nums = [int(i) for i in str(n)]
  add = sum(nums); mult = reduce(lambda x,y: x*y, nums)
  
  count = 0
  if all(not n%i for i in nums if i != 0): count += 1
  if not n%add: count += 1
  if mult != 0 and not n%mult: count += 1
  
  return 'Perfect' if count == 3 else 'Indivisible' if count == 0 else count


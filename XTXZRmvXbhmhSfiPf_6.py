
def single_number(nums):
  ops = set()
  disc = set()
  
  for num in nums:
    if num not in disc:
      if num in ops:
        ops.remove(num)
        disc.add(num)
      else:
        ops.add(num)
  
  return ops.pop()


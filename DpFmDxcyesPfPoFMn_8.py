
def isbn13(txt):
  l1 = [10,9,8,7,6,5,4,3,2,1]
  l2 = [1, 3, 1,  3,  1,  3,  1,  3,  1,  3,  1,  3, 1]
  chrs = list(txt)
  if 'X' in chrs:
    chrs.remove('X')
  nums = [int(n) for n in chrs]
  if txt[-1] == 'X':
    nums.append(10)
  if len(nums) == 10:
    s = 0
    for i in range(len(nums)):
      s += nums[i]*l1[i]
  elif len(nums) == 13:
    s = 0
    for i in range(len(nums)):
      s += nums[i]*l2[i]
    if s%10 == 0:
      return 'Valid'
    else:
      return 'Invalid'
  if s%11 != 0:
    return 'Invalid'
  nums = [9,7,8] + nums[:-1]
  s3 = 0
  for i in range(len(nums)):
    s3 += nums[i]*l2[i]
  n1 = 10- s3%10
  nums.append(n1)
  ns = [str(m) for m in nums]
  st = ''.join(ns)
  return st


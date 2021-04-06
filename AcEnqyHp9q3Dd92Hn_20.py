
def multiply_nums(nums):
  r =1
  for x in range(len(nums.split(','))):
    r = r*int(nums.split(',')[x])
  return r


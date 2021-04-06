
def sum_of_cubes(nums):
  sum = 0 
  for x in nums:
    sum += x**3
  if nums == []: 
    return 0 
  else: 
    return sum


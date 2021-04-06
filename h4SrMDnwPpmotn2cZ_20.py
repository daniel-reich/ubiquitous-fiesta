
def sum_of_cubes(nums):
  _sum = 0;
  x = len(nums);
  y = 0;
  while y < x:
    _sum += nums[y] ** 3;
    y += 1
  return _sum



def divisible_by_left(n):
  nums = list(map(int, str(n)))
  return [False] + [
    False if not i else (j / i).is_integer() 
    for i, j in zip(nums, nums[1:])
  ]


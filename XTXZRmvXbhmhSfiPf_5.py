
def single_number(nums):
  for x in set(nums):
    if nums.count(x) == 1:
      return x


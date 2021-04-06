
def single_number(nums):
  for n in set(nums):
    if nums.count(n) == 1:
      return n


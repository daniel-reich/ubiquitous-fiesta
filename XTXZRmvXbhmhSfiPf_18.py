
def single_number(nums):
  for e in set(nums):
    if nums.count(e) == 1:
      return e
    else:
      continue


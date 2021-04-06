
def prime(x):
  nums = [2, 3, 5, 7]
  for count, item in enumerate(nums):
    if x%item == 0:
      if x != item:
        return False
  return True


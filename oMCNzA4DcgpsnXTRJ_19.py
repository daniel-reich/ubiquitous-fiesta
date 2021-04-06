
def missing_num(lst):
  nums = list(range(1, 11))
  for num in nums:
    if num not in lst:
      return num



def missing_num(lst):
  nums = [1,2,3,4,5,6,7,8,9,10]
  for num in nums:
    if num not in lst:
      return num


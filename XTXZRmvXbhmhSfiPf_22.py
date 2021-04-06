
def single_number(nums):
  for i in set(nums):
    if nums.count(i)==1:
      return i


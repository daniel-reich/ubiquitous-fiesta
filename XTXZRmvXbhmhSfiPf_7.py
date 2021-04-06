
def single_number(nums):
  return list(filter(lambda x: nums.count(x) == 1,list(set(nums))))[0]


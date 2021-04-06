
def single_number(nums):
  return [i for i in set(nums) if nums.count(i) == 1][0]


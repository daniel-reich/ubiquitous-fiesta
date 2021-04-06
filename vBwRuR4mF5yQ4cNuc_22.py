
def count_missing_nums(lst):
  nums = [int(i) for i in lst if i.isnumeric()]
  return max(nums) - min(nums) + 1 - len(nums)


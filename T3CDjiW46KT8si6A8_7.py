
def product(lst):
  sorted_nums = sorted(set(lst), reverse=True)
  if len(sorted_nums) == 1:
    return sorted_nums[0]**2
  return sorted_nums[0] * sorted_nums[1]



def max_total(nums):
  sorted_nums = sorted(nums)
  return sum(sorted_nums[-5:])


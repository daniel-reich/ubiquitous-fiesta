
def ends_add_to_10(nums):
  nums = map(str,  map(abs, nums))
  return sum([int(i[0]) + int(i[-1]) == 10 for i in nums])


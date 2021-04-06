
def ends_add_to_10(nums):
  if not nums:
    return 0
  nums = map(abs, nums)
  return sum(1 for i in nums if int(str(i)[0]) + int(str(i)[-1]) == 10)


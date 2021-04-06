
def ends_add_to_10(nums):
  nums = [str(abs(num)) for num in nums]
  return sum(int(x[0]) + int(x[-1]) == 10 for x in nums)


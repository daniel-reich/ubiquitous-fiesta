
def break_point(num):
  nums = [int(num) for num in str(num)]
  for i in range(1, len(nums)):
    if sum(nums[:i]) == sum(nums[i:]):
      return True
  return False


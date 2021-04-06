
def find_all_digits(nums):
  ud = set()
  for i in range(len(nums)):
    ud |= set(str(nums[i]))
    if len(ud) == 10: return nums[i]
  return "Missing digits!"


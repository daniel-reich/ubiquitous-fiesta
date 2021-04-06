
def ends_add_to_10(nums):
  return sum([1 for i in nums if int(str(i).strip("-")[0]) + int(str(i)[-1]) == 10])


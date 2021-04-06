
import math
def ends_add_to_10(nums):
  for i in range(0,len(nums)):
    if nums[i] < 0:
      nums[i] *= -1
  tally = 0
  brr = map(str,nums)
  for x in brr:
    if int(list(x)[0]) + int(list(x)[-1]) == 10:
      tally += 1
  return tally


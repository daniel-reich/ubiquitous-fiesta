
def ends_add_to_10(nums):
  res = 0
  for n in nums:
    if int(str(abs(n))[0]) + int(str(abs(n))[-1]) == 10:
      res += 1
  return res


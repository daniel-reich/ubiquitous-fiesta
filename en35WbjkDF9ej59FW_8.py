
def ends_add_to_10(nums):
  x = 0
  for i in nums:
    i = abs(i)
    i = str(i)
    if int(i[-1]) + int(i[0]) == 10:
      x += 1
  return x


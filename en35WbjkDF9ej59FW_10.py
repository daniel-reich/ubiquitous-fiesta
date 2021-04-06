
def ends_add_to_10(nums):
  count = 0
  for i in nums:
    k = str(i)
    if '-' in k:
      k = k[1:]
    if int(k[0]) + int(k[-1])==10:
      count += 1
  return count



def twins(lst):
  left = 0
  lSum = lst[0]
  right = len(lst) - 1
  rSum = lst[-1]
  while right - left > 0:
    if lSum > rSum:
      right -= 1
      rSum += lst[right]
    elif rSum > lSum:
      left += 1
      lSum += lst[left]
    else:
      right -= 1
      rSum += lst[right]
      left += 1
      lSum += lst[left]
  return left


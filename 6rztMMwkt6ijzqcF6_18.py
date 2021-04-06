
def is_repeated(strn):
  nums = [24, 12, 8, 6, 4, 3, 2]
  for i in nums:
    if strn == strn[0:24 // i] * i:
      return i
  return False


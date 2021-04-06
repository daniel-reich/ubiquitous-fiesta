
def is_prob_matrix(arr):
  if len(arr[0]) != len(arr):
    return False
  for i in arr:
    res = 0
    for y in i:
      if y > 1 or y < 0:
        return False
      res += y
    if res > 1:
      return False
  return True


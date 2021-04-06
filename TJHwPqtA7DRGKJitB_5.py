
def is_prob_matrix(arr):
  if len(arr) != len(arr[0]): return False
  for row in arr:
    if sum(row) != 1: return False
    for num in row:
      if num < 0 or num > 1: return False
  return True


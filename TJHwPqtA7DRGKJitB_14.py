
def is_prob_matrix(arr):
  for y, row in enumerate(arr):
    if len(row) != len(arr): return False
    if sum(row) != 1: return False
    for num in row:
      if not 0 <= num <= 1: return False
  return True


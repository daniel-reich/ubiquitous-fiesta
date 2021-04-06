
def is_prob_matrix(arr):
  if all (len (row) == len (arr) for row in arr) !=True:
    return False
  for row in arr:
    for number in row:
      if number <0:
        return False
    if sum(row) != 1:
      return False
  return True


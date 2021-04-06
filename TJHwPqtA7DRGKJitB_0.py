
def is_prob_matrix(arr):
  if all(len(i)!=len(arr) for i in arr):
      return False
  for i in arr:
    if sum(i)!=1:
      return False
    for j in i:
      if j>1 or j<0:
        return False
  return True


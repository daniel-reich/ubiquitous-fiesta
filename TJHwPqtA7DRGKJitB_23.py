
def is_prob_matrix(arr):
  nrow,ncol = len(arr),len(arr[0])
  if nrow!=ncol:
    return False
  for row in arr:
    s=0
    for x in row:
      if x<0 or x>1:
        return False
      s+=x
    if s!=1:
      return False
  return True


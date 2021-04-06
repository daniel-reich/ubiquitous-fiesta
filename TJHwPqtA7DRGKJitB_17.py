
def is_prob_matrix(arr):
  if(len(arr)!=len(arr[0])):
    return False
  for i in arr:
    for j in i:
      if(j>1 or j<0):
        return False
    if(sum(i)!=1):
      return False
  return True


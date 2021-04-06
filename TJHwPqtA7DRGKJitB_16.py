
def is_prob_matrix(arr):
  if len(arr) != len(arr[0]):
    print ("Not a square matrix.")
    return False
  for i in arr:
    for j in i:
      if j > 1 or j < 0:
        print("Entries are not probabilities.")
        return False
    if sum(i) != 1:
      print("Rows do not add to 1.")
      return False
      
    return True


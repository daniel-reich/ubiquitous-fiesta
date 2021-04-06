
def is_prob_matrix(arr):
  return (len(arr) == len(arr[0]) and
       all(sum(row)==1 for row in arr) and
       all(0<=i<=1 for row in arr for i in row))


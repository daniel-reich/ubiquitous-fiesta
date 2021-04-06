
def num_to_dict(lst):
  A=[{} for _ in range(len(lst))]
  for i in range(len(A)):
    A[i][str(lst[i])]=chr(lst[i])
  return A


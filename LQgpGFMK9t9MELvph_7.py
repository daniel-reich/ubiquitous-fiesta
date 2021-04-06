
def get_diagonals(lst):
  A=[[],[]]
  for i in range(len(lst)):
    for j in range(len(lst)):
      if i==j:
        A[0].append(lst[i][j])
      if i+j+1==len(lst):
        A[1].append(lst[i][j])
  return A



def transpose_matrix(lst):
  lst1 = [[0] * len(lst) for i in range(len(lst[0]))]
  for i in range(len(lst)):
    for j in range(len(lst[0])):
      lst1[j][i] = lst[i][j]
  return lst1


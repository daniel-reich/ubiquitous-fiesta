
def subtract_matrix(lst1, lst2):
  return [[float(lst1[i][j])-float(lst2[i][j]) for j in range(len(lst1))] \
  for i in range(len(lst2))]


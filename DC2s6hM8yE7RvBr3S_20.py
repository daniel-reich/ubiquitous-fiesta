
def subtract_matrix(lst1, lst2):
  return [[float(lst1[j][i]) - float(lst2[j][i]) for i in range(len(lst1[0]))] for j in range(len(lst1))]



def subtract_matrix(lst1, lst2):
  return [[float(x[i]) - float(y[i]) for i in range(len(lst1[0]))] for x, y in zip(lst1, lst2)]


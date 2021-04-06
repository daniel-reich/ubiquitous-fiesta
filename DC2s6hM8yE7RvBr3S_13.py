
def subtract_matrix(lst1, lst2):
  matrix = []
  for i in range(len(lst1)):
    matrix.append([])
    for x,y in zip(lst1[i] , lst2[i]):
      matrix[i].append(eval(str(x) + ' - ' + str(y)))
  return matrix


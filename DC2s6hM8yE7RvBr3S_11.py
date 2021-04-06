
def subtract_matrix(lst1, lst2):
  return [[float(a[i])-float(b[i]) for i in range(len(a))] for a,b in zip(lst1,lst2)]


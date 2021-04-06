
def subtract_matrix(lst1, lst2):
  try:
    for i in range(0,len(lst1)):
      for j in range(0,len(lst1[0])):
        lst2[i][j] = lst1[i][j] - lst2[i][j]
    return lst2
  except TypeError:
    lst1 = [[float(ele) for ele in sub] for sub in lst1]
    lst2 = [[float(ele) for ele in sub] for sub in lst2]
    for i in range(0,len(lst1)):
      for j in range(0,len(lst1[0])):
        lst2[i][j] = lst1[i][j] - lst2[i][j]
    return lst2


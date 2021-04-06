
def subtract_matrix(lst1, lst2):
  res=[[0 for j in range(len(lst1[0]))] for i in range(len(lst1))]
  for i in range(len(lst1)):
    for j in range(len(lst1[0])):
      if type(lst1[i][j])!=str and type(lst2[i][j])!=str:
        res[i][j]=lst1[i][j]-lst2[i][j]
      else:
        res[i][j]=int(lst1[i][j])-int(lst2[i][j])
  return res


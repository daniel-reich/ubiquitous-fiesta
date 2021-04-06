
def is_shifted(lst1, lst2):
  tmp=[]
  x = list(zip(lst1,lst2))
  for i in range(len(x)):
    tmp.append(x[i][1] - x[i][0])
  if len(set(tmp))==1:
    return True
  else:
    return False
def is_multiplied(lst1, lst2):
  tmp = []
  x = list( zip( lst1, lst2 ) )
  for i in range(len(x)):
    if x[i][0] != 0:
      tmp.append(x[i][1] / x[i][0])
  if len(set(tmp)) == 1:
    return True
  else:
    return False


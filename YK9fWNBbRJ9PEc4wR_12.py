
def tuck_in(lst1, lst2):
  result=[]
  result.append(lst1[0])
  for i in lst2:
    result.append(i)
  result.append(lst1[1])
  return result


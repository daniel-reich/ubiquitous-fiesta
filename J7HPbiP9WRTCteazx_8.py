
def n_differences(lst):
  lst2=[]
  if len(lst)>2:
    for i in range(1,len(lst)):
      lst2.append(lst[i]-lst[i-1])
  else:
    return lst[1]-lst[0]
  if len(lst2)>2:
    return n_differences(lst2)
  else:
    return lst2[1]-lst2[0]


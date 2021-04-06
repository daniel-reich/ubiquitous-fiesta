
def ranged_reversal(lst, start, finish):
  lst2=[]
  for i in range(start,finish+1):
    lst2.append(lst[i])
  lst2.reverse()
  if start>0:
    return(lst[0:start]+lst2+lst[finish+1::])
  else:
    return(lst2+lst[finish+1::])


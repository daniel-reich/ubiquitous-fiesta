
def covered_integers(lst):
  k=[]
  for i in lst:
    for j in range(i[0],i[1]+1):
      if(j not in k):
        k.append(j)
  return len(k)


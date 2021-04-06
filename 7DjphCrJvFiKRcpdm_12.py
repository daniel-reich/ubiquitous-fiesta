
def covered_integers(lst):
  x = []
  for i in lst:
    for j in range(i[0],i[1]+1):
      if j not in x:
        x.append(j)
  return len(x)


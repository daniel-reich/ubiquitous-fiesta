
def row_sum(n):
  lst=[1]
  for x in range(n-1):
    lst.append(lst[-1]+lst.index(lst[-1])+1)
  return sum(range(lst[-1],lst[-1]+n))


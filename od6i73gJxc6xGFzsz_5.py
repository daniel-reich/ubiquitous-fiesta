
def is_slidey(n):
  s=str(n)
  L=[int(x) for x in s]
  return all(abs(L[i]-L[i+1])==1 for i in range(len(L)-1))


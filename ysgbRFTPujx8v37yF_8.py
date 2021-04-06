
def row_sum(n):
  a=int((n*(n+1))/2)
  return a+sum([i for i in range(a-1,a-n,-1)])


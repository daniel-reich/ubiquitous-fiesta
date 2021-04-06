
def split(n):
  return max([round((n/i) ** i,1) for i in range(1,n+1)])


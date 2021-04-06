
def multTable(n):
  x=range(1,n+1)
  return [[[1]],[[i*j for i in x]for j in x]][n>1]


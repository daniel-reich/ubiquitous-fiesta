
def snakefill(n):
  a=1;summ=0;count=0
  while summ<n**2:
    summ=summ+a
    a=a*2
    count=count+1
  return count-1


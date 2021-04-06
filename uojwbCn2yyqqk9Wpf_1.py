
def is_untouchable(n):
  if n>1:
    a=[x for x in range(2,n*n+1)if(1+sum(sum({y,x//y})for y in range(2,int(x**0.5)+1)if not x%y))==n]
    return(1,a)[len(a)>0]
  return'Invalid Input'



def is_exact(n,x=2,i=0):
  if i==0:
    i=n
  if n==1:
    return [i,x-1]
  if n<1:
    return 'Not exact!'
  return is_exact(n/x,x+1,i)


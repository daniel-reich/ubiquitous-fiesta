
def is_happy(n,s=''):
  if n==1:return 1
  if'4'in s:return 0
  n=sum(int(x)**2for x in str(n))
  return is_happy(n,str(n))


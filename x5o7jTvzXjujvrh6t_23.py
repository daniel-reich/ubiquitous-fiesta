
def i_sqrt(n):
  if n<0:
    return 'invalid'
  count=0
  while n>=2:
    n=n**.5
    count+=1
  return count


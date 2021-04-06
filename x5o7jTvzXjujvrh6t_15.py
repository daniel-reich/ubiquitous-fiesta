
def i_sqrt(n):
  count=0
  if n<0:
    return 'invalid'
  while n>=2:
    n=n**0.5
    count+=1
  return count



def is_powerful(n):
  for i in prime_factor(n):
    if n%i**2:
      return False
  return True
  
def prime_factor(n):
  res=[]
  i=2
  while n//2>=i:
    if not n%i:
      res += [i]
    i+=1
  if res == []:
    return True
  return [x for x in res if prime_factor(x)==True]


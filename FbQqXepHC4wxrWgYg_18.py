
def prime_divisors(n):
  
  
  l = []
  while n%2==0:
    n//=2
    l.append(2)
  for i in range(3,int(n**.5)+1,2):
    while n%i==0:
      n//=i
      l.append(i)
  if n>=2:
    l.append(n)
  return sorted(list(set(l)))


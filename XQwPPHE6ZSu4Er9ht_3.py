
def is_economical(n):
  f, l = fact(n), len(str(n))
  m=len(''.join(str(i)+str(f.count(i))*(f.count(i)>1)for i in set(f)))
  return m<l and"Frugal"or m>l and"Wasteful"or"Equidigital" 
  
def fact(n):
  i, f = 2, []
  while n>1:
    if n%i: i+=1
    else: f+=[i]; n//=i
  return f


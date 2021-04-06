
def simplify_sqrt(n):
  m=sq_fact(n)
  return (m,n//m**2)
​
def sq_fact(n):
  for i in range(2,int(n**0.5)+1):
    if not n%i**2: return i*sq_fact(n//i**2)
  return 1


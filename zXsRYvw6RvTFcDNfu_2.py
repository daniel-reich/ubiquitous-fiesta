
def ruth_aaron(n):
  a = (p_fac(n-1))
  b = (p_fac(n))
  c = (p_fac(n+1))
  p=0
  
  if sum(a) == sum(b) or sum(b) == sum(c):
    p+=2
  if sum(set(a)) == sum(set(b)) or sum(set(b)) == sum(set(c)):
    p+=1
  return False if p==0 else ['Aaron', p] if sum(a)==sum(b) or sum(set(a))==sum(set(b)) else ['Ruth', p]
​
​
def p_fac(n):
  f = []
  i = 2
  while n>1:
    if not n%i:
      f.append(i)
      n/=i
    else:
      i+=1
  return f


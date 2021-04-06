
def primeFacts(n):
  res = []
  while not n&1:
    res.append(2)
    n //= 2
  i = 3
  while i*i <= n:
    while not n%i:
      res.append(i)
      n //= i
    i += 2
  if n > 2: 
    res.append(n)
  return res
​
def r_a_calc(x,y):
  ans = 0
  if sum(x) == sum(y) and sum(set(x)) == sum(set(y)):
    ans = 3
  elif sum(x) == sum(y):
    ans = 2
  elif sum(set(x)) == sum(set(y)):
    ans = 1
  return ans
  
def ruth_aaron(n):
  low,mid,high = primeFacts(n-1), primeFacts(n), primeFacts(n+1)
  aar,rut = r_a_calc(low,mid), r_a_calc(mid,high)
  return ['Aaron',aar] if aar else ['Ruth',rut] if rut else False


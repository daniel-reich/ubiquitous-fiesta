
def esthetic(num):
  res = []
  for b in range(2,11):
    n = to_base(b,num)
    if all(abs(int(n[i])-int(n[i+1]))==1 for i in range(len(n)-1)):
      res.append(b)
  return res or 'Anti-Esthetic'
​
def to_base(b,n,s=''):
  while n:
    s = str(n % b) + s
    n //= b
  return s


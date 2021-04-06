
def gcd(lst):
  b=[]
  for i in range(1,min(lst)+1):
    for a in lst:
      if a%i==0:
        b.append(i)
  c=[]
  for j in b:
    if b.count(j)==len(lst):
      c.append(j)
  return max(c)


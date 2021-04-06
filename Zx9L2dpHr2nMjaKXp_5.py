
def int_to_vlq(n):
  length = 1
  while 128**length<=n:
    length+=1
  vlq = []
  for base in reversed(range(length)):
    if base==0:
      vlq.append(n)
    else:
      bit,n = divmod(n,128**base)
      vlq.append(128+bit)
  return vlq
​
def vlq_to_int(lst):
  res = 0
  for i in range(len(lst)):
    base = len(lst)-i-1
    if base==0:
      res+=lst[i]
    else:
      res+=(lst[i]-128)*(128**base)
  return res


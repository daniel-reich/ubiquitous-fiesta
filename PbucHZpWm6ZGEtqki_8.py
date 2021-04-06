
def sliding_sum(lst, n, k):
  l=[]
  for i in range(0,len(lst)):
    s=lst[i:i+n]
    if sum(s)==k:
      l.append(s)
  return l


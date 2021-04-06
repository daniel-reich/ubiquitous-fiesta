
def transform_matrix(lst):
  l=[]
  ml=[]
  sum=0
  d=0
  for s in lst:
    if d>0:
      ml.append(l)
      l=[]
    for e in range(len(s)):
      count=0
      while(True):
        if count>len(lst)-1:
          break
        sum=sum+lst[count][e]
        count+=1
      for f in s:
        sum=sum+f
      if s[e]==1:
        sum=sum-2
      l.append(sum)
      sum=0
      d+=1
  ml.append(l)
  return ml


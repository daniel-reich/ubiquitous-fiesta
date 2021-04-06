
def three_sum(lst):
  if len(lst)<3: return []
  l=[]
  for i in range(len(lst)-2):
    for j in range(i+1,len(lst)-1):
      for k in range(j+1,len(lst)):
        if lst[i]+lst[j]+lst[k]==0 and [lst[i],lst[j],lst[k]] not in l: l.append([lst[i],lst[j],lst[k]])
  return l


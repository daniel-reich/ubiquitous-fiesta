
def majority_vote(lst):
  if not lst:
    return None
  d={}
  for a in lst:
    if a in d:
      d[a]+=1
    else:
      d[a]=1
  s = sorted(d, key=d.__getitem__, reverse=True)[0]
  if d[s]>len(lst)/2:
    return s
  return None



def majority_vote(lst):
  a = {}
  for x in lst:
    if x not in a:
      a[x] = 1
    else:
      a[x]+=1
  for y in a:
    if a[y] > (len(lst)/2):
      return y
  return None


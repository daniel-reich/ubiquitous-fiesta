
def big_sub(lst):
  lst=lst[::-1]
  best, cur=0,0
  curi, s, e=0,0,0
  for i, x in enumerate(lst):
    if cur+x>0:
      cur+=x
    else:
      cur, curi=0, i+1
    if cur>best:
      s,e,best=curi, i+1,cur
  return [best, len(lst)-e, len(lst)-s-1]


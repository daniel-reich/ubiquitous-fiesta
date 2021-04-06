
def max_sum_pair(lst):
  mx = 0
  for a in range(len(lst)):
    for b in range(a,len(lst)+1):
      for c in range(b,len(lst)+1):
        for d in range(c,len(lst)+1):
          mx = max(sum(lst[a:b])+sum(lst[c:d]),mx)
  return mx


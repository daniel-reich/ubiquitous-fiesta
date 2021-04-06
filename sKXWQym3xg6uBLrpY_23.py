
def iqr(lst):
  slst = sorted(lst)
  med = median(lst)
  if(len(lst)%2 == 1):
    slst.remove(med)
  q3l = slst[int(len(lst)/2):]
  q1l = slst[:int(len(lst)/2)]
  return(median(q3l) - median(q1l))
    
def median(lst):
  slst = sorted(lst)
  mid = int(len(lst)/2)
  if(len(lst) % 2 == 0):
    return(slst[mid]/2 + slst[mid - 1]/2)
  else:
    return(slst[int(mid+0.5)])


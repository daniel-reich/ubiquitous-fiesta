
def median(lst):
  a = sorted(lst)
  if len(lst)%2 > 0:
    return a[len(lst)//2]
  else:
    return (a[int(len(lst)/2)] + a[int((len(lst)/2)-1)])/2


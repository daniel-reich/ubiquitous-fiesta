
def progress_days(r):
  a=[r[i+1]-r[i] for i in range(len(r)-1)]
  return sum([1 if a[i]>0 else 0 for i in range(len(a))])


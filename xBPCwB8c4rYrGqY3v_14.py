
def missing(lst):
  gap = (max(lst)-min(lst))/len(lst)
  for i in range(1,len(lst)):
    if lst[i]!=lst[i-1]+gap:
      return lst[i-1]+gap


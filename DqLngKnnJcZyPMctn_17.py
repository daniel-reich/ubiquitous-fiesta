
def stock_picker(lst):
  maxdiff=-1
  for i in range(len(lst)):
    for j in range(i,len(lst)):
      diff = lst[j]-lst[i]
      if diff>maxdiff:
        maxdiff=diff
  return maxdiff if maxdiff!=0 else -1


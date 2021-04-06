
def leader(lst):
  high = max(lst)
  tort = lst.index(high)
  new = lst[tort:len(lst)]
  n = len(new)
  for i in new:
    
    if i == 3 and new.index(i) != (n-1):
      
      inde = new.index(i)
      new.pop(inde)
      break
  return new


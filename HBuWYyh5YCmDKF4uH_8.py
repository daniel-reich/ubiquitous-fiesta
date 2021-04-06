
def almost_sorted(lst):
  if lst== sorted(lst) or lst== sorted(lst)[::-1]: return False
  for x in lst:
    l = [i for i in lst]    
    l.remove(x)     
    if l== sorted(l) or l== sorted(l)[::-1]:
      return True
  return False


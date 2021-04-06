
def consecutive_combo(lst1, lst2):
  l=sorted(lst1+lst2)
  return list(range(min(l),max(l)+1))==l


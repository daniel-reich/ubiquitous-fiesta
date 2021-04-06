
def consecutive_combo(lst1, lst2):
  combo = lst1 + lst2
  combo.sort()
  for n,num  in enumerate(combo):
     if (n != 0 and combo[n] - combo[n-1] != 1):
      return False
  return True


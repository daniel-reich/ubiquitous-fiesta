
def circular_shift(lst1, lst2, n):
 if not n == 0:
  if lst1 == lst2:
   return True 
  else:
   return lst1[:n] == lst2[n:]
​
 elif n == 0:
  return True
  
 else:
  return False


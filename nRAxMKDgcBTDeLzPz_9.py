
def circular_shift(lst1, lst2, n):  
  l  = [lst1[(i - n) % len(lst1)]for i, x in enumerate(lst1)] 
  return l == lst2



def circular_shift(lst1, lst2, n):  
  x =  lst1
  n =abs(n)
  for i in range(len(x)-n):
    x[i], x[i+n] = x[i+n], x[i] 
  return x == lst2


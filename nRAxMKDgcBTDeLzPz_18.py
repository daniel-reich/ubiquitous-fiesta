
def circular_shift(lst1, lst2, n):
  
  if n >= 0:
    for i in range(n):
      temp = lst1[0]
      lst1.pop(0)
      lst1.append(temp)
  else:
    for i in range(n,0,1):
      temp = lst1[-1]
      lst1.pop(-1)
      lst1.insert(0, temp)
​
  return lst1 == lst2


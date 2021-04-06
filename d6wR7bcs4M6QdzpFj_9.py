
def repeat(lst, n):
    lst_copy = lst[:]
    t = 0
    while t < n-1:
      for a in lst_copy:
        lst.append(a)
      t += 1
    return lst
​
def add(lst, x):
  lst.append(x)
  return lst
​
def remove(lst, i, j):
  range_x = lst[i-1:j]
  for i in range_x:
    lst.remove(i)
  return lst
  
def concat(lst, lst2):
  for f in lst2:
    lst.append(f)
  return lst


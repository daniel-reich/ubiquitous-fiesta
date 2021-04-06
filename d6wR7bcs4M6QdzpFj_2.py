
def repeat(lst, n):
  l = lst[:]
  for i in range(n - 1):
    lst.extend(l)
  return lst
​
def add(lst, x):
  lst.append(x)
  return lst
​
def remove(lst, i, j):
  for k in range(i, j + 1):
    del lst[i]
  return lst
​
def concat(lst, lst2):
  lst.extend(lst2)
  return lst


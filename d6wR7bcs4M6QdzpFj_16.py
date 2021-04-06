
def repeat(lst, n):
  add = list(lst)
  for i in range(n - 1):
    lst.extend(add)
  return lst
​
def add(lst, x):
  lst.append(x)
  return lst
​
def remove(lst, i, j):
  for _ in range(j):
    del lst[i]
  return lst
​
def concat(lst, lst2):
  lst.extend(lst2)
  return lst


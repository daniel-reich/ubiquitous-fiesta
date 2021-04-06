
def repeat(lst, n):
  elem = lst[:]
  while n - 1 > 0:
    lst += elem
    n -= 1
  return lst
​
def add(lst, x):
  lst.append(x)
  return lst
​
def remove(lst, i, j):
  del lst[i:j+1]
  return lst
​
def concat(lst, lst2):
  lst += lst2
  return lst


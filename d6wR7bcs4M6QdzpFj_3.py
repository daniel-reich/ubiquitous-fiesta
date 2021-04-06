
def repeat(lst, n):
  k = lst[:]
  for _ in range(n-1):
    lst.extend(k)
  return lst
​
def add(lst, x):
  lst.append(x)
  return lst
​
def remove(lst, i, j):
  k = j - i + 1
  for _ in range(k):
    lst.pop(i)
  return lst
​
​
​
def concat(lst, lst2):
  lst.extend(lst2)
  return lst



def repeat(lst, n):
  lst.__imul__(n)
  return lst
​
​
def add(lst, x):
  lst.append(x)
  return lst
​
​
def remove(lst, i, j):
  for k in range((j-i)+1):
    lst.pop(i-1)
  return lst
​
​
def concat(lst, lst2):
  lst.extend(lst2)
  return lst


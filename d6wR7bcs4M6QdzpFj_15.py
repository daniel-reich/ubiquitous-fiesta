
def repeat(lst, n):
  for i in range(len(lst)*(n-1)):
    lst.append(lst[i])
  return lst
  
​
def add(lst, x):
  lst.append(x)
  return lst
  
​
def remove(lst, i, j):
  del(lst[i:j+1])
  return lst
  
​
def concat(lst, lst2):
  for i in lst2:
    lst.append(i)
  return lst


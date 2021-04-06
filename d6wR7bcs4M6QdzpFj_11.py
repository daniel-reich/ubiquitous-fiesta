
def repeat(l,n):
  l*=n
  return l
​
def add(l,x):
  l+=[x]
  return l
​
def remove(l,i,j):
  [l.pop(i) for _ in range(j-i+1)]
  return l
​
def concat(lst, lst2):
  for i in lst2: lst.append(i)
  return lst


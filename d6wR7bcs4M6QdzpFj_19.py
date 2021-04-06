
def repeat(lst, n):
    lst *= n
    return lst
  
​
def add(lst, x):
    lst += [x]
    return lst
  
​
def remove(lst, i, j):
    for k in range(i, j + 1):
        lst.remove(lst[i])
    return lst
        
​
def concat(lst, lst2):
    lst += lst2
    return lst


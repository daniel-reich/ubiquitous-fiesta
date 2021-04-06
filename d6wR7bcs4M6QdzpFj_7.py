
def repeat(lst, n):
    lst.extend(lst*(n-1))
    return lst
    
def add(lst, x):
   lst.append(x)
   return lst
  
def remove(lst, i, j):
    x = i
    for x in range(j):
        lst.remove(lst[i])
    return lst    
      
def concat(lst, lst2):
   lst.extend(lst2)
   return lst


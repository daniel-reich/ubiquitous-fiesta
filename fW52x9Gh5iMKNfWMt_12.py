
def recaman_index(n):
  lst = [0]
  
  for i in lst:
    if i != n:
      if lst[-1] - len(lst) > 0 and lst[-1] - len(lst) not in lst:
        lst.append(lst[-1] - len(lst))
      else:
        lst.append(lst[-1] + len(lst))
  
  return lst.index(n)



def find_missing(lst):
  len_lst = []
  
  if lst == None or len(lst) == 0:
    return False
  else: 
    for i in lst:
      if  i == None or len(i) == 0:
        return False
      else:
        len_lst.append(len(i))
​
    i = min(len_lst)
    while i in len_lst:
      i += 1
​
    return i


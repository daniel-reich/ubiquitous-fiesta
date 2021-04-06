
def recaman_index(n):
  lst = [0]
  
  while n not in lst:
    last_minus_length = lst[-1] - len(lst)
    last_plus_length = lst[-1] + len(lst)
    
    if last_minus_length > 0 and last_minus_length not in lst:
      lst.append(last_minus_length)
    else:
      lst.append(last_plus_length)
  
  return lst.index(n)


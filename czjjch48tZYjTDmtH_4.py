
def is_shifted(lst1, lst2):
  shift = lst2[0]-lst1[0] 
  for i in range(0, len(lst1)):
      if lst1[i] + shift == lst2[i]:
        continue
      else:
        return False
  return True
​
def is_multiplied(lst1, lst2):
  multi = lst2[0]/lst1[0]
  for i in range(0,len(lst1)):
    if lst1[i]*multi == lst2[i]:
      continue
    else:
      return False
  return True


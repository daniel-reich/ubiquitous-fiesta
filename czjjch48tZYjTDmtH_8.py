
def is_shifted(lst1, lst2):
  res = lst1[0]-lst2[0]
  
  for i in range(1, len(lst1)):
    if lst1[i]-lst2[i] != res: return False
  return True
​
def is_multiplied(lst1, lst2):
  res = lst2[0]/lst1[0]
  
  for i in range(1, len(lst1)):
    if lst2[i]/lst1[i] != res: return False
  return True


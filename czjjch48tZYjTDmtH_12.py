
def is_shifted(lst1, lst2):
  d1 = []
  d2 = []
  for i in range(len(lst1)):
    d1.append(abs(lst2[i])-lst1[i])
    d2.append(abs(lst2[i])+lst1[i])
  if len(set(d1)) == 1:
    return True
  elif len(set(d2)) == 1:
    return True
  return False
​
def is_multiplied(lst1, lst2):
  d1 = []
  d2 = []
  for i in range(len(lst1)):
    d1.append(abs(lst2[i])*lst1[i])
    d2.append(abs(lst2[i])/lst1[i])
  if len(set(d1)) == 1:
    return True
  elif len(set(d2)) == 1:
    return True
  return False


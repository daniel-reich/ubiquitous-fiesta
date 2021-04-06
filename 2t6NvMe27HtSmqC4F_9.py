
def boolean_and(lst):
  return not False in lst
​
def boolean_or(lst):
  return True in lst
  
def boolean_xor(lst):
  while len(lst) > 1:
    tmp = []
    for i in range(len(lst)-1):
      a, b = lst[i:i+2]
      if (a or b) and not (a and b): tmp.append(True)
      else: tmp.append(False)
    lst = tmp[:]
  return tmp[0]



def boolean_and(lst):
  for i in range(1,len(lst)):
    if lst[i-1] and lst[i]:
      lst[i] = True
    else:
      lst[i] = False
  return lst[-1]
​
def boolean_or(lst):
  for i in range(1,len(lst)):
    if lst[i-1] or lst[i]:
      lst[i] = True
    else:
      lst[i] = False
  return lst[-1]
​
def boolean_xor(lst):
  for i in range(1,len(lst)):
    if lst[i-1] != lst[i]:
      lst[i] = True
    else:
      lst[i] = False
  return lst[-1]


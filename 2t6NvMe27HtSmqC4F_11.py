
def boolean_and(lst):
  while len(lst)>1:
    x = lst[0] & lst[1]
    lst = [x] + lst[2:]
  return lst[0]
​
def boolean_or(lst):
  while len(lst)>1:
    x = lst[0] | lst[1]
    lst = [x] + lst[2:]
  return lst[0]
​
def boolean_xor(lst):
  while len(lst)>1:
    x = lst[0] ^ lst[1]
    lst = [x] + lst[2:]
  return lst[0]


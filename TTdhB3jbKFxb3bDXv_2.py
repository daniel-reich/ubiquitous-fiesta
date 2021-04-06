
def left_shift(lst, n):
  for counter in range(n):
    lst.append(lst.pop(0))
  return lst
  
def right_shift(lst, n):
  for counter in range(n):
    lst.insert(0,lst.pop())
  return lst


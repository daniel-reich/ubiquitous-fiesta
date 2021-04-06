
def left_shift(lst, n):
  for i in range(n):
    lst.insert(len(lst),lst[0])
    lst.pop(0)
  return lst
​
def right_shift(lst, n):
  for i in range(n):
    lst.insert(0,lst[-1])
    lst.pop()
  return lst


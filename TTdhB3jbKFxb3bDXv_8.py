
def left_shift(lst, n):
  for i in range (n):
    lst=lst[1:]+[lst[0]]
  return lst
​
def right_shift(lst, n):
  for i in range (n):
    lst=[lst[-1]]+lst[:-1]
  return lst


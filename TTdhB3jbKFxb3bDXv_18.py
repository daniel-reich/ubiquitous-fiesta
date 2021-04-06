
def left_shift(lst, n):
  while n != 0:
    lst = lst[1:] + lst[0:1]
    n = n - 1
  return lst
​
def right_shift(lst, n):
  while n != 0:
    lst = lst[-1:] + lst[:-1]
    n = n - 1
  return lst


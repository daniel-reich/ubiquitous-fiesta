
def left_shift(lst, n):
  if n > len(lst):
    n -= len(lst)
  return lst[n:]+lst[:n]
​
def right_shift(lst, n):
  if n > len(lst):
    n -= len(lst)
  return lst[abs(len(lst)-n):]+lst[:abs(len(lst)-n)]



def left_shift(lst, n):
  if n>len(lst):  x=n%len(lst)
  else: x=n
  return lst[x:] + lst[:x]
​
def right_shift(lst, n):
  if n>len(lst):  x=n%len(lst)
  else: x=n
  return lst[-x:] + lst[:-x]


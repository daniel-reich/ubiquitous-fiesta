
def left_shift(lst, n):
  if n < len(lst):
    return lst[n:] + lst[:n]
  else:
    return lst[n-len(lst):] + lst[:n-len(lst)]
​
def right_shift(lst, n):
  return lst[-n:] + lst[:-n]



def left_shift(lst, n):
  n = n % len(lst)
  return lst[n:] + lst[:n]
​
def right_shift(lst, n):
  n = n % len(lst)
  return lst[-n:] + lst[:-n]


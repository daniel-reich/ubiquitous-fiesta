
def left_shift(lst, n):
  n %= len(lst)
  return lst[n:] + lst[:n]
​
def right_shift(lst, n):
  return left_shift(lst, len(lst) - n)


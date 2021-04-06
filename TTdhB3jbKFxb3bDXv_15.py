
def left_shift(lst, n):
  a = len(lst)
  return lst[n % a:] + lst[:n % a]
​
def right_shift(lst, n):
  a = len(lst)
  return lst[(a - n) % a:] + lst[:(a - n) % a]


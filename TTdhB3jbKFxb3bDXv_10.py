
def left_shift(lst, n):
  return lst[n%5:] + lst[:n%5]
​
def right_shift(lst, n):
  return lst[len(lst) - n%5:] + lst[:len(lst) - n%5]


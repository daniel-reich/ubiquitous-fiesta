
def left_shift(lst, n):
  return lst[n%len(lst):] + lst[:n%len(lst)]
​
def right_shift(lst, n):
  return lst[-n%len(lst):] + lst[:-n%len(lst)]


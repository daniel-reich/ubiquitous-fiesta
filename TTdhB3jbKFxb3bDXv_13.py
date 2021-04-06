
def left_shift(lst, n):
  return [lst[(i+n)%len(lst)] for i in range(len(lst))]
​
def right_shift(lst, n):
  return [lst[(i-n)%len(lst)] for i in range(len(lst))]


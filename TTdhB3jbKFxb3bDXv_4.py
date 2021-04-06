
def left_shift(lst, n):
  if n > len(lst):
    n = n % len(lst)
  lst = lst[n:] + lst[0:n]
  return lst
  
def right_shift(lst, n):
  if n > len(lst):
    n = n % len(lst)
  lst = lst[len(lst)-n:] + lst[0:len(lst)-n]
  return lst


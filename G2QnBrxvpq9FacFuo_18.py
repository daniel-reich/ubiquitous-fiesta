
def possible_path(lst):
  a = all(i=='H' for i in lst[::2])
  b = all(i=="H" for i in lst[1::2])
  return a or b


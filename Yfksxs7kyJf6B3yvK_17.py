
def min_miss_pos(lst):
  x = 1
  while True:
    if x not in lst:
      return x
    x += 1


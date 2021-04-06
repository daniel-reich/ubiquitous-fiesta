
def min_miss_pos(lst):
  for x in range(1, max(lst) + 2):
    if lst.count(x) == 0:
      return x


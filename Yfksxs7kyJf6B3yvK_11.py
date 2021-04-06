
def min_miss_pos(lst):
  for x in range(1, max(lst)+2):
    if x not in lst:
      return x


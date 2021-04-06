
def min_miss_pos(lst):
  for n in sorted(lst):
    if n>=0 and n+1 not in lst:
      return n+1


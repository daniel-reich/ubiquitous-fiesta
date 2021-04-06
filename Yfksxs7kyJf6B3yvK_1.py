
def min_miss_pos(lst):
  return min(n for n in range(1,len(lst)+2) if n not in lst)


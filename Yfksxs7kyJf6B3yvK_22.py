
def min_miss_pos(lst):
  lst = sorted(i for i in lst if i>=0)
  for i,j in zip(lst,lst[1:]):
    if j-i > 1:
      return i + 1
  return lst[-1] + 1


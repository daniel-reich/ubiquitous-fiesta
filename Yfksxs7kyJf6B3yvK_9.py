
def min_miss_pos(lst):
  lst = sorted(set(lst))
  lst = [k for k in lst if k >=1]
  current = 1
  if len(lst)==0:
      return 1
  for i in lst:
    if current != i:
      return current
    current = i+1
    if i == lst[-1]:
      return current


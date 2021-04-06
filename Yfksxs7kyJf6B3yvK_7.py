
def min_miss_pos(lst):
  lst = sorted(set(lst))
  a = []
  for i in range(len(lst)-1):
    if lst[i] + 1 != lst[i+1]:
      if lst[i] + 1 > 0:
        return lst[i] + 1
​
  return lst[-1] + 1


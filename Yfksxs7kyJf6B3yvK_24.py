
def min_miss_pos(lst):
  lst1 = sorted(list(dict.fromkeys(lst)))
  if max(lst1) <= 0:
    return 1
  lst2 = [num for num in range(1,max(lst1)+2) if num not in lst1]
  return lst2[0]


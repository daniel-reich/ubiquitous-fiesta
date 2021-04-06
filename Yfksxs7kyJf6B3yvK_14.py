
def min_miss_pos(lst):
  lst2 = [i for i in range(1, max(lst)+1) if i not in sorted(set([i for i in lst if i>0]))]
  return max(lst)+1 if not lst2 else lst2[0]


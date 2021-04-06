
def min_miss_pos(lst):
  for i in range(min(list([x for x in sorted(lst) if x >= 0])),max(list([x for x in sorted(lst) if x >= 0]))):
    if i not in list([x for x in sorted(lst) if x >= 0]):
      return i
  return max(list([x for x in sorted(lst) if x >= 0]))+1


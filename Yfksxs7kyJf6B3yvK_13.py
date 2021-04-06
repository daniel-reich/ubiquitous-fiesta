
def min_miss_pos(lst):
  for i in range(1, abs(max(lst)) + 2):
    if i not in lst: 
      return i


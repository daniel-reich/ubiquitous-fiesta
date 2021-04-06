
def left_side(lst):
  return [sum([1 for j in lst[:i] if lst[i] > j]) for i in range(len(lst))]
  
def right_side(lst):
  return [sum([1 for j in lst[i:] if lst[i] > j]) for i in range(len(lst))]


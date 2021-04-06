
def left_side(lst):
  return [[lst[x] < lst[i] for x in range(i)].count(True) if i != 0 else 0 for i in range(len(lst))]
  
​
def right_side(lst):
  return [[lst[x] < lst[i] for x in range(i+1, len(lst))].count(True) if i != len(lst) - 1 else 0 for i in range(len(lst))]


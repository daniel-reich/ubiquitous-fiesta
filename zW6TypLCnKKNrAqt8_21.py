
def left_side(lst):
  return [sum(1 for i in lst[:j] if lst[j]>i) for j in range(len(lst))]
​
def right_side(lst):
  return [sum(1 for i in lst[j+1:] if lst[j]>i) for j in range(len(lst))]



def left_side(lst):
  return [sum(1 for i in lst[:j] if i<lst[j]) for j in range(len(lst))]
​
def right_side(lst):
  return [sum(1 for i in lst[j+1:] if i<lst[j]) for j in range(len(lst))]


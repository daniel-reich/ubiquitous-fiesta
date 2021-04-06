
def left_side(lst):
  return [sum(1 for j in range(i) if lst[j] < lst[i]) for i in range(len(lst))]
​
​
def right_side(lst):
  return [sum(1 for j in range(i,len(lst)) if lst[j] < lst[i]) for i in range(len(lst))]


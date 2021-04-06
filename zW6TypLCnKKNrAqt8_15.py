
def left_side(lst):
  e = list(enumerate(lst))
  return [sum(j>y for x,y in e[:i]) for i,j in e]
​
def right_side(lst):
  e = list(enumerate(lst))
  return [sum(j>y for x,y in e[i:]) for i,j in e]


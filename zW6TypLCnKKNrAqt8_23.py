
def left_side(lst):
  l = []
  for i in range(len(lst)):
    l.append(sum(1 for x in lst[0:i] if x<lst[i]))
  return l
    
def right_side(lst):
  l = []
  for i in range(len(lst)):
    l.append(sum(1 for x in lst[i+1:] if x<lst[i]))
  return l



def complete_square(lst):
  x = max(len(lst), len(lst[0]))
  while len(lst) < x:
    lst.append([0] * x) 
  for i in lst:
    while len(i) < x:
      i.append(0)
  return lst


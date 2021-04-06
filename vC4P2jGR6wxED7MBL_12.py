
def larger_than_right(lst):
  fin = []
  for k,v in enumerate(lst):
    if k == len(lst)-1:
      fin.append(lst[k])
      break
    if v > max(lst[k+1:]):
      fin.append(lst[k])
  return fin


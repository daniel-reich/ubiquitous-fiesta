
def complete_square(lst):
  n=len(lst)-len(lst[0])
  if n < 0: return lst + [[0]*len(lst[0])]*-n
  return [l+[0]*n for l in lst]


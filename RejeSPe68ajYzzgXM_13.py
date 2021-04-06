
def combine(lst):
  d={}
  for i in range(0, len(lst), 2):
    d[lst[i][0]]=[lst[i][2], lst[i+1][2]]
  return d


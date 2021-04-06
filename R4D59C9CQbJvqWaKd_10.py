
def batting_avg(lst):
  hits, official  = 0, 0
  for i, j in lst:
    hits += i
    official += j
    
  return '{:.3f}'.format(hits / official).lstrip('0')


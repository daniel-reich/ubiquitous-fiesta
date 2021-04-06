
def bitwise_index(lst):
  num, ndx = float('-inf'), 0
  for i, n in enumerate(lst):
    if not n&1:
      if n > num:
        num = n
        ndx = i
  if isinstance(num, float):
    return 'No even integer found!'
    
  par = 'even' if not ndx&1 else 'odd'
  return {'@{} index {}'.format(par, ndx): num}


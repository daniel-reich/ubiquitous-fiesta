
def widen_streets(lst, n):
  return [x.replace('  ',' *').replace(' ',' '*n).replace(' *','  ') for x in lst]


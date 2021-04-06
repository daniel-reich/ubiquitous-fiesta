
def relation_lst(lst):
  result = list( (y,x) for x in lst for y in lst if x >= y )
  result.sort( key = lambda t: (t[0],t[1]) )
  return result


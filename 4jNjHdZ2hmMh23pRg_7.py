
def cutting_grass(lst, *cuts):
  def to_cut(lst, cut):
    nl = []
    for item in lst:
      nl.append(item - cut)
    return nl
  
  results = []
  l = lst
  for cut in cuts:
    if l != 'Done':
      c = to_cut(l, cut)
      if 0 in c:
        results.append('Done')
      else:
        results.append(c)
​
      l = results[-1]
    else:
      results.append('Done')
  
  return results


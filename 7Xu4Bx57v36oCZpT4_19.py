
def where_is_waldo(lst):
  waldo = max(w for l in lst for w in l)
  col = [l for l in lst if waldo in l ]
  return [lst.index(col[0])+1,col[0].index(waldo)+1]


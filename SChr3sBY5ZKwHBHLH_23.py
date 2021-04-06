
def sort_it(lst):
  def _sortfunc(l):
    try:
      return l[0]
    except TypeError:
      return l
      
  return sorted(lst, key=_sortfunc)


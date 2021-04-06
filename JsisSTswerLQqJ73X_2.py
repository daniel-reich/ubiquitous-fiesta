
def priority_sort(lst, s):
  def _sortfunc(x):
    if x in s:
      return (0, x)
    return (1, x)
  return sorted(lst, key=_sortfunc)


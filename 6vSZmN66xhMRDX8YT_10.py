
def advanced_sort(lst):
  return sorted(([s]*lst.count(s) for s in set(lst)), key=lambda x: lst.index(x[0]))


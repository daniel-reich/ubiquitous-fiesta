
def holey_sort(lst):
  return sorted(lst, key = lambda x: sum(["046889".count(i) for i in str(x)]))


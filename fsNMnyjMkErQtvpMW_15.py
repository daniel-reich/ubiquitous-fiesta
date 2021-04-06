
def holey_sort(lst):
  return [x[1] for x in sorted(([sum([str(i).count(j) for j in "046889"]), i] for i in lst), key=lambda x: (x[0], lst))]


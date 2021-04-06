
def even_last(lst):
  return 0 if not len(lst) else \
     sum(i for idx, i in enumerate(lst) if not idx % 2) * lst[-1]


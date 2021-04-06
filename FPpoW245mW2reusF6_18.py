
def even_last(lst):
  return sum(j * lst[-1] for i, j in enumerate(lst) if i % 2 == 0)


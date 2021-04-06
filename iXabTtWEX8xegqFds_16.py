
def alternate_sort(lst):
  x, y = [i for i in lst if isinstance(i, int)], [j for j in lst if isinstance(j, str)]
  return [x for y in [[a, b] for a, b in zip(sorted(x), sorted(y))] for x in y]


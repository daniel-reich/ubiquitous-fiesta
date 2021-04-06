
def combo(lst, n):
  import itertools
  return [list(elem) for elem in itertools.combinations(lst, n)]


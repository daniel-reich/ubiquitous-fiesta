
import itertools
def combinator(lst, sep=""):
  if lst == [[]]:
    return []
  if len(lst) == 1:
    return lst[0]
  for i, l in enumerate(lst):
    if type(l) == str:
      lst[i] = list(l)
  pairs = list(itertools.product(*lst))
  try:
    return list(map(lambda pair: sep.join(pair), pairs))
  except IndexError:
    return []


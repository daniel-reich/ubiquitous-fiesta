
import itertools
def combinator(lst: list, combiner='') -> list:
  return list(map(combiner.join, itertools.product(*lst)))



import itertools
def relation_lst(lst):
  return list(itertools.combinations_with_replacement(sorted(lst),2))


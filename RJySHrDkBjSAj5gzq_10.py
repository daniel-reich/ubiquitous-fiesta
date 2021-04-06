
import itertools as it
def nespers(lst):
  nes = len(list(it.permutations(lst, len(lst))))
  if all(type(i)!=list for i in lst): return nes
  for i in lst:
    if type(i)==list:
      nes *= nespers(i)
  return nes


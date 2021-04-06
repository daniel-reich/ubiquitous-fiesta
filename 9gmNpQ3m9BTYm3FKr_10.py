
import itertools
def lucky_seven(lst):
  for x in list(itertools.combinations(lst, 3)):
    if sum(x) == 7:
      return True
  return False


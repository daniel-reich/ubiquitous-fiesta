
import itertools
def lucky_seven(lst):
  for comb in itertools.combinations(lst,3):
    if sum(comb) == 7:
      return True
  return False


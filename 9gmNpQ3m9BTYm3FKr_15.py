
import itertools;
​
def lucky_seven(lst):
  for combination in itertools.combinations(lst, 3):
    if sum(combination) == 7:
      return True
    else:
      continue
  return False


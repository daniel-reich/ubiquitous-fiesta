
def lucky_seven(lst):
  import itertools as it
  for j in it.combinations(lst,3):
    if (sum(j))==7:
      return True
  else:
    return False


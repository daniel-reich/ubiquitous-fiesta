
def letter_check(lst):
  lst[0] = [x.lower() for x in lst[0]]
  lst[1] = [x.lower() for x in lst[1]]
  return set(lst[1]).issubset(set(lst[0]))


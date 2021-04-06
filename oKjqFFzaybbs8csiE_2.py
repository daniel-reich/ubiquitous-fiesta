
def cons(lst):
  if sorted(lst) == [x for x in range(min(lst), max(lst) + 1)]:
    return True
  return False


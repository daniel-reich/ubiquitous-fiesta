
def cons(lst):
  if len(lst)-1 + sorted(lst)[0]!=sorted(lst)[-1]:
    return False
  return len(lst)==len(sorted(lst))


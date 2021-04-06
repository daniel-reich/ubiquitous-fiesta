
def how_many_missing(lst):
  if len(lst) == 1 or len(lst) == 0:
    return 0
  orgLst = [x for x in range(lst[0], lst[-1] +1)]
  lst = set(lst)
  return len(list(lst ^ set(orgLst)))


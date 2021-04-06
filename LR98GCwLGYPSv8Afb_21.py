
def pluralize(lst):
  plurals = []
  for i in lst:
    if lst.count(i) > 1:
      plurals += [i + 's']
    else:
      plurals += [i]
  plurals_set = set(plurals)
  return plurals_set


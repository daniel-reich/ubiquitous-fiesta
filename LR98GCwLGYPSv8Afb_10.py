
def pluralize(lst):
  nl = []
  for item in lst:
    if lst.count(item) == 1:
      nl.append(item)
    if lst.count(item) > 1:
      x = '{}s'.format(item)
      nl.append(x)
  return set(nl)


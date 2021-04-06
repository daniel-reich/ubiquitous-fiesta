
def pluralize(lst):
  return set(i + "s" if lst.count(i)> 1 else i for i in lst)


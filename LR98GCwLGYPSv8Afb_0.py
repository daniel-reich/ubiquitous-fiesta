
def pluralize(lst):
  return set(i + 's'*(lst.count(i)>1) for i in lst)


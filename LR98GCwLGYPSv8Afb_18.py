
def pluralize(lst):
  plurals = set()
  a = set(lst)
  for word in a:
    if lst.count(word) > 1:
      plurals.add(word + "s")
    else:
      plurals.add(word)
  return plurals


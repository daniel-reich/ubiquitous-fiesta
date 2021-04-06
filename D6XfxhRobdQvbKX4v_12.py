
def first_before_second(s, first, second):
  filtered = ''.join([x for x in s if x in ([first, second])])
  return filtered.rfind(first) < filtered.index(second)


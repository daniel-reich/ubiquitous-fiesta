
def reversible_inclusive_list(start, end, lst=[]):
  if start == end:
    return lst + [start]
  return reversible_inclusive_list(start + 1, end, lst + [start]) if start < end else reversible_inclusive_list(start - 1, end, lst + [start])


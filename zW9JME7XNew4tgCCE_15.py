
def reversible_inclusive_list(start, end):
  if start < end:
    return list(range(start, end + 1))
  elif start > end:
    return list(reversed(list(range(end, start + 1))))
  else:
    return [end]



def reversible_inclusive_list(start, end, res = []):
  if start == end: return res + [end]
  step = 1 if start < end else -1
  return reversible_inclusive_list(start + step, end, res + [start])


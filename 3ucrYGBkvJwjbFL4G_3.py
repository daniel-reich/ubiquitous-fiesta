
def reversible_inclusive_list(start, end):
  if start == end:
    return [start]
  if start < end:
    return [start] + reversible_inclusive_list(start+1, end)
  else:
    return [start] + reversible_inclusive_list(start-1, end)


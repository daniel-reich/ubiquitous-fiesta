
def reversible_inclusive_list(start, end):
  if start == end:
    return [start]
  elif start > end:
       return [start] + reversible_inclusive_list(start-1, end)
  elif start < end:
    return [start] + reversible_inclusive_list(start+1, end)


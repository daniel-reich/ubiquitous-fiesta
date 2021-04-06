
def reversible_inclusive_list(sr, er):
  if sr > er:
    return list(range(sr,er-1, -1))
  return list(range(sr, er+1))

